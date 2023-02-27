from bank import Bank
from visitor import *
import unittest
from buyer import Buyer
from vendor import Vendor
from obsPattern import Observer,Subject
class MyTestCase(unittest.TestCase):
    def testBuyerInflation(self):
        bank = Bank(1.5, 5)
        buyer = Buyer("Mark")
        buyer.observe(bank, buyer.onBankUpdate)
        bank.nextRound()
        self.assertEqual(buyer.inflation, 1.6)

    def testVendorInflation(self):
        bank = Bank(2, 5)
        vendor = Vendor("Paolo",4,2)
        vendor.observe(bank, vendor.onBankUpdate)
        bank.nextRound()
        bank.nextRound()
        bank.nextRound()
        self.assertEqual(round(vendor.inflation,2), 2.3)
    
    def testBuyerAccept(self):
        buyer = Buyer("Mark")      
        self.assertEqual(buyer.funds, 20)
        buyer.accept(BuyerVisitorGetWage())
        self.assertEqual(buyer.funds,40)
        
    def testVendorAccept(self):
        vendor = Vendor("Paolo",4,2)
        self.assertEqual(vendor.availableAmount, 2)
        vendor.availableAmount = 0
        self.assertEqual(vendor.availableAmount, 0)
        vendor.accept(VendorVisitorRestock())
        self.assertEqual(vendor.availableAmount, 2)

    def testVendorStockStatusAbove(self):
        vendor = Vendor("Paolo",4,2)
        self.assertTrue(vendor.hasStock())

    def testVendorStockStatusEmpty(self):
        vendor = Vendor("Paolo",4,0)
        self.assertFalse(vendor.hasStock())

    def testBuyerPays(self):
        vendor = Vendor("Paolo",4,2)
        buyer = Buyer("Marysia")
        buyer.buy(vendor)
        self.assertAlmostEqual(buyer.funds, 16)

    def testVendorAmountDecreases(self):
        vendor = Vendor("Paolo",4,2)
        buyer = Buyer("Marysia")
        buyer.buy(vendor)
        self.assertAlmostEqual(vendor.availableAmount, 1)        

    def testBuyerCantBuyMoreThanAvailable(self):
        vendor = Vendor("Paolo",4,2)
        buyer = Buyer("Marysia")
        buyer.buy(vendor)
        buyer.buy(vendor)
        buyer.buy(vendor)
        self.assertAlmostEqual(buyer.funds, 12)

    def testBankObserver(self):
        self.assertTrue(issubclass(Bank, Observer))

    def testVendorObserver(self):
        self.assertTrue(issubclass(Vendor, Observer))

    def testBankSubject(self):
        self.assertTrue(issubclass(Bank, Subject))

    def testBuyerObserver(self):
        self.assertTrue(issubclass(Buyer, Observer))

    def testVendorSubject(self):
        self.assertTrue(issubclass(Vendor, Subject))
    
    
if __name__ == '__main__':
    unittest.main()