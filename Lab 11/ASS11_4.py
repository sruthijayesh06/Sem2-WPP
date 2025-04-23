import pandas as pd
import numpy as np

df = pd.DataFrame({
    'John':  [True, False, True, False, True, True, False, True, False, True],
    'Judy':  [True, True, False, False, True, False, False, True, False, True]
})

df['party'] = df['John'] & df['Judy']

df['days_til_party'] = np.nan

party_days = df.index[df['party']].tolist()

for i in reversed(range(len(df))):
    future_parties = [day for day in party_days if day >= i]
    if future_parties:
        df.at[i, 'days_til_party'] = future_parties[0] - i
    else:
        df.at[i, 'days_til_party'] = np.nan 

df['days_til_party'] = df['days_til_party'].astype(int)

df = df.drop(columns='party')

print(df)
