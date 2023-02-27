from threading import Thread, local
from abc import ABCMeta

class ThreadLocalSingletonMeta(ABCMeta):
    _thread_local = local()
    def __call__(cls, *args, **kwargs):
        if 'instance' not in dir(cls._thread_local):
            cls._thread_local.instance = super().__call__(*args, **kwargs)
        return cls._thread_local.instance

class ThreadLocalSingleton(metaclass=ThreadLocalSingletonMeta):
    value: int = 0
    def addNumber(self,value):
        self.value += value

def singletonCreate():
    singleton = ThreadLocalSingleton()
    print("Created thread singleton: " + str(id(singleton)))
    for i in range(0,3):
        singleton.addNumber(10)
    print(str(id(singleton)) + ": " + str(singleton.value))

def testSingleton():
    temp:Thread = []
    for i in range(0,15):
        temp.append(Thread(target=singletonCreate))
    for i in temp:
        i.start()
    for i in temp:
        i.join()

if __name__ == "__main__":
    testSingleton()