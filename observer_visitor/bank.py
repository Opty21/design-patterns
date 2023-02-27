from __future__ import annotations

from obsPattern import Observer, Subject

class Bank(Subject,Observer):
    def __init__(self, inflation: float, expectedIncome: float):
        super().__init__()
        self.inflation = inflation
        self.currentIncome = 0
        self.expectedIncome = expectedIncome
    
    def onBuyerUpdate(self,buyer:Buyer):
        self.currentIncome += buyer.lastPurchase

    def nextRound(self):
        if self.currentIncome < self.expectedIncome:
            self.inflation = self.inflation + 0.1
        else:
            self.inflation = self.inflation - 0.1
        print("wczorajszy zysk: "+ str(round(self.currentIncome,2)) + " | inflacja: " + str(round(self.inflation,1)))
        self.currentIncome = 0
        self.notify()

