import random

class Account:
    """Account class for maintaining a bank account"""

    def __init__(self, name, balance):
        """Initialize an Account object"""
        self.name = name
        self.balance = balance
        self.__user_id = random.randint(pow(10, 5), pow(10, 8))

    def deposit(self, amount):
        """Deposit money to the account"""
        self.balance += amount

# Create an instance of a class
james_account = Account('James Gosling', 50000)

# Let's deposit some money in there
james_account.deposit(500)

# Let's withdraw money from the account
james_account.withdraw(1000)

# Let's see Eric's balance
print(james_account.balance)

# Let's see Eric's user_id
print(james_account.__user_id)


