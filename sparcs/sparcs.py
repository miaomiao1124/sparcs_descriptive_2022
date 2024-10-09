import pandas as pd
import time

start_time=time.time()
df=pd.read_csv('sparcs\sparcs_2022.csv')
end_time=time.time()
load_time=end_time-start_time
print(f"Time to load data:{load_time}seconds")
del(df)

start_time=time.time()
df_small_1000=pd.read_csv('sparcs\sparcs_2022.csv', nrows=1000)
end_time=time.time()
load_time=end_time-start_time
print(f"Time to load data:{load_time}seconds")
df_small_1000.to_csv('sparcs\sparcs_2022_small_1000.csv', index=False)

start_time=time.time()
df_small_100000=pd.read_csv('sparcs\sparcs_2022.csv', nrows=100000)
end_time=time.time()
load_time=end_time-start_time
print(f"Time to load data:{load_time}seconds")

df = df_small_100000
###
df.columns

## remove all white spaces, lower case, replace space with underscore
df.columns=df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(','').str.replace(')','').str.replace('-', '_')

df['hospital_county']