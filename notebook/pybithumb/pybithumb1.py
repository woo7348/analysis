import pybithumb

tickers = pybithumb.get_tickers()
print(tickers)

price = pybithumb.get_current_price("ETH") # 이더리움을 KRW로 나타낸값, 현재가
print(price)
