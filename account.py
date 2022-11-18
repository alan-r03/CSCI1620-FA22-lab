class Account:

    def __init__(self, name):
        self.account_name = name
        self.account_balance = 0

    def is_float(self, amount):
        try:
            float(amount.strip())
            return True
        except:
            return False

    def deposit(self, amount):
        if is_float(amount):
            amount = float(amount.strip())
            if 0 < amount:
                self.account_balance += amount
                return True
        return False

    def withdraw(self, amount):
        if is_float(amount):
            amount = float(amount.strip())
            if 0 < amount <= self.account_balance:
                self.account_balance -= amount
                return True
        return False

    def get_balance(self):
        return self.account_balance

    def get_name(self):
        return self.account_name