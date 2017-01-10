import pandas as pd
import re
import datetime

#pd.options.mode.chained_assignment = None
current_term = 201604

def aggregate(df_in):
# Aggregate arithmetic operations:
    operations = {'Weekly_Class_Hours' : 'sum', '%_Capacity' : 'mean', 'Actual_Enrl' : 'mean'}
    df_in.groupby('Meeting_Location_1', as_index=False).agg(operations)

    # Calculate hourly utilizations
    df_in['Class_Hour_Utilization'] = (df_in['Weekly_Class_Hours']/40.0).astype(float)

    # Round optimal size to the nearest 5
    df_in['Optimal_Size'] = 5 * round((df_in['Actual_Enrl'] * 1.25)/5)
    # Optimal size should be a minimum of 10 seats
    df_in.loc[df_in['Optimal_Size'] < 10.0, 'Optimal_Size'] = 10.0
    return df_in


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
df['End_Time'] = df['Meeting_Times'].str.extract('((?<=-).*$)', expand=True)
#df['Start_Time'] = '{0}:{1}'.format(df['Start_Time'][:-2], df['Start_Time'][-2:])
########TODO: Convert string to datetime

# Avoid classes that only occur on a single day
df = df.loc[df['Start_Date'] != df['End_Date']]


# Calculate number of days per week and treat Sunday condition
for row in df['Days']:
    if 'SU' in row:
        print('Sunday Condition!')
        # ToDO: If sunday does come up, refactor code to address this.
    else:
        df['Days_Per_Week'] = df['Days'].str.len()

df['%_Capacity'] = df['Actual_Enrl'].astype(float) / df['Max_Enrl'].astype(float) 
df['Actual_Enrl'] = df['Actual_Enrl'].astype(int)

x_list_operations = {'Actual_Enrl' : 'sum', 'Xlst_Max_Enrl' : 'max'}
df_xlist = df.groupby('Xlst', as_index=False).agg(x_list_operations)
print(df_xlist)


print(df[['Class', 'ROOM', '%_Capacity', 'Xlst', 'Start_Date', 'End_Date', 'Days', 'Actual_Enrl']])