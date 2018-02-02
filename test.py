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


print(df_all)
