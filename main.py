from modules.utilities import get_user_input, display_message, generate_random_value
from modules.logic_handler import evaluate_guess


def main():
    target_value = generate_random_value(1, 100)
    user_guess = None
    nr_of_guesses = 0
    display_message("Guess the number between 1 and 100")

    while user_guess!= target_value:
        try:
            nr_of_guesses += 1 
            user_guess = int(get_user_input("Enter your guess: "))
            result = evaluate_guess(target_value, user_guess)
            display_message(result)

        except ValueError:
            display_message("Please enter a number")


    display_message(f"You guessed the number in {nr_of_guesses} guesses!")            



if __name__ == "__main__":
    main()
