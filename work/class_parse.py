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
master_times = []
master_morning = []
master_afternoon = []
master_evening = []


def clean_day_time(df_day_time):
    #Clean meeting times
    split_times = []
    meeting_times = df_day_time.Meeting_Time_1.tolist()
    day_list = []
    start_times = []
    for time in meeting_times:
        split_times.append(re.findall(r"[\w]+", time))
    for list_ in split_times:
        try:
            day = list_[0]
            start_time = list_[1]
            master_times.append(start_time)
            start_times.append(start_time)
            if 'SU' in day:
                print('Sunday condition!')
            else:
                for char in day:
                    day_list.append(char)
        except:
            print('WARNING: A class is missing a date/time! and will not be counted!')
            continue

    morning = []
    afternoon = []
    evening = []
    for time in start_times:
        time = int(time)
        if time > 700 and time < 1200:
            morning.append(time)
            master_morning.append(time)
        if time >= 1200 and time < 1700:
            afternoon.append(time)
            master_afternoon.append(time)
        if time >1700:
            evening.append(time)
            master_evening.append(time)
    for day in days:
        print(" ", day, ": {:.0%}".format(day_list.count(day)/len(day_list)))

    print(" Morning classes: {:.0%}".format(len(morning)/len(start_times)),'\n'
    " Afternoon classes: {:.0%}".format(len(afternoon)/len(start_times)), '\n'
    " Evening classes: {:.0%}".format(len(evening)/len(start_times)))
    print(' =============================================================','\n'
    )



def compile_reg_classes_and_xlist_classes(df_reg_xlist, current_term):
    # Group the crosslisted classes and calculate their sums.
    xlist = df_reg_xlist.groupby('Crosslist_ID').Actual_Enrl
    xlist_count = len(xlist) - 1
    xlist_actual_enrl = (df_reg_xlist.groupby('Crosslist_ID').Actual_Enrl.sum())[0]
    xlist_auth_size = (df_reg_xlist.groupby('Crosslist_ID').Auth_Size.sum())[0]

    # Count the regular classes and calculate their sums.
    reg_count = df_reg_xlist.shape[0]
    reg_actual_enrl = df_reg_xlist.Actual_Enrl.sum()
    reg_auth_size = df_reg_xlist.Auth_Size.sum()

    # Calculate necessary statistics.
    tot_class = xlist_count + reg_count
    avg_enrl = int(round((xlist_actual_enrl + reg_actual_enrl) / (xlist_count +  reg_count)))
    avg_auth = int(round((xlist_auth_size + reg_auth_size) /  (xlist_count +  reg_count)))
    avg_cap =  (xlist_actual_enrl + reg_actual_enrl) / (xlist_auth_size + reg_auth_size)    

    # Append to master counts
    master_classes.append(tot_class)
    master_enrls.append(xlist_actual_enrl + reg_actual_enrl)
    master_auths.append(xlist_auth_size + reg_auth_size)

    print('\n','=============================================================','\n'
    " Total classes for {0}: {1}".format(current_term, tot_class),'\n'
    " Average classroom capacity: {0}".format(avg_auth),'\n',
    "Average enrollment per class: {0}".format(avg_enrl),'\n',
    "Average capacity per classroom: {:.0%}".format(avg_cap)
    )
    clean_day_time(df_reg_xlist)

def print_summary():
    print('\n','=============================================================','\n'
        " Average number of classes for ALL TERMS: {0}".format(int(round(np.mean(master_classes)))),'\n'
        " Average classroom capacity for ALL TERMS: {0}".format(int(round(sum(master_auths)/sum(master_classes)))),'\n',
        "Average enrollment per class for ALL TERMS: {0}".format(int(round(sum(master_enrls)/sum(master_classes)))),'\n',
        "Average capacity per classroom for ALL TERMS: {:.0%}".format(sum(master_enrls)/sum(master_auths)),'\n',
        "Morning classes: {:.0%}".format(len(master_morning)/len(master_times)),'\n',
        "Afternoon classes: {:.0%}".format(len(master_afternoon)/len(master_times)), '\n',
        "Evening classes: {:.0%}".format(len(master_evening)/len(master_times)), '\n',
    '=============================================================','\n'
    )

def main():
    for year in years:
        for quarter in quarters:
            current_term = year + quarter
            df = pd.read_csv('CLE-SPH-{0}.csv'.format(current_term))
            df = df.fillna('') #fill all null values with empty space
            #Give us classes that have actual physical meeting locations, e.g. NOT in the 
            #following locations:
            meeting_location_values = ['OFFCAM', 'TBA', 'WEB', '']
            df = df[~df['Meeting_Location_1'].isin(meeting_location_values)]
            compile_reg_classes_and_xlist_classes(df, current_term)
            print_summary()


if __name__=="__main__":
    main()