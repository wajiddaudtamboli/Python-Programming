# Thread

class Hello:
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi:
    def run(self):
        for i in range (5):
            print("Hi")
            sleep(1)

t=time()
t1=Hello
t2=Hi
t1.run()
t2.run()
print("Done",time()-t)
'''


# using Thread

from threading import *
from time import *

class Hello(Thread):
    def run(self):
        for i in range (5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range (5):
            print("Hi")
            sleep(1)

t=time()
t1=Hello()
t2=Hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("Done",time()-t)
'''
