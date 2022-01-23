#DATAFRAME 객체를 엑셀로 저장하기

import pybithumb

df = pybithumb.get_ohlcv("BTC")
df.to_excel("btc.xlsx")