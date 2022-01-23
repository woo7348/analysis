#backtesting2는 목표가 컬럼을 추가해준 코드이다.
#목표가 컬럼은 시가 컬럼에 레인지 컬럼 데이터를 더해주면된다.
#이때 레인지 컬럼의 모든 데이터를 하나 밑으로 내린 후 더해주면 된다.

import pybithumb

df = pybithumb.get_ohlcv("BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df['range_shift1'] = df['range'].shift(1)
df['target'] = df['open'] + df['range'].shift(1)
df.to_excel("btc.xlsx")