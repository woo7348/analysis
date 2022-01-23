#목표가 계산까지 합친 코드 + 매도기능 + 매수 + 함수정리
import time
import pybithumb
import datetime
def sell_crypto_currency(ticker):
    unit = pybithumb.get_balance(ticker)[0]
    pybithumb.sell_market_order(ticker, unit)

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
        now = datetime.datetime.now()
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
        sell_crypto_currency("BTC")

    current_price = pybithumb.get_current_price("BTC")
    if current_price > target_price:  #현재가가 목표가 보다 클때 if문 실행
        krw = pybithumb.get_balance("BTC")[2] #잔고조회 api를 사용해서 보유중인 원화를 계산
        orderbook = pybithumb.get_orderbook("BTC") # 호가창을 조회해서 최우선 호가를 조회
        sell_price = orderbook['asks'][0]['price']
        unit = krw / float(sell_price) # 원화 잔고를 최우선 매도가로 나눠서 구매가능한 수량을계산
        pybithumb.buy_market_order("BTC", unit) # 시장가 주문으로 비트코인 매수

    time.sleep(1)

#1) 보유한 비트코인이 있다면(당일 매수 조건에 따라 매수가 됐다면) 해당 비트코인을 시장가로 매매
#2) 전일 시가, 고가, 저가, 종가 기준으로 래리 윌리엄스의 변동성 돌파 전략 기반 목표가 재계산
#3) 해당 일 기준으로 다음 날의 00:00:00 초 시간 계산


#매수 + 매도 함수정리

#while True:
#     now = datetime.datetime.now()
#     if mid < now < mid + datetime.timedelta(seconds=10):
#         target_price = get_target_price(“BTC”)
#         mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
#         sell_crypto_currency("BTC")
#
#     current_price = pybithumb.get_current_price("BTC")
#     if current_price > target_price:
#         buy_crypto_currency("BTC")
#
#     time.sleep(1)





