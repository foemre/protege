import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
channel = 3
gain = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

tempread = 3
gain = 1 #ignore this

while True:
		value = adc.read_adc(tempread, gain=gain)
		temp = 0.0579*value-1294.2 # calibrated, fitted to this line
		str_temp = "Temperature: {temp:.2f} C\nADC Value: {value}".format(temp=temp, value=value)
		print(str_temp)
		if value < 25: #room temp
				GPIO.output(18,GPIO.HIGH)
		else:
				GPIO.output(18,GPIO.LOW)
		time.sleep(0.2)
