
from budgeter import Budgeter
from interface import Intrfc

def main():
    
    interface = Intrfc()
    budgeter = Budgeter()
    
    interface.run(budgeter)


main()
