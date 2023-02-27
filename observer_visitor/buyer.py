from obsPattern import Observer, Subject
from vendor import Vendor
from visitor import BuyerVisitor
from bank import Bank
import random 

class Buyer(Observer,Subject):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.funds: float = 20
        self.lastPurchase = 0

    def onVendorUpdate(self,vendor:Vendor):
        buyChance = random.random()
        if(vendor.basePrice / vendor.price > 0.5):
             buyChance -= 0.1
        if buyChance > 0.5 and vendor.price <= self.funds:
            self.buy(vendor)

    def buy(self,vendor:Vendor):
        if vendor.hasStock():
            print("Klient " + self.name + " kupił produkt od " + vendor.name)
            self.funds -= vendor.price
            self.lastPurchase = vendor.price
            self.notify()
            vendor.sellProduct()
            
    def onBankUpdate(self, bank: Bank):
        self.inflation = bank.inflation

    def accept(self, visitor: BuyerVisitor):
        visitor.visit(self)