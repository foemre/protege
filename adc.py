import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
channel = 3
gain = 1

while True:
	value = adc.read_adc(0, gain=gain)
	print("ADC0temp: ",value)
	value = adc.read_adc(3, gain=gain)
	print("ADC3soil: ",value)
	print()
	time.sleep(0.5)
