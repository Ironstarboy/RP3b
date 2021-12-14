import time
import threading

class MyThread(threading.Thread):
    def __init__(self,arg1,arg2):
        super(MyThread, self).__init__()
        self.s=arg1
        self.t=arg2
    def run(self):
        while 1:
            print(self.s)
            time.sleep(self.t)

t1=MyThread('Faster',1)
t2=MyThread('Slower',2)
t1.start()
t2.start()