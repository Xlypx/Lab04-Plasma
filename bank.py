class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
<<<<<<< HEAD
        return self.balance
=======
        return self.balance
>>>>>>> 312d9ff8ebd8eede0788d5629e2b15b75221da3c
