import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")  #시가(open),고가(high),저가(low), 종가(close), 거래량(volume)
print(df)

df = pyupbit.get_ohlcv("KRW-BTC", interval="minute1") # 분봉
print(df)

df = pyupbit.get_ohlcv("KRW-BTC", count=5) # 5일간의 데이터만 조회
print(df)
