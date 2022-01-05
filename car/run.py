import move
import buzzer
import time
import threading
import LED
import RPi.GPIO as GPIO
import sonic
import global_var
import light


danger_d=15 # 单位厘米，距离内蜂鸣+转弯

threading.Thread(target=sonic.distance).start()
# threading.Thread(target=buzzer.ring).start()  # args=(danger_d,0.5)
threading.Thread(target=light.detect).start()
# threading.Thread(target=LED.run)
# GPIO.output(4,0)#ctrl c退出，会导致ring没来得及执行变成低电平


while 1:
    d = global_var.get('d')  # 不停读取正前方距离d
    R_detected = global_var.get('Rd')  # Rd=0即右前方有东西
    L_detected = global_var.get('Ld')
    move.forward(10)
    move.AIturn(10,d,R_detected,L_detected,danger_d)