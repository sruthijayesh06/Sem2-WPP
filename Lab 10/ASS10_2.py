import pandas as pd

dt1=pd.Timestamp("2012-01-15")
print("a) ",dt1)

dt2=pd.Timestamp("2012-01-15 21:20:00")
print("b) ",dt2)

dt3=pd.Timestamp.now()
print("c) ",dt3)

dt4=dt3.normalize()
print("d) ",dt4)

dt5=