secret_number = 42

num_of_guesses = 1

# Read in user's guess as an integer
user_guess = int(input("Please enter a number: "))

MAX_GUESSES = 5

def get_int(prompt: str) -> int:
    """Prompt until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def play_game() -> bool:
    """Play the number-guessing game. Returns True if guessed correctly."""
    num_of_guesses = 0
    while num_of_guesses < MAX_GUESSES:
        user_guess = get_int("Please enter a number: ")
        num_of_guesses += 1
        if user_guess == secret_number:
            print("Correct")
            return True
        else:
            print("Incorrect.")

    print("Incorrect. Game over.")
    return False

if __name__ == "__main__":
    play_game()

