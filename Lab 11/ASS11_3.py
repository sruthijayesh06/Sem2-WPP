import pandas as pd

asking_prices = pd.Series([25000, 18000, 22000, 19500, 21000])
fair_prices   = pd.Series([26000, 17500, 23000, 20000, 21500])

good_deals = asking_prices < fair_prices

good_deal_indices = good_deals[good_deals].index.tolist()

print("Good deal indices:", good_deal_indices)
