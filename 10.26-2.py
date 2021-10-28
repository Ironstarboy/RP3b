"""
2头孔 和一头孔一头针的电线
针不接触输出0
接触输出1
GPIO2 3默认pud dwon
得用其他GPIO
"""


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # GPIO.BOARD

GPIO.setup(18,GPIO.IN) # 2 3默认已经上拉
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,GPIO.HIGH)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
    x=GPIO.input(18)  # 读出2口的电流
    print(x)
    time.sleep(0.1)

GPIO.cleanup((2,3))
GPIO.cleanup()