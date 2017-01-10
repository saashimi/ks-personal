import pandas as pd
import re

pd.options.mode.chained_assignment = None

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


df = pd.read_csv('enrollment_data/CLE-GSE-201604.csv')
df = df.fillna('')

# Clean for meeting at physical campus locations:
meeting_location_values = ['OFFCAM', 'TBA', 'WEB', '']
df = df[~df['Meeting_Location_1'].isin(meeting_location_values)]

# Split Meeting times into Days of the week, Start time, and End time
# Regex searches
df['Days'] = df['Meeting_Time_1'].str.extract('([^\s]+)', expand=True)
df['Start_Time'] = df['Meeting_Time_1'].str.extract('(?<= )(.*)(?=-)', expand=True)
df['Start_Time'] = df['Start_Time'].astype(int)
df['End_Time'] = df['Meeting_Time_1'].str.extract('((?<=-).*$)', expand=True)
df['End_Time'] = df['End_Time'].astype(int)

# Create new columns based on relevant data
df['Class_Hours'] = (df['End_Time'] - df['Start_Time'])/60.
df['%_Capacity'] = df['%_Capacity'].astype(float)

# Calculate number of days per week and treat Sunday condition
for row in df['Days']:
    if 'SU' in row:
        print('Sunday Condition!')
        # ToDO: If sunday does come up, refactor code to address this.
    else:
        df['Days_Per_Week'] = df['Days'].str.len()

df['Weekly_Class_Hours'] = df['Class_Hours'] * df['Days_Per_Week']

reg_class = df[df['Crosslist_ID'] == ''] 
xlist = df[df['Crosslist_ID'] != '']
xlist_operations = {'Actual_Enrl' : 'sum', 'Auth_Size' : 'max'}
xlist = xlist.groupby('Crosslist_ID', as_index=False).agg(xlist_operations)

#print(xlist)

df_reg_class = aggregate(reg_class)
#df_xlist = aggregate(xlist)


#dfs = [df_reg_class, df_xlist]
#cleaned_df = pd.concat(dfs)


output = df_reg_class.groupby('Optimal_Size').count()
print(output)
