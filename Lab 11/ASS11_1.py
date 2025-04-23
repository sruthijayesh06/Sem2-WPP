import pandas as pd
from datetime import datetime, time

dt_object = pd.Timestamp('2012-01-15')
print("a) Date time object for Jan 15 2012:", dt_object)

specific_dt = pd.Timestamp('2023-01-01 21:20:00')  
print("b) Specific date and time of 9:20 pm:", specific_dt)

local_dt = pd.Timestamp.now()
print("c) Local date and time:", local_dt)

date_only = pd.to_datetime('2023-04-10').date()
print("d) A date without time:", date_only)

current_date = pd.Timestamp.today().date()
print("e) Current date:", current_date)

some_datetime = pd.Timestamp('2023-04-10 15:45:30')
time_only = some_datetime.time()
print("f) Time from a date time:", time_only)

current_local_time = datetime.now().time()
print("g) Current local time:", current_local_time)
