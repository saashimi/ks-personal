import pandas as pd
import re
import datetime

#pd.options.mode.chained_assignment = None
current_term = 201604

def aggregate(df_agg):
    # Aggregate arithmetic operations:
    operations = ({'Weekly_Class_Hours' : 'sum', 
                   '%_Capacity' : 'mean', 
                   'Actual_Enrl' : 'mean'})
    df_agg.groupby('Meeting_Location_1', as_index=False).agg(operations)

    # Calculate hourly utilizations
    df_agg['Class_Hour_Utilization'] = (df_agg['Weekly_Class_Hours']/40.0).astype(float)

    # Round optimal size to the nearest 5
    df_agg['Optimal_Size'] = 5 * round((df_agg['Actual_Enrl'] * 1.25)/5)
    # Optimal size should be a minimum of 10 seats
    df_agg.loc[df_agg['Optimal_Size'] < 10.0, 'Optimal_Size'] = 10.0
    return df_agg

def merge_xlist(df_xl):
    # merge the crosslised classes
    xl_operations = ({'Actual_Enrl' : 'sum', 
                          'Room_Capacity' : 'max'})
    df_xl = df_xl.groupby('Xlst', as_index=False).agg(xl_operations)
    df_xl['%_Capacity'] = df_xl['Actual_Enrl'] / df_xl['Room_Capacity'].astype(int)
    #df_xl.drop('Xlst_Max_Enrl', axis=1, inplace=True)
    return df_xl


df = pd.read_csv('classroom_data/PSU_master_classroom.csv')
df = df.fillna('')

#Clean for 201604 Data:
terms = ['201604']
df = df[df['Term'].isin(terms)]

df_classes = pd.read_csv('enrollment_data/CLE-GSE-{0}.csv'.format(current_term))
df_classes['Class_'] = df_classes['Subj'] + " " + df_classes['Course'] 
valid_class_list = set(df_classes['Class_'].tolist())

df = df.loc[df['Class'].isin(valid_class_list)]


#df_joined = pd.merge(df, df_classes, left_on=df['Class'], right_on=df_classes['Class_'], how='inner')

# Split Meeting times into Days of the week, Start time, and End time
# Regex searches
df['Days'] = df['Meeting_Times'].str.extract('([^\s]+)', expand=True)
df['Start_Date'] = df['Meeting_Dates'].str.extract('^(.*?)-', expand=True)
df['End_Date'] = df['Meeting_Dates'].str.extract('((?<=-).*$)', expand=True)
df['Start_Time'] = df['Meeting_Times'].str.extract('(?<= )(.*)(?=-)', expand=True)
df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='%H%M')
df['End_Time'] = df['Meeting_Times'].str.extract('((?<=-).*$)', expand=True)
df['End_Time'] = pd.to_datetime(df['End_Time'], format='%H%M')
df['Duration_Hr'] = ((df['End_Time'] - df['Start_Time']).dt.seconds)/3600

# Avoid classes that only occur on a single day
df = df.loc[df['Start_Date'] != df['End_Date']]

# Calculate number of days per week and treat Sunday condition
for row in df['Days']:
    if 'SU' in row:
        print('Sunday Condition!')
        # ToDO: If sunday does come up, refactor code to address this.
    else:
        df['Days_Per_Week'] = df['Days'].str.len()

df['%_Capacity'] = df['Actual_Enrl'].astype(int) / df['Room_Capacity'].astype(int) 
df['Actual_Enrl'] = df['Actual_Enrl'].astype(int)

### This is a useful lambda example
#df['Xlst_Max_Enrl'] = df['Xlst_Max_Enrl'].apply(lambda x: x if (x != '') else '0')
####

df_xlist = merge_xlist(df)
print(df_xlist)


#print(df[['Class', 'ROOM', '%_Capacity', 'Xlst', 'Start_Date', 'End_Date', 'Days', 'Actual_Enrl', 'Duration_Hr']])