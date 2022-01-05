import RPi.GPIO as GPIO
import time
import global_var

'''
灵敏度：往中间旋转会变得灵敏，远距离就能探测到
'''
R =19  # 右侧感光二极管探测器,有东西就变成0
L=16
GPIO.setmode(GPIO.BCM)
GPIO.setup(R,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(L,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def detect():
    while 1:
        global_var.set('Rd',GPIO.input(R))
        global_var.set('Ld', GPIO.input(L))
        time.sleep(0.1)

