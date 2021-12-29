import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
gain = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

moisture_ain = 3
gain = 1 #ignore this

while True:
    value = adc.read_adc(moisture_ain, gain=gain)
    print("ADC level:", value)
    print("Better info:", int(value / 100))
    time.sleep(1)
