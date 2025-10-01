from colorama import Fore, Style

def is_palindrome(s):
    # Remove space and signs, and turn everything to small letters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if string is equal in reverse
    return cleaned == cleaned[::-1]

def main():
    print("\n –––| Palindrome Checker|–––")
    print("    (type 'quit' to exit)\n")
    
    # Counts palindrome checked
    count_checked = 0
    count_palindromes = 0
    
    # Main loop for user interaction. Validates and checks palindromes until 'quit'.
    while True:
        user_input = input("Enter a word to check: ")
        
        if user_input.lower() == "quit":
            print("Goodbye!")
            print(f"You checked {count_checked} word(s), {count_palindromes} were palindromes.")
            break
    
        # Check that userinput is not empty
        if not user_input.strip():
            print(Fore.RED + "Empty input. Please enter a valid word.\n" + Style.RESET_ALL)
            continue
        
        # Check that input is only a-z and not numbers
        if not any (char.isalpha() for char in user_input):
            print("Numbers are not allowed. Please enter a word (letters only).\n")
            continue
        
        count_checked += 1
    
        if is_palindrome(user_input):
            count_palindromes += 1
            print(Fore.GREEN + "YES " + Style.RESET_ALL + f'"{user_input}" is a palindrome.\n')
        else:
            print(Fore.RED + "NO " + Style.RESET_ALL + f'"{user_input}" is not a palindrome.\n')
        
if __name__ == "__main__":
    main()