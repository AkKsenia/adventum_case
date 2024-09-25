import pandas as pd
from scipy.stats import kruskal


df_time = pd.read_csv('data1.csv')
df_day = pd.read_csv('data2.csv')
df_interval = pd.read_csv('data3.csv')


time_of_day = df_time['time_of_day']
avg_likes_time = df_time['avg_likes_amount']

day_of_week = df_day['day_of_week']
avg_likes_day = df_day['avg_likes_amount']

date_diff = df_interval['date_diff']
avg_likes_interval = df_interval['avg_likes_amount']

# посчитаем коэффициент корреляции Пирсона

time_of_day_mapping = {'утро': 0, 'день': 1, 'вечер': 2, 'ночь': 3}
day_of_week_mapping = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}

df_time['time_of_day_num'] = df_time['time_of_day'].map(time_of_day_mapping)
df_day['day_of_week_num'] = df_day['day_of_week'].map(day_of_week_mapping)

corr_time = df_time['time_of_day_num'].corr(df_time['avg_likes_amount'])
corr_day = df_day['day_of_week_num'].corr(df_day['avg_likes_amount'])
corr_interval = df_interval['date_diff'].corr(df_interval['avg_likes_amount'])

print("Correlation coefficient (time of day):", corr_time)
print("Correlation coefficient (day of week):", corr_day)
print("Correlation coefficient (time interval):", corr_interval)
print()


# тест Краскела — Уоллиса

h_stat_time, p_val_time = kruskal(*[df_time[df_time['time_of_day'] == i]['avg_likes_amount'] for i in df_time['time_of_day'].unique()])
h_stat_day, p_val_day = kruskal(*[df_day[df_day['day_of_week'] == i]['avg_likes_amount'] for i in df_day['day_of_week'].unique()])

print("H-statistic (time of day):", h_stat_time)
print("p-value (time of day):", p_val_time)
print("H-statistic (day of week):", h_stat_day)
print("p-value (day of week):", p_val_day)
