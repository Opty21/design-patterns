from abc import ABC, abstractmethod

class Product(ABC):
    pass

class type1(Product):
    @abstractmethod
    def doSomething(self) -> int:
        pass

class type2(Product):
    @abstractmethod
    def doSomething(self) -> tuple[bool, int]:
        pass

class type3(Product):
    @abstractmethod
    def doSomething(self) -> tuple[bool, str, int]:
        pass


class type1product1(type1):
    def doSomething(self) -> int:
        return 1

class type1product2(type1):
    def doSomething(self) -> int:
        return 2

class type1product3(type1):
    def doSomething(self) -> int:
        return 3
class type1product4(type1):
    def doSomething(self) -> int:
        return 4
class type1product5(type1):
    def doSomething(self) -> int:
        return 5

class type2product1(type2):
    def doSomething(self) -> tuple[bool, int]:
        return True,1

class type2product2(type2):
    def doSomething(self) -> tuple[bool, int]:
        return False,2

class type2product3(type2):
    def doSomething(self) -> tuple[bool, int]:
        return True,3

class type2product4(type2):
    def doSomething(self) -> tuple[bool, int]:
        return True,4

class type2product5(type2):
    def doSomething(self) -> tuple[bool, int]:
        return True,5

class type3product1(type3):
    def doSomething(self) -> tuple[bool, str, int]:
        return True,"type3Product1",3332323

class type3product2(type3):
    def doSomething(self) -> tuple[bool, str, int]:
        return True,"type3Product2",5555555

class type3product3(type3):
    def doSomething(self) -> tuple[bool, str, int]:
        return False,"type3Product3",555222121

class type3product4(type3):
    def doSomething(self) -> tuple[bool, str, int]:
        return False,"type3Product4",55756756757

class type3product5(type3):
    def doSomething(self) -> tuple[bool, str, int]:
        return False,"type3Product5",5556666