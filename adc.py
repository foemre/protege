import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
gain = 1
def convertToVoltage(adcValue):
	return adcValue/65536 * 3.3

def main():
	while True:
		value = adc.read_adc(3, gain=gain)
		voltage = convertToVoltage(value)
		print("Voltage: %.3f V\n" % voltage)
		print("Value: %d" % value)
		time.sleep(0.5)

if __name__ == "__main__":
	main()