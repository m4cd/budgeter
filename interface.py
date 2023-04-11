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
    c. Spend budget
    d. Create a bill
    e. Pay the bill
    f. Reset billing period
    g. Print summary
    h. Exit        
"""
        )
        option = input()
        option = option.lower()
        match option:
            case "a":
                value = input("How much you want to top up?\n")
                try:
                    value = float(value)
                    budgeter.topUpAccount(value)
                    print(f"\nYour current balance is:\n{budgeter.account.saldo}\n")
                except Exception as e:
                    print(f"Sorry, you did not provide a number. {e}\n")
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
            case "c":
                pass
            case "d":
                pass
            case "e":
                pass
            case "f":
                pass
            case "g":
                print(budgeter)
            case "h":
                self.__run = False
                print("Bye...")
                return
            case _:
                print(f"Sorry, I don't understand...\n")
        input("Press Enter to continue...\n")
        
    def run(self, budgeter):
        while self.__run:
            self.menu(budgeter)

            


            
