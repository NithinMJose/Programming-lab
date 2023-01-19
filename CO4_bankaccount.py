class Bank_Account:
    def __init__(self):
        self.balance=0
        print("hello!!! Welcome to the Deposite & withdraw machine")

    def diposit(self):
        amount=float(input("Enter the amount to be Deposited: " ))
        print("\n Amount Diposited $",amount)
        self.balance+=amount
    def withdraw(self):
        amount = float(input("Enter the amount to be Withdraw: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n you withdraw: $",amount)
        else:
            print("\n Insuffient Balance !!!")
    def display(self):
        print("\n Net Available balance = $",self.balance)

s=Bank_Account()

s.diposit()
s.withdraw()
s.display()
