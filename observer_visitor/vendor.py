from __future__ import annotations

from visitor import VendorVisitor
from obsPattern import Observer,Subject
class Vendor(Subject,Observer):
    def __init__(self, name: str,price, amount: int):
        super().__init__()
        self.name = name
        self.price = price
        self.basePrice = price
        self.margin = 1.1
        self.inflation = 1
        self.amount = amount
        self.availableAmount = amount

    def onBankUpdate(self, bank: bank.Bank):
        self.inflation = bank.inflation
        self.updatePrice()

    def updatePrice(self) -> None:
        self.price = self.basePrice * self.inflation * self.margin
        self.notify()
    
    def sellProduct(self):
        self.availableAmount -= 1

    def hasStock(self):
        if(self.availableAmount > 0):
             return True
        return False
    
    def accept(self, visitor: VendorVisitor):
        visitor.visit(self)