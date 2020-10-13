import threading
import time

start = time.perf_counter()

def do_something():
    print(" sleeping ")
    time.sleep(1)
    print(" done sleeping ")

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

stop = time.perf_counter()

print(round(stop - start))