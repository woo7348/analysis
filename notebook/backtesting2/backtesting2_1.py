import pybithumb # 변동성돌파 + 상승장 전략에 대한 백테스팅
import numpy as np

df = pybithumb.get_ohlcv("BTC")

df['ma5'] = df['close'].rolling(window=5).mean().shift(1) #각 거래일에 대해 5일 이동평균 계산
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)
df['bull'] = df['open'] > df['ma5'] #거래일의 시가가 전일 종가까지 계산된 5일 이동평균보다
#크면 'bull'컬럼에 True를 저장 하고 그렇지 않으면 False를 저장.

fee = 0.0032
df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                     df['close'] / df['target'] - fee,
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD: ", df['dd'].max())
print("HPR: ", df['hpr'][-2])
df.to_excel("larry_ma.xlsx")
#변동성 돌파 + 상승장 투자 전략의 수익은 MDD, 기간 수익률은 HPR로 나온다.
