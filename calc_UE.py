import numpy as np
import pandas as pd

def readInData():
    df = pd.read_csv('emp-unemployment.csv', engine='python', encoding='utf-8', error_bad_lines=False)
    df = df.set_index('Area')
    df_t  = df.iloc[:,1:].T
    return df_t

def calculateAvgs(df):

    for column in df:
        print(column)
        df[f"{column}_SMA"] = df[column].rolling(window=3).mean()
    return df

def calcAges(df):
    df['Year Born'] = pd.to_numeric(df.index.to_series())- 17
    
    return df.iloc[2:]


if __name__ == "__main__":
    df = readInData()
    print(df)
    # print(df.iloc[:1])
    df_SMA = calculateAvgs(df)
    print(df_SMA.index)
    df_final = calcAges(df_SMA)

    print(df_final)