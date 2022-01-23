import pyupbit
print(pyupbit.Upbit)

tickers = pyupbit.get_tickers() # 세계시장 타겟
print(tickers)

tickers = pyupbit.get_tickers(fiat="KRW") # 한국시장 한정
print(tickers)

price = pyupbit.get_current_price("KRW-ETH") # 이더리움을 KRW로 나타낸값, 현재가
print(price)

