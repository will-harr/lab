class Account:
    def __init__(self, name: str):
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: float):
        if amount > 0:
            self.account_balance += amount
            return True

        else:
            return False

    def withdraw(self, amount: float):
        if (amount > 0) and (amount <= self.account_balance):
            self.account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.account_balance

    def get_name(self):
        return self.account_name
