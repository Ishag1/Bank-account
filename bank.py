class BankAccount:
    # initializing the class
    def __init__(self):
        self.balance = 0


    # this function takes the amount you put in  as a deposit
    def deposit(self, amount):#the balance was zero but when you deposit it increas
        self.balance = self.balance + amount # by the amount you deposit

    def withdraw(self,amount):
        # it takes the amount you withdraw as an argument
        if self.balance >= amount:
            self.balance -= amount # this can be written as self.balance = self.balance - amount 
        else:
            print("Insufficient funds")
    def print_balance(self):
         return self.balance
account = BankAccount() #creating an instance. This is your bank account

account.deposit(100)#Depositing  100 dollars 

account.deposit(100)#depositing

account.deposit(400)
#you have 600 dollars in your account

#print(account.print_balance())

account.withdraw(400)
print(account.print_balance())