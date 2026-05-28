import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print(f"Account created for {self.name}")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be between 0 and balance")
        self.show_balance()

    def show_balance(self):
        print(f"Account balance: {self.balance}")

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"{date}: {tran_type} {amount}")


if __name__ == "__main__":
    salman = Account("Tim", 0)
    salman.show_balance()

    salman.deposit(1000)
    salman.withdraw(500)
    salman.withdraw(2000)
    salman.show_transactions()

    alex = Account("Alex", 800)
    alex.deposit(100)
    alex.withdraw(200)
    alex.show_transactions()