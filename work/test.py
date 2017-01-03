import pandas as pd
import re

df_enrl = pd.read_csv('enrollment_data/CLE-GSE-201604.csv')
df_enrl = df_enrl.fillna('')
meeting_location_values = ['OFFCAM', 'TBA', 'WEB', '']
df_enrl = df_enrl[~df_enrl['Meeting_Location_1'].isin(meeting_location_values)]
df_enrl = df_enrl[df_enrl['Crosslist_ID'] == '']