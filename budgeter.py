from account import Account
from budget import Budget
from bill import Bill

class Budgeter:
    def __init__(self):
        self.account = Account("Bank1", float(0))
        #self.account = Account("BankAccount", float(1234))
        self.budgets = set()
        self.bills = set()

    def __repr__(self):
        message = f"Account: {self.account.name}\nsaldo: {self.account.saldo}\n"
        message += f"Money left: {self.moneyLeft()}\n\n"
        
        
        message += "Budgets:\n"
        sum = 0
        for b in self.budgets:
            message += f"{b.name}: {b.saldo}\n"
            sum += b.saldo
        message += f"TOTAL: {sum}\n"
        message += "\n"

        message += "Bills:\n"
        sum = 0
        for b in self.bills:
            message += f"{b.name}: {b.value}\t"
            if b.paid:
                message += "PAID"
            else:
                message += "UNPAID"
            message += "\n"
            sum += b.value
        message += f"TOTAL: {sum}\n"
        message += "\n"

        return message

    def moneyLeft(self):
        moneyLeft = self.account.saldo
        for b in self.budgets:
            moneyLeft -= b.saldo
        for b in self.bills:
            if b.paid == False:
                moneyLeft -= b.value
        return moneyLeft

    def budgetExists(self, name):
        for b in self.budgets:
            if b.name == name:
                 return True
        return False

    def budgetAttainable(self, value):
        sum = value
        for b in self.budgets:
            sum += b.saldo
        if sum <= self.account.saldo:
            return True
        else:
            return False

    def createBudget(self, name, saldo=0):
        if self.budgetExists(name):
            raise LookupError("Budget Already Exists")
        elif self.budgetAttainable(saldo) == False:
            raise ValueError("Not enough funds.")
        else:
            self.budgets.add(Budget(name, saldo))

    def topUpBudget(self, name, saldo):
        if not self.budgetExists(name):
            raise LookupError("Budget Does Not Exist")
        elif self.budgetAttainable(saldo) == False:
            raise ValueError("Not enough funds.")
        else:
            for b in self.budgets:
                if b.name == name:
                    b.saldo += saldo

    def spendBudget(self,name, value):
        if not self.budgetExists(name):
            raise LookupError("Budget Does Not Exist")
        else:
            for b in self.budgets:
                if b.name == name:
                    if value > b.saldo:
                        raise ValueError("Value exceeds the budget.")
                    else:
                        b.saldo -= value
                        self.account.saldo -= value
        
    def deleteBudget(self, name):
        if not self.budgetExists(name):
            raise LookupError("Budget Does Not Exist")
        else:
            for b in self.budgets:
                if b.name == name:
                    self.budgets.discard(b)
                    return


    def billExists(self, name):
        for b in self.bills:
            if b.name == name:
                 return True
        return False

    def createBill(self, name, value=0):
        if self.billExists(name):
            raise LookupError("Bill Already Exists")
        self.bills.add(Bill(name, value))
    
    def deleteBill(self, name):
        if not self.billExists(name):
            raise LookupError("Bill Does Not Exist")
        else:
            for b in self.bills:
                if b.name == name:
                    self.bills.discard(b)
                    return

    def payBill(self, name):
        if not self.billExists(name):
            raise LookupError("Bill Does Not Exist")
        else:
            for b in self.bills:
                if b.name == name:
                    if b.value > self.account.saldo:
                        raise ValueError("Not enough funds to pay the bill.")
                    if b.paid:
                        raise ValueError("Bill already paid.")
                    self.account.saldo -= b.value
                    b.paid = True

    def resetAllBills(self):
        for b in self.bills:
            b.paid = False

    def topUpAccount(self,value):
        self.account.topUp(value)
    