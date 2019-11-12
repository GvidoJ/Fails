import RPi.GPIO as GPIO
import time
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
        if button_state1 == GPIO.LOW:
            print('LED 1 on')
            GPIO.output(26,GPIO.HIGH)
            GPIO.output(19,GPIO.HIGH)
            GPIO.output(13,GPIO.HIGH)
            time.sleep(1)
    print ('Led off')
except:
    GPIO.cleanup()