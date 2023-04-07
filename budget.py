class Budget:
    def __init__(self, name, saldo):
        self.saldo = saldo
        self.name = name

    def __repr__(self):
        return f"{self.name} : {self.saldo}"

    