#목표가 계산까지 합친 코드 + 매수기능
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
    if current_price > target_price:  #현재가가 목표가 보다 클때 if문 실행
        krw = pybithumb.get_balance("BTC")[2] #잔고조회 api를 사용해서 보유중인 원화를 계산
        orderbook = pybithumb.get_orderbook("BTC") # 호가창을 조회해서 최우선 호가를 조회
        sell_price = orderbook['asks'][0]['price']
        unit = krw / float(sell_price) # 원화 잔고를 최우선 매도가로 나눠서 구매가능한 수량을계산
        pybithumb.buy_market_order("BTC", unit) # 시장가 주문으로 비트코인 매수

    time.sleep(1)

#26~31까지 함수로 정리.
# def buy_crypto_currency(ticker):
#    krw = bithumb.get_balance(ticker)[2]
#    orderbook = pybithumb.get_orderbook(ticker)
#    sell_price = orderbook['asks'][0]['price']
#    unit = krw/float(sell_price)
#   bithumb.buy_market_order(ticker, unit)






