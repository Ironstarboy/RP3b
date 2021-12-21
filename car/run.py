import move

import time
import threading
import LED
import RPi.GPIO as GPIO
from concurrent.futures import ThreadPoolExecutor

d=100

GPIO.setmode(GPIO.BCM)  # GPIO.BOARD
Trig=22  # tirg links out
Echo=27  # echo links in
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)
def distance():
    global d
    while 1:
        GPIO.output(Trig,GPIO.HIGH)
        time.sleep(0.1) # sleep时间太短，d一直是同一个数字
        GPIO.output(Trig,GPIO.LOW)
        while GPIO.input(Echo)==GPIO.LOW:
            pass
        t1=time.time()
        while GPIO.input(Echo) == GPIO.HIGH:
            pass
        t2=time.time()
        d=(t2-t1)*34000/2

dis=threading.Thread(target=distance)
dis.start()

angel=0
count=0 #转向次数，多次转不出来就后退
while 1:
    move.forward(10,d)
    print(d)
    if d < 15:
        print(d)
        if angel < 180:
            angel += 30
            count+=1
            move.turnLeft()
        else:
            angel -= 30
            count+=1
            move.turnRight()
        if count>10:
            #　进入死角　后退并转弯
            move.backward(speed=10,t=2)
            move.turnRight()
            angel-=30
            count=0










