import random

def load_words(filename):
        # Loads a word from a file and returns a list.
        with open(filename, "r") as file:
            words = file.read().split()
        return words
    
def choose_word(words):
    # Chooses a random word from the list.
    return random.choice(words).lower()

def play_game():
    try:
        words = load_words("words.txt")
    except FileNotFoundError:
        print("Error: 'words.txt' not found. Please make sure the file exists.")
        return
    word = choose_word(words)
    word_length = len(word)
    guesses_left = word_length
    guessed_word = ["_"] * word_length
    guesses_letters = set()
    quit_flag = False
    
    print("\n –––| Word Guessing Game |–––\n")
    print(f"The word you need to guess has '{word_length}' characters.")
    print(f"You now have '{guesses_left}' guesses.\n")
    print(" ".join(guessed_word))
    
    while guesses_left > 0 and "_" in guessed_word:
        print("\n+––––––––––––––––––––––––––+")
        guess = input("\nGuess a character (or type 'quit' to exit): ").lower()
        
        # Let´s the user quit the game
        if guess == "quit":
            print("\nYou chose to quit the game.")
            print(f'The word was ––> "{word}"')
            quit_flag = True
            break
        
        # Check that input is only a-z and not full words or numbers
        if len(guess) != 1:
            print("Please enter exactly one character.")
            print()
            continue
        elif not guess.isalpha() or not guess.isascii():
            print("Only letters A-Z are allowed. No numbers or characters.")
            print()
            continue
        
        # Check if the character has aldready been guesses before
        if guess in guesses_letters:
            print("You already guessed that letter.")
            print()
            continue
        
        guesses_letters.add(guess)
        print()
        
        if guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("Sorry, that letter is not in the word.")
            print()
            guesses_left -= 1
            
        print(" ".join(guessed_word))
        print(f"\nYou have {guesses_left} guess(es) left.")
        print("Guessed letters so far:", ", ".join(sorted(guesses_letters)))        
    print("\n+––––––––––––––––––––––––––+")
    
    if quit_flag:
        pass # If user quit the game, skip the rest
    elif "_" not in guessed_word:
        print(f'You found the word ––> "{word}"')
        print("Congratulations! You won!")
    else:
        print("You ran out of guesses.")
        print(f'The word is ––> "{word}"')
        print("Better luck next time!")
        
# Run the game
if __name__ == "__main__":
    play_game()