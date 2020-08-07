import pandas as pd
import numpy as np
import os

def load_clean_fight_songs():
    '''
    runs sequentially:
        load_fight_songs() 
            - loads fight_songs.csv
        
        df = turn_value_null(df, 'Unknown') 
            - turns values "Unknown" to np.nan
        
        df = drop_nulls(df)
            - drops null rows from df
            
        df['year'] = turn_column_float(df['year'])
            - turns 'year' column to float type
            
    result:
        fight_songs.csv loaded and cleaned
    '''

    df = load_fight_songs()
    df = turn_value_null(df, 'Unknown')
    df = drop_nulls(df)
    df['year'] = turn_column_int(df['year'])

    return df


def turn_value_null(frame, value):
    '''
    data cleaning: turn argument value to null
    
    input: 
        frame: dataframe
        value_to_nan: specific value to turn to np.nan
        
    output: frame w/ all values of value_to_nan replaced w/ np.nan
    '''
    frame = frame.replace(value, np.nan)
    return frame


def drop_nulls(frame):
    '''
    data cleaning: drop rows w/ np.nan anywhere in frame
    
    input: dataframe 
    output: dataframe w/ rows w/ np.nan dropped
    '''

    frame = frame.dropna(axis=0, how="any")

    return frame


def turn_column_int(column):
    '''
    data cleaning: turn column to float type
    
    input: column from dataframe
    output: column as float type
    '''
    column = column.astype(int)
    return column


def load_fight_songs():
    '''
    loads in fight_songs.csv from the data folder using pd.read_csv
    
    outputs: dataframe of fight_songs.csv
    '''

    data_path = os.path.join(os.pardir, os.pardir, "data", "fight_songs.csv")
    df = pd.read_csv(data_path)

    return df
