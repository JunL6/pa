
import pandas as pd
import numpy as np
import datetime
#import pandas.io.data
from pandas_datareader import data
import geoplotlib
import pyglet



# start = datetime.datetime(2010, 1, 1)
# end = datetime.datetime(2015, 8, 22)
#
# df = data.DataReader("XOM", "google", start, end)
#
#
# print(df.count())

web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors':[43, 53, 34, 45, 64, 34],
             'Bounce_Rate':[65, 72, 62, 64, 54, 66]}

df = pd.DataFrame(web_stats)
# print(type(df['Day'][1]))
df.drop([0], inplace=True)
# print(df)
df1 = df.head(1).index.values
i = df.head(1).index.values[0]
# i = df1[0]
print(i)

####
# print(df['Day'][0])
# i = 0
# print(df.iloc[i])
# df_a = pd.DataFrame(df.iloc[i])
####
# print(df[0:1])

###
# record = df[0: 1]
# print(record['Day'])

###
# print(df[i: i+1])
# print('len: ', len(df))

# #遍历dataframe
# while i < len(df):
#     print(df[i: i+1])
#     i = i+1

# print(df.iloc[-1:])
# print(df.iat[-1, -1])
# print(df.loc[5, ['Day']])

# while df[i] is not None:
#     print(df[i])
#     i = i + 1

# list_csdn = [[1, 2, 3], [4, 5, 6]]
# df_csdn = pd.DataFrame(list_csdn, index=['row1', 'row2'], columns=['c1', 'c2', 'c3'])
# # print(df_csdn)

# dates = pd.date_range('20141001', periods=6)
# df_random = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('abcd'))
#
# list_gps = [(793, 'a', 2014), (933, 'b', 2015), (942, 'c', 2016), (943, 'd', 2017)]
# df_gps = pd.DataFrame(list_gps)
# print(df_gps)
# print(df_gps.shape)

# #测试geoplotlib显示2个坐标点
# thedata = pd.DataFrame([[52.124569, -106.633258], [52.132523, -106.638236]], columns=['lat', 'lon'])
# geoplotlib.dot(thedata)
# geoplotlib.show()

#测试dataframe构造传入一个 一维list
    #结果：不行，会报错。得传入二维list
# list_1d = (1, 2, 3)
# df_1d = pd.DataFrame(list_1d)

#测试先构造空的dataframe，然后再添加数据
    #在函数内使用global variable也要先声明: global variblename
# df_empty = pd.DataFrame()
# list_testempty = [(1, 2, 3), (2, 4, 6)]
#
# def try_emptydf():
#     global df_empty
#     df_empty = df_empty.append(list_testempty)
#     print(df_empty)
#
# try_emptydf()

# COUNT=1
#
# def func():
#     temp = COUNT + 1
#     print('temp: ', temp)
#     print('COUNT: ', COUNT)
#
# func()
#
# #测试关于time的方法
# import datetime
# import time
# t1 = time.time()
# t2 = datetime.now()
# # delta = t2 - t1
# print('t1: ', t1)
# print('t2: ', t2)


#???
# 怎么删除dataframe的第一行后，再继续删除剩下的第一行