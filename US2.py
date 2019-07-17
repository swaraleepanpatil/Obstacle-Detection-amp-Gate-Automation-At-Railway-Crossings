#Final

#Connect ultrasonic ensor to rasp pi directly
#Libraries
#importing the threading module 
import threading
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
#set GPIO Pins
#VCC breadboard + rasp pi right pin2 ie pin for 5v (BOARD 4)
#GND breadboard + rasp pi right pin3 (BOARD 6)
GPIO_TRIGGER1 = 16 #right pin8
GPIO_ECHO1 = 18 #right pin 9

#VCC multiple male-feamale wires + one female-female wire + rasp pi right pin1 5v (BOARD 2)
#GND multiple male-feamale wires + one female-female wire + rasp pi left pin5 GND (BOARD 9)
GPIO_TRIGGER2 = 11
GPIO_ECHO2 = 15

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
'''
def distance1():
    print("distance() started")
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER1, True)
    print("distance() 1")
    # set Trigger after 0.01ms to LOW
    time.sleep(0.000001)
    GPIO.output(GPIO_TRIGGER1, False)
    print("distance() 2")
    StartTime = time.time()
    StopTime = time.time()
    print("distance() 3")
    # save StartTime
    while GPIO.input(GPIO_ECHO1) == 0:
        print("finding GPIO_ECHO1")
        StartTime = time.time()
    print("distance() 4")
    # save time of arrival
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()
        break
    print("distance() 5")
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    global dist1
    dist1 = (TimeElapsed * 34300) / 2
    time.sleep(1)
'''

def distance1():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER1, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.000001)#0.00001
    GPIO.output(GPIO_TRIGGER1, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    global dist1
    dist1 = (TimeElapsed * 34300) / 2
    time.sleep(1)

def distance2():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER2, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.000001)#0.00001
    GPIO.output(GPIO_TRIGGER2, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    global dist2
    dist2 = (TimeElapsed * 34300) / 2
    time.sleep(1)
  
if __name__ == "__main__":
    try:
        while True:
            distance1()
            distance2()
            print ("Measured Distance1 = %.1f cm" % dist1)
            print ("Measured Distance2 = %.1f cm" % dist2)

            if (dist1>3.0 and dist1<13):#8.5
                print("Obstacle detected at distance1 {} in Alert zone".format(dist1))
            elif (dist1>13 and dist1<21.0):
                print("Obstacle detected at distance1 {} in Alarm zone".format(dist1))

            if (dist2>3.0 and dist2<13):
                print("Obstacle detected at distance2 {} in Alert zone".format(dist2))
            elif (dist2>13 and dist2<21.0):
                print("Obstacle detected at distance2 {} in Alarm zone".format(dist2))

            print ("\n")
            #time.sleep(1)
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
