from __future__ import annotations
from abc import ABC, abstractmethod


class BuyerVisitor(ABC):
    @abstractmethod
    def visit(self, buyer):
        pass


class VendorVisitor(ABC):
    @abstractmethod
    def visit(self, seller):
        pass


class BuyerVisitorGetWage(BuyerVisitor):
    def visit(self, buyer):
        buyer.funds += 20


class VendorVisitorRestock(VendorVisitor):
    def visit(self, seller):
        seller.availableAmount = seller.amount