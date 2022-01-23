#목표가 계산까지 합친 코드
import time
import pybithumb
import datetime
def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("BTC")

while True:
    now = datetime.datetime.now()
    if mid < now < mid + datetime.timedelta(seconds=10):
        target_price = get_target_price("BTC")
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

    current_price = pybithumb.get_current_price("BTC")
    print(current_price)

    time.sleep(1)

#실행하게되면 현재가를 기준으로 목표가를 1초마다 계산해서 출력해준다.






