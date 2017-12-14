# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 10:24:18 2017

"""

import pandas as pd
df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]

df.set_index(['STNAME','CTYNAME'], inplace=True)


import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})

x = df.apply(min_max, axis=1)
y = x.reset_index()

df['SUMLEV'] == df.SUMLEV


sum(pd.Series(range(10)) * pd.Series(range(10,20)))
