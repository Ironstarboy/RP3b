# 发光感光二极管
# ip:192.168.208.xxx

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # GPIO.BOARD
channel=[2,6]
GPIO.setup(channel,GPIO.OUT)

while True:
    GPIO.output(channel,(GPIO.HIGH,GPIO.LOW))
    time.sleep(0.5)
    GPIO.output(reversed(channel), (GPIO.HIGH, GPIO.LOW))
    time.sleep(0.5)
