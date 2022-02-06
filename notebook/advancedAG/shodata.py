import pybithumb
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Coin price in $')
pybithumb['close'].plot(ax=ax1, color='r', lw=2.)