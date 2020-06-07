# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 01:00:55 2020

@author: wang
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
MONTH_DAY = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31,30, 31]

df = pd.read_csv('train_金泉两河.csv')  
del df['C_PM10_24H_MV']
del df['C_O3_8H_MV']
del df['I_O3_8H_MV']
del df['C_PM25_24H_MV']
del df['SOURCE_']
del df['LEVEL_']
del df['CATEGORY_']
del df['STATE_']
del df['COLOR_']

del df['UPDATE_TIME_']
del df['PRIMARY_POLLUTANTS_']
df['datetime'] = pd.to_datetime(df['DATA_TIME_']) #解析时间
del df['DATA_TIME_']#时间就不再需要了

df['HOUR_'] = df['datetime'].apply(lambda x: x.strftime('%h'))#解析小时
df['WEEK_LATER'] = (df['datetime'] + datetime.timedelta(days=7)).dt.strftime('%Y-%m-%d %H:00')


# plt.plot(df['HOUR_'])

del df['DATA_TIME_']


df['AQI_'].dropna() #删除没有AQI的数据
df.to_csv('csv1.csv')

dft = df[df['DATE_'] <= 30] #筛选出日期为I的
df_PM25 = dft['AQI_']
df_DATE = dft['DATE_']
df_HOUR = dft['HOUR_']
plt.plot(df_HOUR + (df_DATE-1) * 24 , df_PM25, marker='o')
plt.show()

dft = df[(df['DATE_']  ==1) & (df['AQI_' ] > 20)] #筛选出日期为I的

for i in range(1,5):
    dft = df[df['DATE_'] == i] #筛选出日期为I的
    df_PM25 = dft['AQI_']
    df_HOUR = dft['HOUR_']
    plt.plot(df_HOUR, df_PM25)
    plt.show()


