import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
duty = 5/100
freq=10000
period=1/freq
while True:
    GPIO.output(18,GPIO.HIGH)
    time.sleep(period*duty)
    GPIO.output(18,GPIO.LOW)
    time.sleep(period*(1-duty))
