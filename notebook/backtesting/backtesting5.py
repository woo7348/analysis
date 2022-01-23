import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)
ror = df['ror'].cumprod()[-2] #ror 컬럼에 대해 cumprod()를 호출하면 series객체가 리턴된다.
#리턴되는 series 객체의 끝에서 2번째 값을 ror변수가 바인딩한다.
print(ror)

df.to_excel("trade.xlsx")

#where함수를 이용해서 고가와 목표가를 비교.
#고가가 목표가보다 큰경우에는 매수 조건에 해당됨.
#매수가 된 경우 해당 거래일의 매도가는 당일 종가이고, 매수가는 목표가 이므로
#수익률은 df[‘close’]/df[‘target’] 이 된다.
