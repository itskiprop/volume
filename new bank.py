#create a class bank account
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
#methods
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return amount
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return amount
            else:
                return "Insufficient balance"
        else:
            return "Invalid withdrawal amount"
#attributes of the class
    def check_balance(self):
        print(f"Current balance: ksh{self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Account Opening: {self.date_of_opening}")
        print(f"Current Balance: ksh{self.balance}")


# sample
if __name__ == "__main__":
    account = BankAccount("55555", 50000, "2023-11-1", "big boss")
    account.customer_details()
    print("Deposited:", account.deposit(1000))
    account.check_balance()
    print("Withdrawn:", account.withdraw(2000))
    account.check_balance()
