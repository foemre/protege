import board
import time
import adafruit_bh1750
import RPi.GPIO as GPIO
import math
from threading import Thread
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)
duty = 1
freq=1000
period = 1/freq
target_brightness = 500
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, freq)
pwm.start(0)
my_list = [0]*20
mean=0

def sense():
    try:
        while(True):
            raw_value = sensor.lux
            my_list.append(raw_value)
            my_list.pop(0)
            mean = sum(my_list)/len(my_list)
            variance = sum([((x - mean) ** 2) for x in my_list]) / len(my_list)
            res = variance ** 0.5
            if True:
                print("Value: %0.2f Lux" % (raw_value))
                print("Moving avg: %.2f" % mean)
                print("Stddev: %.2f" % res)
                print("Coeff of variance: %.3f %%" % (res*100/mean))
                print("")
                time.sleep(0.05)
    except:
        pass

def led_output():
    try:
        while(True):
            if(mean > 400):
                pwm.ChangeDutyCycle(0)
            else:
                pwm.ChangeDutyCycle((400-sensor.lux) % 100 /4)
#                 print((400-sensor.lux)/4)
            time.sleep(0.1)
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
