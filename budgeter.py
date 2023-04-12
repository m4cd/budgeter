from account import Account
from budget import Budget
from bill import Bill

class Budgeter:
    def __init__(self):
        #self.account = Account("Bank1", 0)
        self.account = Account("Bank1", 1234)
        self.budgets = set()
        self.bills = set()

    def __repr__(self):
        message = f"Account: {self.account.name}\nsaldo: {self.account.saldo}\n\n"
        
        
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
            message += f"{b.name}: {b.value}\n"
            sum += b.value
        message += f"TOTAL: {sum}\n"
        message += "\n"

        return message

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
    
    def topUpAccount(self,value):
        self.account.topUp(value)
    