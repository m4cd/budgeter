
from budgeter import Budgeter

def main():
    budgeter = Budgeter()
    budgeter.createBudget("skoki", 1000)
    budgeter.createBudget("dziwki", 2000)
    budgeter.createBill("rent", 400)
    print(budgeter)

main()
