class Bank_system:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0

    def login(self, username, password):
        return self.username == username and self.password == password

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Your new balance is ${self.balance}.")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn ${amount}. Your new balance is ${self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount for withdrawal.")

    def check_balance(self):
        print(f"Your current balance is ${self.balance}.")


def main():
    print("WELCOME")
    user_account = Bank_system("user123", "pass123")
    while True:
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")
        if user_account.login(username_input, password_input):
            print("Login successful.")
            break
        else:
            print("Invalid username or password.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            amount = float(input("Enter the amount to deposit: "))
            user_account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            user_account.withdraw(amount)
        elif choice == "3":
            user_account.check_balance()
        elif choice == "4":
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == '__main__':
    main()
