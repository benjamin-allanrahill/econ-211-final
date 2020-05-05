import numpy as np
import pandas as pd

def readInData():
    df = pd.read_csv('emp-unemployment.csv', engine='python', encoding='utf-8', error_bad_lines=False)
    df = df.set_index('Area')
    df_t = df.iloc[:, 1:].T
    # print(df_t.iloc[1])
    df_t.columns = map(str.lower, df_t.columns)
    return df_t

def calculateAvgs(df):

    for column in df:
        print(column)
        df[f"{column}_SMA"] = df[column].rolling(window=3).mean()
    return df

def calcYear(df):
    df['UEyear'] = pd.to_numeric(df.index.to_series())- 17
    
    return df.iloc[2:]

def calcAge(cps_df):
    cps_df = cps_df.replace({'under 1 year': 0})
    cps_df['yob'] = cps_df['year'] - pd.to_numeric(cps_df['age'])

    return cps_df

def ueRate(row, uedf):
    uerow = uedf.loc[uedf['UEyear'] == row['yob']]
    print(uerow[f"{row['statefip']}"].values)
    return uerow[f"{row['statefip']}"].values or None

def loadCPS():
    df = pd.read_csv('cut_cps_data.csv', engine='python', encoding='utf-8', error_bad_lines=False)
    return df
 



if __name__ == "__main__":
    df = readInData()
    # print(df)
    # print(df.iloc[:1])
    df_SMA = calculateAvgs(df)
    # print(df_SMA.index)

    cps_df = calcAge(loadCPS())
    df_final = calcYear(df_SMA)

    
    print(df_final.head())
    cps_df['ueRate'] = cps_df.apply(lambda person: ueRate(person, df_final), axis=1, result_type='expand')

    
    print(cps_df)