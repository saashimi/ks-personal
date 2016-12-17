"""
class_parse.py 
A script that calculates csv files generated from DATAMASTER. Utilizes pandas
library for csv file manipulation.
"""

import pandas as pd
import numpy as np

quarters = ['01', '02', '03', '04']
years = ['2013', '2014', '2015', '2016']
master_classes = []
master_enrls = [] 
master_auths = []

for year in years:
    for quarter in quarters:
        current_term = year + quarter

        #pd.set_option('display.max_rows', 0)
        df = pd.read_csv('CLE-GSE-{0}.csv'.format(current_term))
        df = df.fillna('') #fill all null values with empty space

        #Give us classes that have actual physical meeting locations, e.g. NOT in the 
        #following locations:
        meeting_location_values = ['OFFCAM', 'TBA', 'WEB', '']
        df = df[~df['Meeting_Location_1'].isin(meeting_location_values)]

        # Group the crosslisted classes and calculate their sums.
        xlist_count = len(df.groupby('Crosslist_ID').Actual_Enrl) - 1
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

        # Append to master counts
        master_classes.append(tot_class)
        master_enrls.append(xlist_actual_enrl + reg_actual_enrl)
        master_auths.append(xlist_auth_size + reg_auth_size)


        print('\n','=============================================================','\n'
            " Total classes for {0}: {1}".format(current_term, tot_class),'\n'
            " Average classroom capacity: {0}".format(avg_auth),'\n',
            "Average enrollment per class: {0}".format(avg_enrl),'\n',
            "Average capacity per classroom: {0}".format(avg_cap),'\n',
            '=============================================================','\n'
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