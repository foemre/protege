import RPi.GPIO as GPIO
import time
from multiprocessing import Process
import Adafruit_ADS1x15
'''
0.494 V = 9811 ADC value
Inverse relation : > 9811:dry, < 9811:moist 
'''

adc = Adafruit_ADS1x15.ADS1115()
gain = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
duty = 5/100
freq=10000
period=1/freq
moisture_ain = 3
gain = 1 #ignore this
value = 0


def run_pump():
    while True:
        value = adc.read_adc(moisture_ain, gain=gain)
        print("ADC level:", value)
        if value > 14811:
            for _ in range(10000):
                GPIO.output(18,GPIO.HIGH)
                time.sleep(period*duty)
                GPIO.output(18,GPIO.LOW)
                time.sleep(period*(1-duty))
            GPIO.output(18,GPIO.LOW)    
        time.sleep(3)

if __name__ == "__main__":
    run_pump()



