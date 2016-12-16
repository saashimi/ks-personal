"""
class_parse.py 
A script that calculates csv files generated from DATAMASTER.
"""

import pandas as pd

pd.set_option('display.max_rows', 0)

df = pd.read_csv('CLE-GSE-201604.csv')

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

# Calculate necessary statistics
tot_class = xlist_count + reg_count
avg_enrl = int(round((xlist_actual_enrl + reg_actual_enrl) / (xlist_count +  reg_count)))
avg_auth = int(round((xlist_auth_size + reg_auth_size) /  (xlist_count +  reg_count)))
avg_cap =  (xlist_actual_enrl + reg_actual_enrl) / (xlist_auth_size + reg_auth_size)


print(
    "Total classes for this quarter: {0}".format(tot_class), '\n'
    "Average classroom capacity: {0}".format(avg_auth), '\n',
    "Average enrollment: {0}".format(avg_enrl), '\n',
    "Average capacity: {0}".format(avg_cap)
)

#TODO: Range of times for class. (Morning, Afternoon, Evening)

#valid_classes = df.loc[~df['Meeting_Location_1'].isin(meeting_location_values)]
