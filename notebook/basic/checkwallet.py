import pyupbit

access_key = "7lY40pdbWyvT8x3CYtTPl9lZIRsAKW1QPBwwB88I" # 내지갑...돈없음.잔고조회만 가능한 api 키
secret_key = "xv0MYBxanI1l6cdqZOOxHkRrp38UImHoLdTZdNWz"

upbit = pyupbit.Upbit(access_key ,secret_key)
print(upbit.get_balances())