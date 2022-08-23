class BankAccount:

    def __init__(self, user, account_number):
        self.user = user
        self.account_number = account_number
        self.balance = 0

    def deposit_money(self):
        amount = int(input("Enter the amount to deposit: "))
        self.balance += amount
        print("Available balance: {}".format(self.balance))

    def withdraw_money(self):
        amount = int(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("You do not have sufficient fund")
        else:
            self.balance -= amount
            print("Available balance: {}".format(self.balance))

customer_1 = BankAccount("John Doe", "123456")
customer_1.deposit_money()
customer_1.withdraw_money()