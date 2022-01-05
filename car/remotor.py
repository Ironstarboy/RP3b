import RPi.GPIO as GPIO
import time
ir=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(ir,GPIO.IN,GPIO.PUD_UP)
keymap={
  0x45:'CH-',0x46:'CH ',0x47:'CH+',
  0x44:'<<<',0x40:'>>>',0x43:'>>|',
  0x47:' - ',0x15:' + ',0x09:'EQ ',
  0x07:' 0 ',0x19:'100+',0x0D:'200+',
  0x0C:' 1 ',0x18:' 2 ',0x5E:' 3 ',
  0x08:' 4 ',0x1C:' 5 ',0x5A:' 6 ',
  0x42:' 7 ',0x52:' 8 ',0x4A:' 9 '}

def getkey():
  if GPIO.input(ir) == GPIO.HIGH:
    return
  channel = GPIO.wait_for_edge(ir,GPIO.RISING,timeout=8)
  GPIO.remove_event_detect(ir)
  if channel is not None:
    return

  time.sleep(0.0045)

  data = 0
  for shift in range(0,32):
    while GPIO.input(ir) == GPIO.LOW:
      time.sleep(0.0001)

    count = 0
    while GPIO.input(ir) == GPIO.HIGH and count < 10:
      count += 1
      time.sleep(0.0005)

    if(count > 1):
      data |=1<<shift

  a1 = (data >> 24) & 0xff
  a2 = (data >> 16) & 0xff
  a3 = (data >> 8) & 0xff
  a4 = (data) & 0xff
  if ((a1+a2) == 0xff) and ((a3+a4) == 0xff):
    return a2
  else: print("repeat key")

print('irremote test start ...')

while True:
  key = getkey()
  if(key != None):
    print('key = ',keymap[key])



A=13
B=12
CONTROL=6
GPIO.setmode(GPIO.BCM)
GPIO.setup((A,B,CONTROL),GPIO.OUT)
speed=GPIO.PWM(CONTROL,1000)
GPIO.output((A,B),(1,0))

f=open('/dev/input/event0','rb')

while True:
  d=f.read(48)
  key=d.hex()[40:42]
  print(key)
  if(key == 18):
    speed.start(90)
    time.sleep(1)
    speed.stop()
    GPIO.output((A,B),(0,1))
    speed.ChangeDutyCycle(20)
    time.sleep(1)
    speed.stop()
    GPIO.cleanup()