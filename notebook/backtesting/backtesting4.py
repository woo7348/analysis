import numpy as np # 넘파이 모듈 임포트
from pandas import DataFrame #

data = {'빗썸': [100, 100, 100],
        '코빗': [90, 110, 120]}

df = DataFrame(data)
df['최저가'] = np.where(df['빗썸'] < df['코빗'], '빗썸', '코빗') # np.where함수를 통해서
#고가 와 목표가를 비교할 수 있다.
df.to_excel("거래소.xlsx")