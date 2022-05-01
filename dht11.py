import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
channel = 0
gain = 1
tempread = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 25
fan_pin = 23
fogger_pin = 24
temp_pin = 20

GPIO.setup(temp_pin,GPIO.OUT)
GPIO.setup(fogger_pin,GPIO.OUT)
GPIO.setup(fan_pin,GPIO.OUT)
 
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    value = adc.read_adc(tempread, gain=gain)
    temp = 0.0579*value-1294.2 # calibrated, fitted to this line
    str_temp = "Temperature: {temp:.2f} C\nADC Value: {value}".format(temp=temp, value=value)
    print(str_temp)
    
    if temp < 25: #room temp
        print(GPIO.output(temp_pin,GPIO.HIGH))
        print("HeaterON")
    else:
        print(GPIO.output(temp_pin,GPIO.LOW))
        print("HeaterOFF")
    time.sleep(0.2)
   
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        if(humidity < 65):
            GPIO.output(fogger_pin,GPIO.HIGH)
        else:
            GPIO.output(fogger_pin,GPIO.LOW)
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(1);
