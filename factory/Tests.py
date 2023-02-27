import cProfile
from SimpleFactory import *
from MethodFactory import *
from AbstractFactory import *
from RegisterFactory import *
from RegisterFactoryReflection import *

from Products import type3product4
label = lambda text: f"\n======================== {text.upper()} ========================\n"

def simpleTest():
    print(label("Simple Factory Test"))
    factory = SimpleFactory()
    for i in range(1000000):
        factory.create(3, 4)

def methodTest():
    print(label("Method Factory Test"))
    factory = Type3Factory()
    for i in range(1000000):
        factory.create(4)

def abstractTest():
    print(label("Abstract Factory Test"))
    factory = product4Factory()
    for i in range(1000000):
        factory.t3()

def registerTest():
    print(label("Register Factory Test"))
    factory = RegisterFactory()
    factory.register("type3product4",type3product4)
    for i in range(1000000):
        factory.create("type3product4")

def registerReflectionTest():
    print(label("Register reflection Factory Test"))
    factory = RegisterFactoryReflection()
    factory.register(type3product4)
    for i in range(1000000):
        factory.create('type3product4')

if __name__ == "__main__":
    cProfile.runctx('simpleTest()', globals(), locals())
    cProfile.runctx('methodTest()', globals(), locals())
    cProfile.runctx('abstractTest()', globals(), locals())
    cProfile.runctx('registerTest()', globals(), locals())
    cProfile.runctx('registerReflectionTest()', globals(), locals())
