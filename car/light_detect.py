'''
底部5个光照强度探测仪
'''
import RPi.GPIO as GPIO
import time
import move

CS = 5
CLOCK = 25
ADDRESS = 24
DATAOUT = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup ((CS , CLOCK , ADDRESS), GPIO.OUT)
GPIO.setup(DATAOUT , GPIO.IN , GPIO.PUD_UP)
def AnalogRead ():
     value = [0]*(6)
     #Read Channel0~channel5 AD value
     for j in range(0, 6):
          GPIO.output(CS , GPIO.LOW)
          for i in range(0, 10):
               #sent 4-bit Address
               if (i < 4):
                    bit = (((j) >> (3 - i)) & 0x01)
                    GPIO.output(ADDRESS , bit)

               #read 10-bit data
               value[j] <<= 1
               value[j] |= GPIO.input(DATAOUT)
               GPIO.output(CLOCK , GPIO.HIGH)
               GPIO.output(CLOCK , GPIO.LOW)

          GPIO.output(CS , GPIO.HIGH)
          time.sleep (0.0001)
     return value [1:] # invalid address for channel 0

# pwr是数组后面
while True:
     d=AnalogRead ()
     left=sum(d[:2])
     right=sum(d[3:])

     if(left<right):
          move.left()
          print('left')
     else:
          move.right()
          print('right')
     time.sleep(0.5)
