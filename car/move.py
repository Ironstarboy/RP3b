import RPi.GPIO as GPIO
import time
l1 = 12
l2 = 13
l_control = 6

r1=20# pwr指示灯那边
r2=21
r_control=26
GPIO.setmode(GPIO.BCM)
GPIO.setup((l1, l2, l_control), GPIO.OUT)
GPIO.setup((r1, r2, r_control), GPIO.OUT)
l_speed = GPIO.PWM(l_control, 1000)
r_speed = GPIO.PWM(r_control, 1000)

def right(speed,reverse=0):
    # 右轮子转
    GPIO.output((r1, r2), (0,1))
    if reverse:
        GPIO.output((r1, r2), (1,0))
    l_speed.start(speed)


def left(speed,reverse=0):
    GPIO.output((l1, l2), (0,1))
    if reverse:
        GPIO.output((l1, l2), (1,0))
    r_speed.start(speed)



def forward(speed,t=-1):
    l_speed.stop()
    r_speed.stop()

    right(speed)
    left(speed)
    if t==-1:
        t=999999
    time.sleep(t)
    l_speed.stop()
    r_speed.stop()



def backward(speed,t=-1):
    l_speed.stop()
    r_speed.stop()

    right(speed,1)
    left(speed,1)
    if t==-1:
        t=999999
    time.sleep(t)
    l_speed.stop()
    r_speed.stop()

def turnRight(speed):
    right(speed)
    left(speed*1.3+10)

    time.sleep(1)
    l_speed.stop()
    r_speed.stop()

def turnLeft(speed):
    right(speed*1.2+10)
    left(speed)

    time.sleep(1)
    l_speed.stop()
    r_speed.stop()





