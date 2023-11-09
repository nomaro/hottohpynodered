# importing module
import sys
  
# appending a path
sys.path.append('src')
from hottohpy import Hottoh
import time

stove = Hottoh('192.168.0.11' ,5001, "lib")

stove.connect()

attempt = 1
time.sleep(2)
stove.set_eco_mode_on()
print("MODE ECO ON")
sys.exit()

