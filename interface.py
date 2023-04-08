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
            c. Create a bill
            
            """
        )
        
    def run(self):
        self.__run = True
        while self.__run:
            print(f"Want to exit?")
            decision = input()
            if decision.lower() == "yes" or decision.lower() == "y":
                self.__run = False
                print("Bye!")


            
