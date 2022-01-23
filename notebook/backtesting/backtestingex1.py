import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("BTC")
df = df['2018']