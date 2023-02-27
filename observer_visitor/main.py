import random
from vendor import Vendor
from buyer import Buyer
from bank import Bank
from visitor import BuyerVisitorGetWage, VendorVisitorRestock
import time

sellers = [Vendor("Antonio",5,3),Vendor("Mario",2,7),Vendor("Frank",3,2)]
customers = [Buyer("Dorota"),Buyer("Ray"),Buyer("Henry")]
bank = Bank(1.8,10)

days = 30
for seller in sellers:
    seller.observe(bank,seller.onBankUpdate)

for customer in customers:
    bank.observe(customer,bank.onBuyerUpdate)
    customer.observe(bank,customer.onBankUpdate)

    for seller in sellers:
        interestLevel = random.random()
        if(interestLevel > 0.4):
            print("Klient " + customer.name + " obserwuje produkt sprzedawcy " + seller.name)
            customer.observe(seller,customer.onVendorUpdate)


print("\n\nROZPOCZĘCIE SYMULACJI")

for i in range(1,days):
    print("\n\n =-=-=-=-    dzien " + str(i) + "        =-=-=-=-=-\n")
    if(i%3 == 0):
        for seller in sellers:
            seller.accept(VendorVisitorRestock())
    if(i%4 == 0):
        for customer in customers:
            customer.accept(BuyerVisitorGetWage())
    bank.nextRound()

