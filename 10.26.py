import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # GPIO.BOARD
GPIO.setup((2,3),GPIO.OUT)

while True:
    GPIO.output((2,3),(GPIO.HIGH,GPIO.LOW))
    time.sleep(0.5)
    GPIO.output((3,2), (GPIO.HIGH, GPIO.LOW))
    time.sleep(0.5)