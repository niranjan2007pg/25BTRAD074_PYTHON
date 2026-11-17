# Lab Exercise 14: Bank Account System Using OOP
# Student: Niranjan P G | USN: 25BTRAD074

class BankAccount:
    def __init__(self, acc_no, holder, balance=0.0):
        self.__acc_no = acc_no
        self.__holder = holder
        self.__balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: Rs.{amount:.2f} | Balance: Rs.{self.__balance:.2f}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Withdrawal Rejected: Insufficient balance! (Req: Rs.{amount:.2f})")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrawn: Rs.{amount:.2f} | Remaining: Rs.{self.__balance:.2f}")

    def display(self):
        print(f"Account: {self.__acc_no} | Holder: {self.__holder} | Balance: Rs.{self.__balance:.2f}")

if __name__ == "__main__":
    print("=== Bank Account Management System (OOP) ===")
    acc = BankAccount("AC78910452", "Niranjan P G", 5000.0)
    acc.display()
    acc.deposit(2500.0)
    acc.withdraw(1200.0)
    acc.withdraw(8000.0)
    acc.display()
