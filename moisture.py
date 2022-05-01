import RPi.GPIO as GPIO
import time
from multiprocessing import Process
import Adafruit_ADS1x15
import math
'''
0.494 V = 9811 ADC value
Inverse relation : > 9811:dry, < 9811:moist 
'''

adc = Adafruit_ADS1x15.ADS1115()
gain = 1
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(18,GPIO.OUT)
# duty = 5/100
# freq=10000
# period=1/freq
moisture_ain0 = 0
moisture_ain1 = 1
moisture_ain2 = 2
moisture_ain3 = 3
gain = 1 #ignore this
value = 0
epoch = time.time()
def run_pump():
    while True:
        value0 = adc.read_adc(moisture_ain0, gain=gain)
        value1 = adc.read_adc(moisture_ain1, gain=gain)
        value2 = adc.read_adc(moisture_ain2, gain=gain)
        value3 = adc.read_adc(moisture_ain3, gain=gain)
        mean = (value1 +  value2 + value3)/3
        mean_01=(value2 +  value1)/2
        mean_03=(value2 +  value3)/2
        mean_13=(value1 +  value3)/2
        stddev = math.sqrt(((value2 - mean)**2 + (value1 - mean)**2 + (value3 - mean)**2)/ 3)
        print("", value1, value2, value3)
        print("Total Mean ", mean)
        print("Stddev %.2f" % stddev)
        print(f"Coefficient of variation = %.2f" % (stddev / mean * 100), " %")
        print("2&1 Mean ", mean_01)
        print("2&3 Mean ", mean_03)
        print("1&3 Mean ", mean_13)
        print("Current time: %d seconds" % (time.time() - epoch))
        time.sleep(1)
#         if value > 14811:
#             for _ in range(10000):
#                 GPIO.output(18,GPIO.HIGH)
#                 time.sleep(period*duty)
#                 GPIO.output(18,GPIO.LOW)
#                 time.sleep(period*(1-duty))
#             GPIO.output(18,GPIO.LOW)    
#         time.sleep(3)
# 
if __name__ == "__main__":
    run_pump()



