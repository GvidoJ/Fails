import smbus2
import bme280
import RPi.GPIO as GPIO
import time

port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.setup(21, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)

try:
    while True:
        button_state1 = GPIO.input(21)
        button_state2 = GPIO.input(20)
        button_state3 = GPIO.input(16)  
        data = bme280.samle(bus, address, calibration_params) 
        if button_state1 == GPIO.LOW:
            print('LED 1 on')
            GPIO.output(26,GPIO.HIGH)
            time.sleep(1)
            print ('Led off')
        if button_state2 == GPIO.LOW:
            print('LED 2 on')
            GPIO.output(19,GPIO.HIGH)
            time.sleep(1)
            print ('LED off')
        if button_state2 == GPIO.LOW:
            print('LED 3 on')
            GPIO.output(13,GPIO.HIGH)
            time.sleep(1)
            print('LED off')
        else:
            GPIO.output(26,GPIO.LOW)
            GPIO.output(19,GPIO.LOW)
            GPIO.output(13,GPIO.LOW)
except KeyboardInterrupt:
   GPIO.cleanup()
finally:
    GPIO.cleanup()