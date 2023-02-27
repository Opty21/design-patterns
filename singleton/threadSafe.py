from threading import Lock, Thread
from time import sleep
from abc import ABCMeta

class ThreadSafeSingletonMeta(ABCMeta):
    _instances = {}
    _lock: Lock = Lock()
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._lock.acquire()
            
            if cls not in cls._instances:
                
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            sleep(0.1)
            cls._lock.release()

        return cls._instances[cls]

class ThreadSafeSingleton(metaclass=ThreadSafeSingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

def singletonCreate(value: str):
    singleton = ThreadSafeSingleton(value)
    print(singleton.value)

def testSingleton():
    temp:Thread = []
    for i in range(0,15):
        temp.append(Thread(target=singletonCreate,args=(str(i),)))
    for i in temp:
        i.start()
    for i in temp:
        i.join()
        
if __name__ == "__main__":
    testSingleton()