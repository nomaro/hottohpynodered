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
        stove.set_power_level(1)
        print("FLAMME PUISSANCE 1")
        time.sleep(1)
        stove._getStoveIsOn()
        sys.exit()
