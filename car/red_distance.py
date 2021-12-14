'''
底盘2个红外距离探测
'''
import RPi.GPIO as GPIO
import time

def my_callback(channel ):
    print('This is a edge event callback function!')
    print('Edge detected on channel ', channel)



GPIO.setmode(GPIO.BCM)  # GPIO.BOARD
channel=26
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.add_event_detect(channel,
                      GPIO.FALLING, # 电压从高变低
                      callback=my_callback,
                      bouncetime=2000) # falling发生就会调用回调函数
# bouncetime,是指手放入感光器下，光反照变强，但是其实会多次输入信号
for i in range(1000):
    print(i)
    time.sleep(1)
    # 在做这个事情时，如果有falling ,中断Print(i) 调用回调函数