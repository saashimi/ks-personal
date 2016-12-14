import pandas as pd

#df is a dataframe
meeting_location_values = ['OFFCAM', 'TBA', 'WEB', 'NaN']
df = pd.read_csv('CLE-GSE-201604.csv')
#print df.columns.values
df[~df['Meeting_Location_1'].isin(meeting_location_values)]


