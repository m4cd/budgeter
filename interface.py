from budgeter import Budgeter

class Intrfc:
    def __init__(self):
        self.__run = False

    def menu(self):
        print(
"""
Pick action:
    a. Top-up your account
    b. Create a budget
    c. Spend budget
    d. Create a bill
    e. Pay the bill
    f. Reset billing period
    g. Exit        
"""
        )
        
    def run(self):
        self.__run = True
        while self.__run:
            self.menu()
            option = input()
            option = option.lower()
            match option:
                case "a":
                    pass
                case "b":
                    pass
                case "c":
                    pass
                case "d":
                    pass
                case "e":
                    pass
                case "f":
                    pass
                case "g":
                    self.__run = False
                    print("Bye...")
                case _:
                    print(f"Sorry, I don't understand...")
            


            
