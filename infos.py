  GNU nano 3.2                                                                                                       infos.py

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
    time.sleep(2)
    print("_getStoveState: ", stove._getStoveState())
    print("get_action: ", stove.get_action())
    print("get_naction: ", stove.get_naction())
    print("_getStoveIsOn: ", stove._getStoveIsOn())
    print("_getEcoMode: ", stove._getEcoMode())
    print("_getSmokeTemperature: ", stove._getSmokeTemperature())
    print("_getSetPowerLevel: ", stove._getSetPowerLevel())
    print("_getSpeedFanSmoke: ", stove._getSpeedFanSmoke())
    print("_getSpeedFan1: ", stove._getSpeedFan1())
    print("_getSetSpeedFan1: ", stove._getSetSpeedFan1())
    print("_getSpeedFan2: ", stove._getSpeedFan2())
    print("_getSetSpeedFan2: ", stove._getSetSpeedFan2())
    sys.exit()

