# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 12:42:50 2017
"""

import pandas as pd

#import os
#os.getcwd()


census_df = pd.read_csv('census.csv')
census_df.head()


# Q5

# display column names
list(census_df)
# or 
census_df.columns#.values

columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'CENSUS2010POP']

#df.loc[<mask or index label values>, <optional column>] = < new scalar value or array like>


cty_level = census_df[census_df['SUMLEV']==50][columns_to_keep]
cty_level['STNAME'].value_counts().idxmax()

# Q6

top3_cty_per_st = cty_level.groupby('STNAME')['CENSUS2010POP'].nlargest(3)
top3_cty_per_st.groupby(level ='STNAME').sum().nlargest(3).index.values.tolist()

# не моё
cty_level.groupby('STNAME')['CENSUS2010POP'].apply(
        lambda x: x.nlargest(3).sum()).nlargest(3).index.values.tolist()


# Q7

value_columns = ['POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']

columns_to_keep = ['STNAME','CTYNAME'] + value_columns
cty_level = census_df.loc[census_df['SUMLEV']==50, columns_to_keep]

#cty_level['Min'] =  cty_level.loc[:, value_columns].min(axis=1)
Min = cty_level.loc[:, value_columns].min(axis=1)
Max = cty_level.loc[:, value_columns].max(axis=1)
id_max = (Max - Min).idxmax()

cty_level.loc[id_max]['CTYNAME']

# Q8

columns_to_keep = ['REGION', 'STNAME', 'CTYNAME',
       'POPESTIMATE2014', 'POPESTIMATE2015']

df = census_df.loc[census_df['SUMLEV']==50, columns_to_keep]
df = df.loc[df['REGION'] <= 2]

pattern = '^Washington'

df = df[df['CTYNAME'].str.match(pattern)]

pop14 = df['POPESTIMATE2014']
pop15 = df['POPESTIMATE2015']

df = df[pop15 > pop14].loc[:, ['STNAME', 'CTYNAME']]






