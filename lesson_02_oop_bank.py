class BankAccount:
    def __init__(self, name, initial_balance):
        """Initialize a bank account with name and initial balance."""
        self.name = name
        self.__balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance exists."""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        """Return the current balance."""
        return self.__balance
    
    def get_info(self):
        """Display account information."""
        print(f"Account Holder : {self.name}")
        print(f"Balance : {self.__balance}")

# Test your code
account = BankAccount("Darshan", 1000)

if account.deposit(500):
    print("Deposited 500")

if account.withdraw(200):
    print("Withdrawd 200")

account.get_info()