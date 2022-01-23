#변동성 돌파 전략.
#1) 가격 변동폭 계산: 투자하려는 가상화폐의 전일 고가(high)에서 전일 저가(low)를 빼서 가상화폐의 가격 변동폭을 구합니다.
#2) 매수 기준: 당일 시간에서 (변동폭 * 0.5) 이상 상승하면 해당 가격에 바로 매수합니다.
#3) 매도 기준: 당일 종가에 매도합니다.

import pyupbit
import time
while True:
#    price = pyupbit.get_current_price("KRW-BTC") #BTC를 KRW로 나타냄
#    print(price)    #얻어온 현재가 출력.
#    time.sleep(0.2)  #숫자 = (t)초당 조회.

    df = pyupbit.get_ohlcv("KRW-BTC")
    print(df.tail(1))