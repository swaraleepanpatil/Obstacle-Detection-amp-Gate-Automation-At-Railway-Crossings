import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

l1r=36
l1y=38
l1g=40

"""for traffic light
l1r=19
l1y=21
l1g=23
"""

GPIO.setup(l1r,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(l1y,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(l1g,GPIO.OUT,initial=GPIO.HIGH)

try:
    while True:
        print("Glow all")
        GPIO.output(l1r,GPIO.HIGH)
        GPIO.output(l1y,GPIO.HIGH)
        GPIO.output(l1g,GPIO.HIGH)

        time.sleep(5)

        print("OFF all")
        GPIO.output(l1r,GPIO.LOW)
        GPIO.output(l1y,GPIO.LOW)
        GPIO.output(l1g,GPIO.LOW)

        time.sleep(5)
except KeyboardInterrupt:
    print("Closed by user")
    GPIO.cleanup()
