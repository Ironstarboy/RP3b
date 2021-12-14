import move
import sonic
import time
import threading

# 距离检测线程
detect=threading.Tread(target=sonic.distance)
# 移动线程
f=threading.Tread(target=move.forward)

detect.start()
f.start()


