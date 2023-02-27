from Singleton import Singleton
from Products import *

class RegisterFactory(metaclass=Singleton):
    def __init__(self):
        self.registeredClasses = {}

    def register(self, className, classInit):
        self.registeredClasses[className] = classInit

    def create(self, className):
        return self.registeredClasses[className]()

if __name__ == "__main__":
    fac = RegisterFactory()
    fac.register("type1product1",type1product1)
    temp = fac.create("type1product1")
    print(id(temp))
