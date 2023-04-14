import unittest

from budgeter import Budgeter


class Tests(unittest.TestCase):
    def testAccountExists(self):
        b = Budgeter()

        self.assertEqual(
            b.account.saldo,
            0,
        )

    def testMoneyLeft(self):
        b = Budgeter()
        b.topUpAccount(200)
        b.createBudget("aaaa",100)
        b.createBill("bbbb", 100)

        self.assertEqual(
            b.moneyLeft(),
            0,
        )

    def testBudgetExists(self):
        b = Budgeter()
        b.topUpAccount(200)
        b.createBudget("aaaa",100)

        self.assertEqual(
            b.budgetExists("aaaa"),
            True
        )

        b.budgets.pop()

        self.assertEqual(
            b.budgetExists("aaaa"),
            False
        )

    def testBudgetAttainable(self):
        b = Budgeter()
        b.topUpAccount(200)
        
        self.assertEqual(
            b.budgetAttainable(200),
            True
        )

        self.assertEqual(
            b.budgetAttainable(201),
            False
        )

    def testCreateBudget(self):
        b = Budgeter()
        b.topUpAccount(100)
        b.createBudget("aaaa", 100)

        c = b.budgets.pop()

        self.assertEqual(
            c.name,
            "aaaa"
        )

        self.assertEqual(
            c.saldo,
            100
        )

        b.createBudget("aaaa", 100)
        with self.assertRaises(LookupError):
            b.createBudget("aaaa", 100)
        with self.assertRaises(ValueError):
            b.createBudget("bbbb", 1000)

    def testTopUpBudget(self):
        b = Budgeter()
        b.topUpAccount(200)
        b.createBudget("aaaa", 100)
        b.topUpBudget("aaaa",100)

        c = b.budgets.pop()

        self.assertEqual(
            c.name,
            "aaaa"
        )

        self.assertEqual(
            c.saldo,
            200
        )

        with self.assertRaises(LookupError):
            b.topUpBudget("aaaa", 100)
        
        b.createBudget("aaaa", 100)

        with self.assertRaises(ValueError):
            b.topUpBudget("aaaa", 1000)

    def testSpendBudget(self):
        b = Budgeter()
        b.topUpAccount(200)
        b.createBudget("aaaa", 100)
        b.spendBudget("aaaa",50)

        c = b.budgets.pop()

        self.assertEqual(
            c.saldo,
            50
        )

        self.assertEqual(
            b.account.saldo,
            150
        )

        with self.assertRaises(LookupError):
            b.spendBudget("aaaa", 100)
        
        b.createBudget("aaaa", 100)

        with self.assertRaises(ValueError):
            b.spendBudget("aaaa", 101)


    def testDeleteBudget(self):
        b = Budgeter()
        b.topUpAccount(200)
        b.createBudget("aaaa", 100)
        b.deleteBudget("aaaa")
        
        self.assertEqual(
            len(b.budgets),
            0
        )

        with self.assertRaises(LookupError):
            b.spendBudget("aaaa", 100)

    def testCreateBill(self):
        b = Budgeter()
        b.topUpAccount(200)
        b.createBill("aaaa", 100)

        c = b.bills.pop()

        self.assertEqual(
            c.name,
            "aaaa"
        )

        self.assertEqual(
            c.value,
            100
        )

        b.createBill("aaaa", 100)
        with self.assertRaises(LookupError):
            b.createBill("aaaa", 100)

    def testDeleteBill(self):
        b = Budgeter()
        b.topUpAccount(200)
        b.createBill("aaaa", 100)

        with self.assertRaises(LookupError):
            b.deleteBill("bbbb")
        
        b.bills.pop()

        self.assertEqual(
            len(b.bills),
            0
        )

    def testPayBill(self):
        b = Budgeter()
        b.topUpAccount(200)
        b.createBill("aaaa", 201)

        with self.assertRaises(LookupError):
            b.payBill("bbbb")
        
        b.createBill("bbbb", 100)
        
        for bill in b.bills:
            bill.paid = True

        with self.assertRaises(ValueError):
            b.payBill("aaaa")

    def testResetAllBills(self):
        b = Budgeter()
        b.topUpAccount(200)
        b.createBill("aaaa", 100)
        b.createBill("bbbb", 50)

        b.payBill("aaaa")
        b.payBill("bbbb")

        b.resetAllBills()

        for bill in b.bills:
            self.assertEqual(
                bill.paid,
                False
            )
            
    def testTopUpAccount(self):
        b = Budgeter()
        b.topUpAccount(200)

        self.assertEqual(
            b.account.saldo,
            200
        )

        b.topUpAccount(200)
        self.assertEqual(
            b.account.saldo,
            400
        )




if __name__ == "__main__":
    unittest.main()