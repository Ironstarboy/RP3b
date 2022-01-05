'''
蜂鸣器
'''
import RPi.GPIO as GPIO
import time
import global_var

GPIO.setmode(GPIO.BCM)
buzzer=4
GPIO.setup(buzzer,GPIO.OUT)

# 有时候蜂鸣器会关不掉
def ring(danger_d=15,t=0.1):
    while 1:
        if global_var.get('d')<danger_d:
            GPIO.output(buzzer,1) #GPIO.HIGH,高电压响
            time.sleep(t)
            GPIO.output(buzzer,0)


