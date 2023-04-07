from account import Account
from budget import Budget
from bill import Bill

class Budgeter:
    def __init__(self):
        self.account = Account("Bank1", 0)
        self.budgets = []
        self.bills = []

    def __repr__(self):
        message = f"Account: {self.account.name}\nsaldo: {self.account.saldo}\n\n"
        
        
        message += "Budgets:\n"
        for b in self.budgets:
            message += f"{b.name}: {b.saldo}\n"
        message += "\n"

        message += "Bills:\n"
        for b in self.bills:
            message += f"{b.name}: {b.value}\n"
        message += "\n"

        return message

    def createBudget(self, name, saldo=0):
        self.budgets.append(Budget(name, saldo))

    def createBill(self, name, value=0):
        self.bills.append(Bill(name, value))
    