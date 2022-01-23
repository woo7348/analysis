import pybithumb #변동성 돌파 백 테스팅.
import numpy as np


def get_ror(k=0.5):
     df = pybithumb.get_ohlcv("BTC")
     df['range'] = (df['high'] - df['low']) * k
     df['target'] = df['open'] + df['range'].shift(1)

     fee = 0.0032
     df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,
                          1)

     ror = df['ror'].cumprod()[-2]
     return ror


for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k) # get_ror() 함수를 호출하여 입력된 k 값에 따른 수익률을 계산
    print("%.1f %f" % (k, ror)) # k 값과 수익률을 화면에 출력해줍니다.

# ror(rate of returns)를 계산하는 코드를 함수로 만들어줌.
#k값을 함수의 인자로 입력받는다.