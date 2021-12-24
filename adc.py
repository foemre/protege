import time
import Adafruit_ADS1x15

'''
J5 – Connects LDR to channel 0 (AIN0)
J4 – Connects thermistor to channel 1 (AIN1)
J6 – Connects the potentiometer to channel 3 (AIN3)
'''

adc = Adafruit_ADS1x15.ADS1115()
channel = 3
gain = 1

while True:
	value = adc.read_adc(channel, gain=gain)
	print(value)
	time.sleep(0.1)
