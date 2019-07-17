import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

#for IR Sensor1
#ir=22
ir=40

GPIO.setup(ir,GPIO.IN)

try:
    while True:
        i=GPIO.input(ir)
        if i==1:
            print("Train not arrived")
            time.sleep(1)
        elif i==0:
            print("Train arrived")
            time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()
