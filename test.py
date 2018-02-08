import pandas as pd
import numpy as np

# i = 1
# while i < 11:
#     df_0 = pd.DataFrame(np.arange(i, i+4), columns=['a'])
#     i = i+1
# print(df_0)

# print(np.arange(1, 5))


user_id = 1
lat_average = 22324
lon_average = 5645645
record_time = 2018
df_all = pd.DataFrame(columns=['user_id', 'lat', 'lon', 'record_time'])
dict_singleaggregateddata = {'user_id': [user_id], 'lat': [lat_average], 'lon': [lon_average], 'record_time': [record_time]}
df_singleaggregateddate = pd.DataFrame({'user_id': [user_id], 'lat': [lat_average], 'lon': [lon_average],
                                        'record_time': [record_time]},
                                       columns=['user_id', 'lat', 'lon', 'record_time'])
df_all = df_all.append(df_singleaggregateddate)


# print(df_all)

# #函数的参数
# ll = [1, 2, 3]
# print(*ll)
# print(ll)
#
# #keyword operand
# def person(name, age, **kw):
#     print('name:' , name, 'age: ', age, 'other: ', kw)
#
# person('Bob', 35, city='Beijing') #不能是person('Bob', 35, 'Beijing')
#
# #可变参数：计算传入参数的乘积
# def product(*numbers):
#     result = 1
#     for n in numbers:
#         result = result * n
#     print(result)
#
# product(5, 6, 7, 9)

# # slice
# def trim(s):
#     return s[1 : len(s)-1]
#
# str = 'helloworld'
# print(trim(str))

# # iteration
# def findMinAndMax(L):
#     min = L[0]
#     max = L[0]
#     for item in L:
#         if item < min:
#             min = item
#         elif item > max:
#             max = item
#     return min, max
#
# L = [5, 4, 3, 2, 1, 0, -9, 99]
# print(findMinAndMax(L))
#
# # ################  list comprehensions
# ll = [x * x for x in range(1, 11)]
# print(findMinAndMax(ll))

# li = range(1, 11)
# print(li)
# ll = list(range(1, 11))
# print(ll)


# import os # 导入os模块，模块的概念后面讲到
# dir = [d for d in os.listdir('.')]
# print(dir)

# L = ['Apple', 'IBM', 18, 'HellO', 'WoRld']
# l = [s.lower() for s in L if isinstance(s, str) is True]
# print(l)

# 杨辉三角: failed....
# def triangles():
#     n = 0
#     lt = []
#     lt.append([1])
#     lt.append([1,1])
#     while True:
#         while lt[n] is not None:
#             yield lt[n], n
#             n = n + 1
#
#             ll = [1]
#             i = 1
#             while i <= n:
#                 if i==n:
#                     ll.append(1)
#                     i = i + 1
#                 else:
#                     j= lt[n-1][i-1] + lt[n-1][i]
#                     ll.append(j)
#                     i = i + 1
#             lt.append(ll)
#
#
# tri = triangles()
# print(next(tri))
# print(next(tri))
# print(next(tri))
# print(next(tri))


