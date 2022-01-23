import pybithumb #빗썸에서도 구해보았다. pyupbit를 사용하다가 빗썸으로 변경

df = pybithumb.get_ohlcv("BTC")
yesterday = df.iloc[-2]  # 전일 데이터를 가져옴(-2) yesterday에 전일 데이터를 series객체로 바인딩

today_open = yesterday['close'] # close 인덱스를 사용해서 당일 시가 조회
yesterday_high = yesterday['high'] # high ..전일고가
yesterday_low = yesterday['low'] # low .. 전일 저가
target = today_open + (yesterday_high - yesterday_low) * 0.5 #변동성 돌파 전략의 목표가를 계산
print(target)

#목표가는 프로그램이 시작될때 + 매일자정마다 재계산 되어야한다.

# 목표가를 계산하는 부분을 함수로 정리
#def get_target_price(ticker):
#    df = pybithumb.get_ohlcv(ticker)
#    yesterday = df.iloc[-2]

#    today_open = yesterday['close']
#    yesterday_high = yesterday['high']
#    yesterday_low = yesterday['low']
#    target = today_open + (yesterday_high - yesterday_low) * 0.5
#    return target