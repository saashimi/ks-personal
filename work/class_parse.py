import pandas as pd
import re
import datetime

#pd.options.mode.chained_assignment = None

def aggregate(df_agg):
    # Aggregate arithmetic operations:
    #df_agg['Weekly_Class_Hours'] = df_agg['Weekly_Class_Hours'].astype(float)
    df_agg['Room_Capacity'] = df_agg['Room_Capacity'].astype(float)
    df_agg['Actual_Enrl'] = df_agg['Actual_Enrl'].astype(float)

    operations = ({'Weekly_Class_Hours' : 'sum', 
                   'Room_Capacity' : 'mean', 
                   'Actual_Enrl' : 'mean',})
    df_agg = df_agg.groupby('ROOM', as_index=False).agg(operations)

    # Calculate hourly utilizations
    df_agg['Class_Hour_Utilization'] = (df_agg['Weekly_Class_Hours']/40.0).astype(float)

    # Round optimal size to the nearest 5
    df_agg['Optimal_Size'] = 5 * round((df_agg['Actual_Enrl'] * 1.25)/5)
    # Optimal size should be a minimum of 10 seats
    df_agg.loc[df_agg['Optimal_Size'] < 10.0, 'Optimal_Size'] = 10.0
    return df_agg

def format_df_reg(df_reg):
    df_reg = df_reg.loc[df_reg['Xlst'] == '']
    #df_reg['Weekly_Class_Hours'] = df_reg['Duration_Hr'] * df_reg['Days_Per_Week']
    columns = ['ROOM', 'Actual_Enrl', 'Room_Capacity', 'Weekly_Class_Hours']
    df_reg = df_reg[columns]
    df_reg['%_Capacity'] = df_reg['Actual_Enrl'] / df_reg['Room_Capacity'].astype(int)
    return df_reg

def merge_xlist(df_xl):
    df_xl = df_xl.loc[df_xl['Xlst'] != '']

    # merge the crosslisted classes
    xl_operations = ({'ROOM' : 'max',
                      'Actual_Enrl' : 'sum', 
                      'Room_Capacity' : 'max',
                      'Weekly_Class_Hours' : 'max',})
    df_xl = df_xl.groupby('Xlst', as_index=False).agg(xl_operations)
    df_xl['%_Capacity'] = df_xl['Actual_Enrl'] / df_xl['Room_Capacity'].astype(int)
    return df_xl

def main():
    current_term = 201604
    df = pd.read_csv('classroom_data/PSU_master_classroom.csv')
    df = df.fillna('')

    #Clean for 201604 Data:
    terms = ['201604']
    df = df[df['Term'].isin(terms)]

    df_classes = pd.read_csv('enrollment_data/CLE-GSE-{0}.csv'.format(current_term))
    
    df_classes['Class_'] = df_classes['Subj'] + " " + df_classes['Course'] 
    valid_class_list = set(df_classes['Class_'].tolist())

    df = df.loc[df['Class'].isin(valid_class_list)]


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
    df['Weekly_Class_Hours'] = df['Duration_Hr'] * df['Days_Per_Week']


    ### This is a useful lambda example
    #df['Xlst_Max_Enrl'] = df['Xlst_Max_Enrl'].apply(lambda x: x if (x != '') else '0')
    ####


    df_reg = format_df_reg(df)
    df_xlist = merge_xlist(df)
    df_combined = aggregate(pd.concat([df_reg, df_xlist]))

    summary = df_combined.groupby('Optimal_Size').size()
    print(summary)

if __name__=='__main__':
    main()