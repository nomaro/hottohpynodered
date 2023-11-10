# importing module
import sys
import parse
from parse import *

# appending a path
sys.path.append('src')
from hottohpy import Hottoh
import time

for arg in sys.argv:
        flam = ''.join(r[0] for r in findall("flame:{}/", arg))
        fan1 = ''.join(r[0] for r in findall("fan1:{}/", arg))
        fan2 = ''.join(r[0] for r in findall("fan2:{}/", arg))
        mode = ''.join(r[0] for r in findall("mode:{}/", arg))

stove = Hottoh('192.168.0.11' ,5001, "lib")

stove.connect()

#print(flam, fan1, fan2, mode)
time.sleep(1)
stove.set_power_level(flam)
print("Flamme : ", flam)
time.sleep(1)
stove.set_speed_fan_1(fan1)
print("Fan1 : ", fan1)
time.sleep(1)
stove.set_speed_fan_2(fan2)
print("Fan2 : ", fan2)
time.sleep(1)
if mode == "eco":
        stove.set_on()
        time.sleep(1)
        stove.set_eco_mode_on()
        print("Mode :", mode)
elif mode == "man":
        stove.set_on()
        time.sleep(1)
        stove.set_eco_mode_off()
        print("Mode :", mode)
elif mode == "off":
        stove.set_off()
        time.sleep(1)
        stove.set_eco_mode_off()
        print("Mode :", mode)
else:
        print("Aucune action demandé")
        sys.exit()
time.sleep(1)
stove._getStoveIsOn()
print("Tout est OK")
sys.exit()



