import board
import time
import adafruit_bh1750
import RPi.GPIO as GPIO
import math
from threading import Thread
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)
duty = 1
freq=50
period = 1/freq
target_brightness = 500
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, freq)
pwm.start(0.01)
def sense():
    try:
        while(True):
            print("%.2f Lux" % sensor.lux)
            time.sleep(0.25)
    except:
        pass

def led_output():
    try:
        while(True):
            if(sensor.lux > 400):
                pwm.ChangeDutyCycle(0)
            else:
                pwm.ChangeDutyCycle((400-sensor.lux)/4)
                print((400-sensor.lux)/4)
                time.sleep(0.01)
    except KeyboardInterrupt:
        print("Interrupt")
        print(e)
    finally:
        pwm.ChangeDutyCycle(0)
        GPIO.cleanup()
        print("Cleanup")

if __name__ == "__main__":
    t1 = Thread(target=sense)
    t2 = Thread(target=led_output)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:
        pass