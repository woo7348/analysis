#트레이딩 전략의 주요부분은 트레이딩 시점을 결정하는 것이다. 주문 전송을 발동시키는 이벤트를 시그널 이라한다,
#DATAFRAME 객체를 엑셀로 저장하기
import pandas as pd
import numpy as np
import pybithumb

df = pybithumb.get_ohlcv("BTC")
print(df.tail(10)) #최근 10일자 BTC데이터를 출력.
df = pybithumb.get_ohlcv("BTC")
#df.to_excel("btc.xlsx") BTC데이터를 엑셀로저장.

#coin_data_signal = pd.Dataframe(index=pybithumb.index) # 코인 데이터 프레임을 생성
#coin_data_signal['price'] = pybithumb['close'] #데이터 프레임 생성후 시그널 구축하는데 사용할
#데이터를 복사.

#coin_data_signal['daily_difference'] = coin_data_signal['price'].diff()
#print(coin_data_signal.head())

df = pybithumb.get_ohlcv("BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)
ror = df['ror'].cumprod()[-2] #ror 컬럼에 대해 cumprod()를 호출하면 series객체가 리턴된다.
#리턴되는 series 객체의 끝에서 2번째 값을 ror변수가 바인딩한다.
print(ror)