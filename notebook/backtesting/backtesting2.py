#레인지 계산. 레인지란 전일고가에서 전일 저가를 뺀 값.
#DATAFRAME은 for문을 사용하지 않고 여러 행에 동일한 연산을 적용할 수 있다.
# 아래의 코드는 고가에서 저가를 뺀 후 여기에 0.5를 곱한 값을 'range' column에추가
import pybithumb

df = pybithumb.get_ohlcv("BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df.to_excel("btc.xlsx")

