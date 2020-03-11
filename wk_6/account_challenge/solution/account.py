from decimal import Decimal
import random


class Account:
    """Account class for maintaining a bank account balance"""

    # __init__ method is typically used to initialize various attributes
    # of the object.
    def __init__(self, name, balance):
        """Initialize an Account object"""
        self.name = name
        self.balance = balance
        self.__user_id = random.randint(pow(10, 5), pow(10, 8))

    # Functions inside a class are called methods. This method gives the
    # object the functionality to make a deposit to its balance.
    def deposit(self, amount):
        """Deposit money to the account"""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('You can not have a negative balance')

        # if deposit is greater than zero, add to the object's balance
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account"""

        if self.balance < Decimal('0.00'):
            raise ValueError('You can not overdraft your account')

        # if withdraw is less than balance, subtract amount from balance
        self.balance -= amount

# Create an instance of a class
james_account = Account('James Gosling', 20000000)

# Let's deposit some money in there
james_account.deposit(500)

# Let's withdraw money from the account
james_account.withdraw(1000)

# Let's see Eric's balance
print(james_account.balance)

# Let's see Eric's user_id (this will throw an error)
# print(james_account.__user_id)


# Inheritance example: Create a child class from Account
class SavingsAccount(Account):
    """Initialize a SavingsAccount object"""
    @property
    def interest_rate(self):
        """Return the interest_rate of the account"""
        return 0.00299

    def calc_interest_gain(self):
        """Calculate annual interest rate"""
        interest = self.interest_rate
        return self.balance * interest

# Create an instance of SavingsAccount
yukihiro_account = SavingsAccount('Yukihiro Matsumoto', 15000000)

# Try to print a private attribute (this will throw an error)
# print(yukihiro_account.interest_rate)

# Calculate interest gain
print(yukihiro_account.calc_interest_gain())

