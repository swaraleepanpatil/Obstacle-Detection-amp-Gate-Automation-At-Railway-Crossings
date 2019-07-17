#Libraries
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

"""
Orange -> GPIO (right 5 pin)
Red -> Power
Brown -> GND
"""

GPIO.setup(8,GPIO.OUT)#12
p1=GPIO.PWM(8,50)
p1.start(2.5)

GPIO.setup(10,GPIO.OUT)#12
p2=GPIO.PWM(10,50)
p2.start(2.5)

try:
    while True:
        i=GPIO.input(10)
        j=GPIO.input(10)
        if i==1 or j==1:
            print("close")
            p1.ChangeDutyCycle(6.5)#(2.5)
            p2.ChangeDutyCycle(6.5)#(2.5)
            time.sleep(1)
        elif i==0 or j==0:
            print("open")
            p1.ChangeDutyCycle(10.5)
            p2.ChangeDutyCycle(10.5)#(2.5)
            time.sleep(1)
            #p.ChangeDutyCycle(2.5)
except KeyboardInterrupt:
    GPIO.cleanup()
