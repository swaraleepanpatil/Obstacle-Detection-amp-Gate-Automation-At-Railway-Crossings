#Libraries
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(8,GPIO.OUT)#12
p=GPIO.PWM(8,50)
p.start(2.5)

try:
    while True:
        i=GPIO.input(8)
        if i==1:
            print("close")
            p.ChangeDutyCycle(5)#(2.5)
            time.sleep(1)
        elif i==0:
            print("open")
            p.ChangeDutyCycle(10.5)
            time.sleep(1)
            #p.ChangeDutyCycle(2.5)
except KeyboardInterrupt:
    GPIO.cleanup()
