class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    def display_balance(self):
        print(f"Account balance for {self.__account_holder_name} (Account #{self.__account_number}): ₹{self.__account_balance}")


# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    my_account = BankAccount(account_number="12345", account_holder_name="ruban", initial_balance=1000.0)

    # Test deposit and withdrawal
    my_account.display_balance()
    my_account.deposit(500.0)
    my_account.withdraw(200.0)
    my_account.display_balance()

