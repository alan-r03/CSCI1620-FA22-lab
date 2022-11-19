class Account:

    def __init__(self, name):
        self.account_name = name
        self.account_balance = 0

    def is_float(self, amount):
        try:
            float(amount)
            print(True)
            return True
        except:
            print(False)
            return False

    def deposit(self, amount):
        if self.is_float(f'{amount}'.strip()):
            amount = float(f'{amount}'.strip())
            print(amount, type(amount))
            if 0 < amount:
                self.account_balance += round(amount, 2)
                return True
        return False

    def withdraw(self, amount):
        if self.is_float(f'{amount}'.strip()):
            amount = float(f'{amount}'.strip())
            if 0 < amount <= self.account_balance:
                self.account_balance -= round(amount, 2)
                return True
        return False

    def get_balance(self):
        return round(self.account_balance, 2)

    def get_name(self):
        return self.account_name