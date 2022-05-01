import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
gain = 1
def convertToVoltage(adcValue):
	return adcValue/65536 * 3.3

#TODO
#write phValue function
#write threaded version of this program: 100Hz sampling, 2Hz reporting

def main():
	cal_bias = 2.57 #Volt
	
	while True:
		value = adc.read_adc(3, gain=gain)
		voltage = convertToVoltage(value)
		phValue = 5.70 * voltage + cal_bias
		print("Voltage: %.3f V" % voltage)
		print("phValue: %.3f" % phValue)
		print("Value: %d \n" % value)
		time.sleep(0.5)

if __name__ == "__main__":
	main()