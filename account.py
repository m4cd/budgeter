
class Account:
    def __init__(self, name, saldo):
        self.saldo = saldo
        self.name = name

    def __repr__(self):
        return f"{self.name} : {self.saldo}"
    
    def topUp(self,amount):
        self.saldo += amount
    
    def withdraw(self, amount):
        self.saldo -= amount

    