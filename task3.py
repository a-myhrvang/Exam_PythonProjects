from colorama import Fore, Style

class BankAccount:
    def __init__(self):
        self.balance = 0.0
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(Fore.GREEN + f"Deposited: ${amount:.2f}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Deposit amount must be positive." + Style.RESET_ALL)
            
    def withdraw(self, amount):
        if amount <= 0:
            print(Fore.RED + "Withdrawal amaount must be positive." + Style.RESET_ALL)
        elif amount > self.balance:
            print(Fore.RED + "Insufficient funds." + Style.RESET_ALL)
        else:
            self.balance -= amount
            print(Fore.GREEN + f"Withdrew: ${amount:.2f}" + Style.RESET_ALL)
            
    def add_interest(self, rate):
        interest = self.balance * rate
        self.balance += interest
        print(Fore.GREEN + f"Interest added: ${interest:.2f}" + Style.RESET_ALL)
            
    def get_balance(self):
        return self.balance
    
    
class Menu:
    def __init__(self):
        self.options = [
            "Open a new account",
            "Deposit money into your account",
            "Withdraw money from your account",
            "Add interests to your account",
            "Get the current balance of your account",
            "Quit"
            ]
        
    def add_option(self, option_text):
        self.options.append(option_text)
        
    def get_input(self):
        # Displays the menu and validates user input
        print("\n –––| Bank Menu |–––\n")
        for idx, option in enumerate(self.options, start=1):
            print(f"{idx}. {option}")
        while True:
            try:
                choice = int(input("\nEnter your choice: "))
                if 1 <= choice <= len(self.options):
                    return choice
                else:
                    print(Fore.RED + "Invalid option. Please try again." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Please enter a valid number. " + Style.RESET_ALL)
            
            
def main():
    print("\nWelcome to the Bank Account Management System\n")
    menu = Menu()
    account = None
    # Main loop to interact with the banking sytem
    while True:
        choice = menu.get_input()
        
        if choice == 1:
            if account is None:
                account = BankAccount()
                print(Fore.GREEN + "New account created." + Style.RESET_ALL)
            else:
                print(Fore.CYAN + "Account already exists." + Style.RESET_ALL)
                
        elif choice == 2:
            if account:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
            else:
                print(Fore.CYAN + "No account found. Please open an account first." + Style.RESET_ALL)
                
        elif choice == 3:
            if account:
                try: 
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except:
                    print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
            else:
                print(Fore.CYAN + "No account found. Please open an account first." + Style.RESET_ALL)
                
        elif choice == 4:
            if account:
                try:
                    rate = float(input("Enter interest rate (e.g., 0.05 for 5%): "))
                    account.add_interest(rate)
                except ValueError:
                        print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
            else:
                print(Fore.CYAN + "No account found. Please open an account first." + Style.RESET_ALL)
                
        elif choice == 5:
            if account:
                print(f"Current balance: ${account.get_balance():.2f}")
            else:
                print(Fore.CYAN + "No account found. Please open an account first." + Style.RESET_ALL)
                
        elif choice == 6:
            print("\nThank you for using the Bank Account Management System.")
            break
        
if __name__ == "__main__":
    main()