
from budgeter import Budgeter
from interface import Intrfc

def main():
    
    interface = Intrfc()
    budgeter = Budgeter()

    #budgeter.createBudget("skoki", 1000)
    #budgeter.createBudget("dziwki", 2000)
    #budgeter.createBill("rent", 400)
    
    interface.run()


main()
