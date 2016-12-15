import pandas as pd

pd.set_option('display.max_rows', -1)

#df is a dataframe
meeting_location_values = ['OFFCAM', 'TBA', 'WEB', '']
df = pd.read_csv('CLE-GSE-201604.csv')
#print df.columns.values
#df = df.fillna('') #fill all null values with empty space
#valid_classes = df.loc[~df['Meeting_Location_1'].isin(meeting_location_values)]
#df[~df['Meeting_Location_1'].isin(meeting_location_values)]
#crosslist = df.groupby('Crosslist_ID')
