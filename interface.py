from budgeter import Budgeter

class Intrfc:
    def __init__(self):
        self.__run = True

    def menu(self, budgeter):
        print(
"""
Pick action:
    a. Top-up your account
    b. Create a budget
    c. Top-up budget
    d. Spend budget
    e. Delete budget
    f. Create a bill
    g. Delete bill
    h. Pay the bill
    i. Reset all bills
    j. Print summary
    k. Exit        
"""
        )
        option = input()
        option = option.lower()
        match option:
            # Top-up your account
            case "a":
                value = input("How much you want to top up?\n")
                try:
                    value = float(value)
                    budgeter.topUpAccount(value)
                    print(f"\nYour current balance is:\n{budgeter.account.saldo}\n")
                except Exception as e:
                    print(f"Sorry, you did not provide a number. {e}\n")
            
            # Create a budget
            case "b":
                try:
                    name = input("Budget name: ")
                    print("")
                    value = input("Budget amount: ")
                    print("")
                    value = float(value)
                    budgeter.createBudget(name, value)
                except Exception as e:
                    print(e)
            
            # Top-up budget
            case "c":
                try:
                    name = input("Budget name: ")
                    print("")
                    value = input("Budget amount: ")
                    print("")
                    value = float(value)
                    budgeter.topUpBudget(name, value)
                except Exception as e:
                    print(e)
            
            # Spend budget
            case "d":
                try:
                    name = input("Budget name: ")
                    print("")
                    value = input("Budget amount: ")
                    print("")
                    value = float(value)
                    budgeter.spendBudget(name, value)
                except Exception as e:
                    print(e)
            
            # Delete budget
            case "e":
                try:
                    name = input("Budget name: ")
                    print("")
                    budgeter.deleteBudget(name)
                except Exception as e:
                    print(e)
            
            # Create a bill
            case "f":
                try:
                    name = input("Bill name: ")
                    print("")
                    value = input("Bill amount: ")
                    print("")
                    value = float(value)
                    budgeter.createBill(name, value)
                except Exception as e:
                    print(e)
            
            # Delete bill
            case "g":
                try:
                    name = input("Bill name: ")
                    print("")
                    budgeter.deleteBill(name)
                except Exception as e:
                    print(e)
            
            # Pay the bill
            case "h":
                try:
                    name = input("Bill name: ")
                    print("")
                    budgeter.payBill(name)
                except Exception as e:
                    print(e)

            # Reset billing period
            case "i":
                try:
                    budgeter.resetAllBills()
                except Exception as e:
                    print(e)
            
            # Print summary
            case "j":
                print(budgeter)
            
            # Exit
            case "k":
                self.__run = False
                print("Bye...")
                return
            case _:
                print(f"Sorry, I don't understand...\n")
        input("Press Enter to continue...\n")
        
    def run(self, budgeter):
        while self.__run:
            self.menu(budgeter)

            


            
