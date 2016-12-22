"""
class_parse.py 
A script that calculates csv files generated from DATAMASTER. Utilizes pandas
library for csv file manipulation.
"""

import pandas as pd
import numpy as np
import re

quarters = ['01', '02', '03', '04']
years = ['2013', '2014', '2015', '2016']
days = ['M', 'T', 'W', 'R', 'F', 'S', 'SU']
master_classes = []
master_enrls = [] 
master_auths = []

for year in years:
    for quarter in quarters:
        current_term = year + quarter

        df = pd.read_csv('CLE-GSE-{0}.csv'.format(current_term))
        df = df.fillna('') #fill all null values with empty space

        #Give us classes that have actual physical meeting locations, e.g. NOT in the 
        #following locations:
        meeting_location_values = ['OFFCAM', 'TBA', 'WEB', '']
        df = df[~df['Meeting_Location_1'].isin(meeting_location_values)]

        #Clean meeting times
        split_times = []
        meeting_times = df.Meeting_Time_1.tolist()
        day_list = []
        start_times = []
        for time in meeting_times:
            split_times.append(re.findall(r"[\w]+", time))
        for list_ in split_times:
            try:
                day = list_[0]
                start_time = list_[1]
                start_times.append(start_time)
                if 'SU' in day:
                    print('Sunday condition!')
                else:
                    for char in day:
                        day_list.append(char)
            except:
                print('WARNING: A class is missing a date/time!')
                continue


        
        # Group the crosslisted classes and calculate their sums.
        xlist = df.groupby('Crosslist_ID').Actual_Enrl
        xlist_count = len(xlist) - 1
        xlist_actual_enrl = (df.groupby('Crosslist_ID').Actual_Enrl.sum())[0]
        xlist_auth_size = (df.groupby('Crosslist_ID').Auth_Size.sum())[0]

        # Count the regular classes and calculate their sums.
        reg_count = df.shape[0]
        reg_actual_enrl = df.Actual_Enrl.sum()
        reg_auth_size = df.Auth_Size.sum()

        # Calculate necessary statistics.
        tot_class = xlist_count + reg_count
        avg_enrl = int(round((xlist_actual_enrl + reg_actual_enrl) / (xlist_count +  reg_count)))
        avg_auth = int(round((xlist_auth_size + reg_auth_size) /  (xlist_count +  reg_count)))
        avg_cap =  (xlist_actual_enrl + reg_actual_enrl) / (xlist_auth_size + reg_auth_size)

        morning = []
        afternoon = []
        evening = []
        for time in start_times:
            time = int(time)
            if time > 700 and time < 1200:
                morning.append(time)
            if time >= 1200 and time < 1700:
                afternoon.append(time)
            if time >1700:
                evening.append(time)
        print("Morning classes: ", len(morning)/len(start_times),'\n'
            "Afternoon classes: ", len(afternoon)/len(start_times), '\n'
            "Evening classes: ", len(evening)/len(start_times))


        # Append to master counts
        master_classes.append(tot_class)
        master_enrls.append(xlist_actual_enrl + reg_actual_enrl)
        master_auths.append(xlist_auth_size + reg_auth_size)


        print('\n','=============================================================','\n'
            " Total classes for {0}: {1}".format(current_term, tot_class),'\n'
            " Average classroom capacity: {0}".format(avg_auth),'\n',
            "Average enrollment per class: {0}".format(avg_enrl),'\n',
            "Average capacity per classroom: {0}".format(avg_cap)
        )
        for day in days:
            print(" ", day, ":", day_list.count(day))
        print(' =============================================================','\n'
        )

print('\n','=============================================================','\n'
    " Average number of classes for ALL TERMS: {0}".format(np.mean(master_classes)),'\n'
    " Average classroom capacity for ALL TERMS: {0}".format(sum(master_auths)/sum(master_classes)),'\n',
    "Average enrollment per class for ALL TERMS: {0}".format(sum(master_enrls)/sum(master_classes)),'\n',
    "Average capacity per classroom for ALL TERMS: {0}".format(sum(master_enrls)/sum(master_auths)),'\n',
    '=============================================================','\n'
)

#TODO: Range of times for class. (Morning, Afternoon, Evening)
#Output to txt file.
#valid_classes = df.loc[~df['Meeting_Location_1'].isin(meeting_location_values)]

#if __name__=="__main__":
#    main()