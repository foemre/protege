import smbus
import time

address = 0x48
ain0 = 0x40
ain1 = 0x41
ain2 = 0x42
ain3 = 0x43

tempread = ain2

bus = smbus.SMBus(1)

while True:
	bus.write_byte(address, tempread)
	value = bus.read_byte(address)
	print(value)
	time.sleep(0.1)
