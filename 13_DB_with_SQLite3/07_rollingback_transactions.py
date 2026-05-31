class Account:

    def __init__(self, name, opening_balance=0.0):
        self.name = name
        self._balance = opening_balance
        print(f"Account created for {name} ", end="")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0.0:
            self._balance += amount
            print(f"Account deposited {amount}")
        return self._balance

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Account withdrew {amount}")
            return self._balance
        else:
            print("Insufficient balance")
            return 0.0

    def show_balance(self):
        print(f"Balance on account: {self._balance}")


if __name__ == "__main__":
    john = Account("John")
    john.deposit(10.10)
    john.deposit(0.10)
    john.deposit(0.10)

    john.withdraw(0.10)
    john.show_balance()