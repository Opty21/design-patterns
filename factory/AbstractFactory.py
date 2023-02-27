from Singleton import Singleton
from Products import *

class AbstractFactory(metaclass=Singleton):

    @abstractmethod
    def t1(self) -> type1:
        pass

    @abstractmethod
    def t2(self) -> type2:
        pass

    @abstractmethod
    def t3(self) -> type3:
        pass

class product1Factory(AbstractFactory):
    
    def t1(self) -> type1:
        return type1product1()
    
    def t2(self) -> type2:
        return type2product1()
    
    def t3(self) -> type3:
        return type3product1()

class product2Factory(AbstractFactory):
    
    def t1(self) -> type1:
        return type1product2()
    
    def t2(self) -> type2:
        return type2product2()
    
    def t3(self) -> type3:
        return type3product2()

class product3Factory(AbstractFactory):
    
    def t1(self) -> type1:
        return type1product3()
    
    def t2(self) -> type2:
        return type2product3()
    
    def t3(self) -> type3:
        return type3product3()

class product4Factory(AbstractFactory):
    
    def t1(self) -> type1:
        return type1product4()
    
    def t2(self) -> type2:
        return type2product4()
    
    def t3(self) -> type3:
        return type3product4()

class product5Factory(AbstractFactory):
    
    def t1(self) -> type1:
        return type1product5()
    
    def t2(self) -> type2:
        return type2product5()

    def t3(self) -> type3:
        return type3product5()


if __name__ == "__main__":
    factory = product3Factory()
    print(factory.t2().doSomething())