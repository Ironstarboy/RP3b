import RPi.GPIO as GPIO
import time
import random

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



def forward(speed):
    # l_speed.stop()
    # r_speed.stop()

    right(speed)
    left(speed)



def backward(speed,t):
    l_speed.stop()
    r_speed.stop()

    right(speed,1)
    left(speed,1)
    if t==-1:
        t=999999
    time.sleep(t)
    l_speed.stop()
    r_speed.stop()


def turnRight(speed=10):
    right(speed,1)
    left(speed)

    time.sleep(0.3)
    l_speed.stop()
    r_speed.stop()


def turnLeft(speed=10):
    right(speed)
    left(speed,1)

    time.sleep(0.35)
    l_speed.stop()
    r_speed.stop()

def stop():
    # 立刻停下
    l_speed.stop()
    r_speed.stop()

def AIturn(speed,d,Rd,Ld,danger_d):

    if d<danger_d or (Rd==0 and Ld==0):
        choice = random.randint(0, 1)
        if choice:
            turnLeft(speed)
        else:
            turnRight(speed)
    if d<danger_d or Rd==1 and Ld==0:
        # 左侧有东西
        turnRight(speed)
        print('Right!')
    if d<danger_d or Rd==0 and Ld==1:
        turnLeft(speed)
        print('Left!')


