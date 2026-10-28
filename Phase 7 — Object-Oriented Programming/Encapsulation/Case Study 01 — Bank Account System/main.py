"""
Build a Bank Account class
Difficulty: Beginner → Intermediate

Business scenario
A financial application needs a BankAccount class. Customers should be able to check their balance, deposit money, and withdraw money. 
However, the application must prevent invalid transactions from corrupting the account balance.

Your task is to design the class so that the balance changes only through methods that enforce the required business rules.

Part 1 — Functional requirements
Implement a class named BankAccount with these requirements.
Requirement	                Expected behavior
Initialize account	        Accept an account holder's name and opening balance
Protect balance	            Store it using a double-underscore attribute such as __balance
Read balance	            Provide a getter method
Deposit money	            Accept only a valid positive amount
Withdraw money	            Reject invalid amounts and withdrawals exceeding the balance
Update balance	            Change the balance only after validation succeeds
Handle invalid input	    Do not modify the balance when an operation fails
"""
class BankAccount :
    def __init__(self,name,pin,bal):
        self.__account_holder_name = name 
        self.__account_pin = pin
        self.__account_balance = bal

    def get_balance(self,p):
        # Display the balance only when the PIN is correct
        if p == self.__account_pin:
            print(f"Your Account Balance is : ₹{self.__account_balance} ")
        else :
            print("Invalid Pin !!!")

    def deposit(self,amt):
        # Accept only positive deposit amounts
        if amt <= 0 :
            print("Invalid Amount. Deposit Amount must e greater than Zero.")
            return
        else :
            self.__account_balance = self.__account_balance + amt
            print(f"₹{amt} Deposited Successfully.")

    def withdraw(self,amt):
        # Validate the amount before updating the balance
        if amt <= 0:
            print("Invalid Amount. Withdraal must be greater that zero")

        elif amt > self.__account_balance :
            print("Insufficient Balance! ") 
        else :
            self.__account_balance -= amt
            print(f"₹{amt} Withdrawn Successfully.")

#Create Instance Object 
acc1 = BankAccount("Jenny","1134",10000)

# Test The Operations
acc1.__account_pin = ("1234")
acc1.get_balance("1234")
acc1.get_balance("1134")
acc1.deposit(155)
acc1.get_balance("1134")
acc1.withdraw(2000)
acc1.get_balance("1134")
acc1.withdraw(10000)
acc1.deposit(0)
acc1.deposit(-20)
acc1.get_balance("1134")

        