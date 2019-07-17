#Final

#Connect ultrasonic ensor to rasp pi directly
#Libraries
#importing the threading module 
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

#for IR Sensor1
ir1=7
ir3=22

servo1=8
servo2=10


"""
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
#for IR Sensor1
ir1=7
#for IR Sensor1
#VCC breadboard rasp pi left pin1 3.3v + multiple male-female wires to vcc of IR 
#GND shorted with US's GND on breadboard
GPIO.setup(7,GPIO.IN)
"""

def initialization():
    GPIO.setmode(GPIO.BOARD)
    
    #set GPIO direction (IN / OUT)
    GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
    GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
    GPIO.setup(GPIO_ECHO1, GPIO.IN)
    GPIO.setup(GPIO_ECHO2, GPIO.IN)

    #for IR Sensor1
    #VCC breadboard rasp pi left pin1 3.3v + multiple male-female wires to vcc of IR 
    #GND shorted with US's GND on breadboard
    GPIO.setup(ir1,GPIO.IN)
    GPIO.setup(ir3,GPIO.IN)

    GPIO.setup(servo1,GPIO.OUT)#12
    global p1
    p1=GPIO.PWM(servo1,50)
    p1.start(10.5)#(0)
    #p1.start(2.5)

    GPIO.setup(servo2,GPIO.OUT)#12
    global p2
    p2=GPIO.PWM(servo2,50)
    p2.start(10.5)#(0)
    #p2.start(2.5)


def distance1():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER1, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
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
    time.sleep(0.00001)
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

def US_exe(ir):
    flag1=False
    flag2=False
    try:
        while True:
            i=GPIO.input(ir3)# 1 for not arrived
            if ir==0 and i==1:
                print("Train arrived")
                distance1()
                distance2()
                print ("Measured Distance1 = %.1f cm" % dist1)
                print ("Measured Distance2 = %.1f cm" % dist2)

                if (dist1>3.0 and dist1<8.5):
                    print("Obstacle detected at distance1 {} in Alert zone".format(dist1))
                    flag1=True
                elif (dist1>8.5 and dist1<21.0):
                    print("Obstacle detected at distance1 {} in Alarm zone".format(dist1))
                    flag1=True
                else:
                    print("no obstacle")
                    flag1=False

                if (dist2>3.0 and dist2<8.5):
                    print("Obstacle detected at distance {} in Alert zone".format(dist2))
                    flag2=True
                    
                elif (dist2>8.5 and dist2<21.0):
                    print("Obstacle detected at distance2 {} in Alarm zone".format(dist2))
                    flag2=True
                else:
                    print("no obstacle")
                    flag2=False
                    
                print ("\n")

                if (flag1==True and flag2==True):#open
                    p1.ChangeDutyCycle(10.5)
                    p2.ChangeDutyCycle(10.5)
                    time.sleep(1)
                elif (flag1==False and flag2==False):#close
                    p1.ChangeDutyCycle(5)
                    p2.ChangeDutyCycle(6.5)
                    time.sleep(1)

                time.sleep(1)
            elif i==0:
                break
        print("Train has arrived very close please stop US")
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        return

 
if __name__ == "__main__":
    #US_exe()
    initialization()
    flag=False
    try:
        while True:
            i=GPIO.input(ir1)
            if i==1:
                print("Train not arrived")
                time.sleep(1)
            elif i==0:
                print("Train arrived")
                #US_exe(i)
                flag=True
                break;
                #US_exe()
                #time.sleep(1)
        print("Train has arrived please start US")
        if flag==True:
            US_exe(i)
    except KeyboardInterrupt:
        GPIO.cleanup()
