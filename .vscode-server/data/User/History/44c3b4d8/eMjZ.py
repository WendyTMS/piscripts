import time
ticks = time.time()
print ("number of ticks since jan 1970", ticks)

localtime=time.asctime(time.localtime(ticks))
print(localtime)