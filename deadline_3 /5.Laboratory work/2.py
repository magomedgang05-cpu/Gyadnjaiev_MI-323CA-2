class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance += amount
    
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
    
    def get_balance(self) -> float:
        return self.balance


if __name__ == "__main__":
    account = BankAccount("Фёдор", 100)
    account.deposit(50)
    account.withdraw(200)
    account.withdraw(30)
    print(account.get_balance())