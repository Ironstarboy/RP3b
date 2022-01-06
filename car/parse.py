# https://geek-docs.com/python/python-tutorial/python-argparse.html
import run
import global_var
import argparse
import time
import threading
import buzzer



parser = argparse.ArgumentParser(description='car control')
parser.add_argument('-s','--speed',type=int,default=10,help="set inital car speed")
parser.add_argument('-l','--led',default=0,help='set led on or off')
parser.add_argument('-b','--buzzer',default=0,help='set buzzer on or off')
args = parser.parse_args()

if args.led:
    global_var.set('led_switch',1)
    print('led state = {}'.format(args.led))

if args.buzzer:
    global_var.set('buzzer_switch',1)
    print('buzzer state = {}'.format(args.buzzer))

if args.speed:
    global_var.set('speed',args.speed)
    r = threading.Thread(target=run.run)
    r.start()
    print('current speed = {}'.format(global_var.get('speed')))





