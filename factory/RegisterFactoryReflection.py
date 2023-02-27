from Singleton import Singleton
from Products import *

class RegisterFactoryReflection(metaclass=Singleton):
    def __init__(self):
        self.registeredClasses = {}

    def register(self, facClass):
        self.registeredClasses[facClass.__name__] = facClass

    def create(self, className):
        return self.registeredClasses[className]()

if __name__ == "__main__":
    fac = RegisterFactoryReflection()
    fac.register(type1product1)
    temp = fac.create("type1product1")
    print(id(temp))
