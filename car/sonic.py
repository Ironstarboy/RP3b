import RPi.GPIO as GPIO
import time
import move

GPIO.setmode(GPIO.BCM)  # GPIO.BOARD
Trig=22  # tirg links out
Echo=27  # echo links in
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

def  distance():
    GPIO.output(Trig,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Trig,GPIO.LOW)
    while GPIO.input(Echo)==GPIO.LOW:
        pass
    t1=time.time()
    while GPIO.input(Echo) == GPIO.HIGH:
        pass
    t2=time.time()
    return (t2-t1)*34000/2




