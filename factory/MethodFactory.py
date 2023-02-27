from Singleton import Singleton
from Products import *

class AbstractFactory(metaclass=Singleton):

    @abstractmethod
    def create(self,prod,add1,add2) -> Product:
        pass
    

class ticketFactory(AbstractFactory):
    def create(self,prod,add1,add2) -> Product:
        if prod == 1:
            return type1product1()
        if prod == 2:
            return type1product2()
        if prod == 3:
            return type1product3()
        if prod == 4:
            return type1product4()
        if prod == 5:
            return type1product5()
        raise Exception('No such class')

class Type2Factory(AbstractFactory):
    def create(self,prod) -> Product:
        if prod == 1:
            return type2product1()
        if prod == 2:
            return type2product2()
        if prod == 3:
            return type2product3()
        if prod == 4:
            return type2product4()
        if prod == 5:
            return type2product5()
        raise Exception('No such class')

class Type3Factory(AbstractFactory):
    def create(self,prod) -> Product:
        if prod == 1:
            return type3product1()
        if prod == 2:
            return type3product2()
        if prod == 3:
            return type3product3()
        if prod == 4:
            return type3product4()
        if prod == 5:
            return type3product5()
        raise Exception('No such class')

