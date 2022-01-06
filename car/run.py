import move
import buzzer
import time
import threading
import LED
import RPi.GPIO as GPIO
import sonic
import global_var
import light
import argparse



danger_d=15 # 单位厘米，距离内蜂鸣+转弯

threading.Thread(target=sonic.distance).start()
buz=threading.Thread(target=buzzer.ring) # args=(danger_d,0.5)
threading.Thread(target=light.detect).start()
led=threading.Thread(target=LED.run)
threading.Thread(target=move.readSpeed).start()  # 运行中改变次小车速度
# GPIO.output(4,0)#ctrl c退出，会导致ring没来得及执行变成低电平代码

def run():
    if global_var.get('buzzer_switch'):
        buz.start()
    if global_var.get('led_switch'):
        led.start()
    while 1:
        d = global_var.get('d')  # 不停读取正前方距离d
        R_detected = global_var.get('Rd')  # Rd=0即右前方有东西
        L_detected = global_var.get('Ld')
        move.forward(global_var.get('speed'))
        move.AIturn(10,d,R_detected,L_detected,danger_d)


