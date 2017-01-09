import pandas as pd
import re

df_enrl = pd.read_csv('enrollment_data/CLE-GSE-201604.csv')
df_enrl = df_enrl.fillna('')
meeting_location_values = ['OFFCAM', 'TBA', 'WEB', '']
df_enrl = df_enrl[~df_enrl['Meeting_Location_1'].isin(meeting_location_values)]
df_enrl = df_enrl[df_enrl['Crosslist_ID'] == '']

df_enrl['Days'] = df_enrl['Meeting_Time_1'].str.extract('([^\s]+)', expand=True)
# Regex searches all until first space
df_enrl['Start_Time'] = df_enrl['Meeting_Time_1'].str.extract('(?<= )(.*)(?=-)', expand=True)
df_enrl['Start_Time'] = df_enrl['Start_Time'].astype(int)
df_enrl['End_Time'] = df_enrl['Meeting_Time_1'].str.extract('((?<=-).*$)', expand=True)
df_enrl['End_Time'] = df_enrl['End_Time'].astype(int)
df_enrl['Class_Hours'] = (df_enrl['End_Time'] - df_enrl['Start_Time'])/60.

for row in df_enrl['Days']:
    if 'SU' in row:
        print('Sunday Condition!')
        # ToDO: If sunday does come up, refactor code to address this.
    else:
        df_enrl['Days_Per_Week'] = df_enrl['Days'].str.len()

df_enrl['Weekly_Class_Hours'] = df_enrl['Class_Hours'] * df_enrl['Days_Per_Week']

room_list = df_enrl.groupby('Meeting_Location_1')

print(room_list.Weekly_Class_Hours.sum())