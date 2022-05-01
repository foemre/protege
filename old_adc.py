import time
import board

import adafruit_pcf8591.pcf8591 as PCF
from adafruit_pcf8591.analog_in import AnalogIn
from adafruit_pcf8591.analog_out import AnalogOut

############# AnalogOut & AnalogIn Example ##########################
#
# This example shows how to use the included AnalogIn and AnalogOut
# classes to set the internal DAC to output a voltage and then measure
# it with the first ADC channel.
#
# Wiring:
# Connect the DAC output to the first ADC channel, in addition to the
# normal power and I2C connections
#
#####################################################################
i2c = board.I2C()
pcf = PCF.PCF8591(i2c)

pcf_in_0 = AnalogIn(pcf, PCF.A0)
pcf_in_1 = AnalogIn(pcf, PCF.A1)

pcf_out = AnalogOut(pcf, PCF.OUT)

my_list = [0]*100
counter = 1
while True:
	
	pcf_out.value = 65535
	raw_value = pcf_in_0.value
	my_list.append(raw_value)
	my_list.pop(0)
	mean = sum(my_list)/len(my_list)
	variance = sum([((x - mean) ** 2) for x in my_list]) / len(my_list)
	res = variance ** 0.5
	if counter>100:	
		print("Pin 0: %0.2f" % (raw_value))
		print("Moving avg: %.2f" % mean)
		print("Stddev: %.2f" % res)
		print("Coeff of variance: %.3f %%" % (res*100/mean))
		print("")
		time.sleep(0.1)
	counter += 1
