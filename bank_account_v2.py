import sys

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.firstName = None
        self.lastName = None

    def withdraw(self, amount):
        self.balance -= amount
        print("you have", self.balance)
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print("you have", self.balance)
        return self.balance

    def welcome(self):
        start.antechamber()
        start.accountSetUp()
        start.mainMenu()

    def antechamber(self):
        print("Welcome. To continue the program, press 'S'. To quit, press 'Q'.\n")
        button = input("Enter: ")
        if (button == 's') or (button == 'S'):
            start.accountSetUp()
        elif (button == 'q') or (button == 'Q'):
            sys.exit(0)

    def mainMenu(self):
        print(
                "What would you like to do today?\n"
                "W --> Withdraw money\n"
                "D --> Deposit money\n"
                "Q --> Quit\n"
            )
        while True: #possible to make this code look nicer? (does that matter tho?)
            button = input("Enter: ")
            if (button == 'w') or (button == 'W'):
                amount = int(input('Enter amount to withdraw:'))
                start.withdraw(amount)
            elif (button == 'd') or (button == 'D'):
                amount = int(input('Enter amount to deposit:'))
                start.deposit(amount)
            elif (button == 'q') or (button == 'Q'):
                q = input('Are you sure? [Y/N]\n')
                if (q == 'y') or (q == 'Y'):
                    start.antechamber() #takes me back to accountsetup() func -- make it go back somewhere else...
                elif (q == 'n') or (q == 'N'):
                    continue
    
    def accountSetUp(self):
        button = input("Welcome to Synchrony Bank. Do you have an account with us?\n\n[Y/N]") #implement what happens when you press "Yes" -- only "no" exists
        if (button == 'n') or (button == 'N'): #give a choice if user would like to create an account
            start.whatsYourName()
        elif (button == 'y') or (button == 'Y'):
            start.whatsYourName()
        
    def whatsYourName(self): #can i make this reusable?
        x = input("Your first name: ")
        y = input("Your last name: ")
        start.validateName(x, y)

    def validateName(self, firstName, lastName): #changed func name from "askName(...)"
        self.firstName = firstName
        self.lastName = lastName
        while True:
            print("Your first name is", firstName, "and your last name is", lastName, "Correct?\n\n\n")
            button = input("[Y/N]")
            if (button == 'y') or (button == 'Y'):
                start.mainMenu()
            elif (button == 'n') or (button == 'N'):
                start.whatsYourName()

start = BankAccount()
start.welcome()