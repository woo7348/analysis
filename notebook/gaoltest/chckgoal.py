import ccxt #목표가 계산하기
import time
import datetime
import pandas as pd

with open("pybithumb/bithumbkey.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret  = lines[1].strip()

binance = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

symbol = "BTC/USDT"

# volatility breakout
btc = binance.fetch_ohlcv(
    symbol=symbol,
    timeframe='1d',
    since=None,
    limit=10)

df = pd.DataFrame(
    data=btc,
    columns=['datetime', 'open', 'high', 'low', 'close', 'volume']
)
df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
df.set_index('datetime', inplace=True)

yesterday = df.iloc[-2]
today = df.iloc[-1]
target = today['open'] + (yesterday['high'] - yesterday['low']) * 0.5
print(target)