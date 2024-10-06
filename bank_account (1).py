class BankAccount:
    # Class variable
    interest_rate = 0.05  # 5% interest rate

    def __init__(self, account_holder):
        # Instance variables
        self.account_holder = account_holder
        self.balance = 0.0  # Initial balance set to zero

    def deposit(self, amount):
        """Add the deposit amount to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Subtract the withdrawal amount from the balance if funds are sufficient."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} from {self.account_holder}'s account.")
            else:
                print(f"Insufficient funds for withdrawal from {self.account_holder}'s account.")
        else:
            print("Withdrawal amount must be positive.")

    def apply_interest(self):
        """Apply interest to the current balance based on the interest rate."""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Applied {BankAccount.interest_rate * 100}% interest  to {self.account_holder}'s account.")

    def display_account_info(self):
        """Display the account holder's name and the current balance."""
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance:.2f}")


account1 = BankAccount("Moreen")
account2 = BankAccount("Enock")


account1.deposit(50000)
account1.withdraw(1000)
account1.deposit(6000)
account2.deposit(10000)
account2.withdraw(30000)

# 3. Apply interest using the apply_interest() method.
account1.apply_interest()
account2.apply_interest()

# 4. Display account information for each account.
account1.display_account_info()
account2.display_account_info()
