import pyupbit
from pandas import DataFrame


data = {'open': [100, 200], "high": [110, 210]}
df = DataFrame(data )
print(df)

btc = pyupbit.get_ohlcv("BTC")
print(btc)