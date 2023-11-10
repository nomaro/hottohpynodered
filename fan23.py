# importing module
import sys
  
# appending a path
sys.path.append('src')
from hottohpy import Hottoh
import time

stove = Hottoh('192.168.0.11' ,5001, "lib")

stove.connect()

attempt = 1

while True:
        time.sleep(1)
        stove.set_speed_fan_2(3)
        print("FAN 2 PUISSANCE 3")
        time.sleep(1)
        stove._getStoveIsOn()
        sys.exit()

