from Singleton import Singleton
from Products import *

class SimpleFactory(metaclass = Singleton):
    def create(self,type,product):
        if type == 1 and product == 1:
            return type1product1()
        if type == 1 and product == 2:
            return type1product2()
        if type == 1 and product == 3:
            return type1product3()
        if type == 1 and product == 4:
            return type1product4()
        if type == 1 and product == 5:
            return type1product5()
        if type == 2 and product == 1:
            return type2product1()
        if type == 2 and product == 2:
            return type2product2()
        if type == 2 and product == 3:
            return type2product3()
        if type == 2 and product == 4:
            return type2product4()
        if type == 2 and product == 5:
            return type2product5()
        if type == 3 and product == 1:
            return type3product1()
        if type == 3 and product == 2:
            return type3product2()
        if type == 3 and product == 3:
            return type3product3()
        if type == 3 and product == 4:
            return type3product4()
        if type == 3 and product == 5:
            return type3product5()

if __name__ == "__main__":
    factory = SimpleFactory()
    #print(id(factory))
    for i in range(1,4):
        for j in range(1,6):
            temp = factory.create(i,j)
            print(temp.doSomething())
