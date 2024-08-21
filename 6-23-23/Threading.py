import threading
import time

def eat():
    time.sleep(3)
    print('ate')

def drink():
    time.sleep(4)
    print('drank')

def study():
    time.sleep(5)
    print('studied')

x = threading.Thread(target=eat, args=())
x.start()
y = threading.Thread(target=drink, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

print(threading.active_count())
print(threading.enumerate())