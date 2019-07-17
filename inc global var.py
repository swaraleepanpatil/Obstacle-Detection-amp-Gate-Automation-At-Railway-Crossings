"""count=0

def inc():
    global count
    count=count+1
    print("inside function count=",count)
    
while True:
    inc()
    print("outside function count=",count)

#print("outside function count=",count)
"""
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

l1r=36
l1y=38
l1g=40

GPIO.setup(l1r,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(l1y,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(l1g,GPIO.OUT,initial=GPIO.HIGH)


#count=0
cntr=0

def inc():
    global cntr
    cntr=cntr+1
    print("inside function count=",cntr)

try:    
    while True:
        inc()
        print("outside function count=",cntr)
        if cntr==450:
            print("\n\t yellow")
            GPIO.output(l1g,GPIO.LOW)
            GPIO.output(l1y,GPIO.HIGH)
        elif cntr==600:
            print("\n\t red")
            GPIO.output(l1y,GPIO.LOW)
            GPIO.output(l1r,GPIO.HIGH)
except KeyboardInterrupt:
    GPIO.cleanup()
#print("outside function count=",count)
