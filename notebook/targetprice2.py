#자정에 목표가를 갱신시키고자한다.
import time
import datetime

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

while True: #  while문 안에서 반복해서 현재 시각을 얻어옴
    now = datetime.datetime.now()
    if now == mid: # datetime의 비교 연산을 사용해서 얻어온 현재 시각이 자정인지 체크.
        print("정각입니다")
        now = datetime.datetime.now()
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1) # 자정이라면 다음날의 자정 시각을 계산.

        print(now, "vs", mid)
        time.sleep(1) # 1초에 한번씩 현재시각과 다음날 자정의 시각이 출력.