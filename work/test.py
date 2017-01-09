import pandas as pd
import re




def clean_and_format(df):

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

    # Aggregate arithmetic operations:
    operations = {'Weekly_Class_Hours' : 'sum', '%_Capacity' : 'mean', 'Actual_Enrl' : 'mean'}
    df = df.groupby('Meeting_Location_1').agg(operations)

    # Calculate houly utilizations
    df['Class_Hour_Utilization'] = (df['Weekly_Class_Hours']/40.0).astype(float)

    # Round to the nearest 5
    df['Optimal_Size'] = 5 * round((df['Actual_Enrl'] * 1.25)/5)
    df.loc[df['Optimal_Size'] < 10.0, 'Optimal_Size'] = 10.0

    return df


df_raw = pd.read_csv('enrollment_data/CLE-GSE-201604.csv')
df_raw = df_raw.fillna('')

# Clean for meeting at physical campus locations:
meeting_location_values = ['OFFCAM', 'TBA', 'WEB', '']
df_raw = df_raw[~df_raw['Meeting_Location_1'].isin(meeting_location_values)]

df_reg_class = df_raw[df_raw['Crosslist_ID'] != ''] 
df_xlist = df_raw[df_raw['Crosslist_ID'] != '']

dfs = [clean_and_format(df_reg_class), clean_and_format(df_xlist)]
cleaned_df = pd.concat(dfs)


output=cleaned_df.groupby('Optimal_Size').count()
print(output)
