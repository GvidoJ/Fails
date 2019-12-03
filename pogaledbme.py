#Visu importē un setupo pinus
import smbus2
import bme280

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

GPIO.setup(21, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)

#Nosaka portu addressi busu un calibration_paramus
port = 1
address = 0x76
bus = smbus2.SMBus(port)
claibration_params = bme280.load_calibration_params(bus, address)

#Nosaka pogas tagadnējo stadiju un nosaka kad nospiežot 1. poga uzrāda laiku, iededz 1 LED uz 0.4 s, 2. poga uzrāda spiedienu, iededz 2 LED uz o.4 s, 3. poga uzrāda temperatūru, iededz 3 LED uz 0.4 s.
try:
    while True:
        button_state1 = GPIO.input(21)
        button_state2 = GPIO.input(20)
        button_state3 = GPIO.input(16)
        data = bme280.sample(bus, address, claibration_params)
        if button_state1 == GPIO.LOW:
            GPIO.output(26,GPIO.HIGH)
            print(data.timestamp)
            time.sleep(0.4)
        if button_state2 == GPIO.LOW:
            GPIO.output(19,GPIO.HIGH)
            print(data.pressure)
            time.sleep(0.4)
        if button_state3 == GPIO.LOW:
            GPIO.output(13,GPIO.HIGH)
            print(data.temperature)
            time.sleep(0.4)
        else:
            GPIO.output(26,GPIO.LOW)
            GPIO.output(19,GPIO.LOW)
            GPIO.output(13,GPIO.LOW)
except KeyboardInterrupt:
   GPIO.cleanup()
finally:
    GPIO.cleanup()