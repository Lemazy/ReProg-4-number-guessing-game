def evaluate_guess(target_value, user_guess):
    if user_guess < target_value:
        return "Too low"
    elif user_guess > target_value:
        return "Too high"
    else:
        return "Congradulations! You guessed it right!"
