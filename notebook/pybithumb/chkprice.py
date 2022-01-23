import pybithumb # 주기적으로 현재가 얻어오기.
import time

while True:
    price = pybithumb.get_current_price("BTC")
    print(price)
    time.sleep(0.2)