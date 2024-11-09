def set_lives_number(difficulty: str, singular_letters_in_word_to_guess: int) -> int:
    """
    Returns the maximum number of lives (rounds of letter guessing) as an integer.
    Sets the number of lives based on the arg -d, --difficulty, which can be 1, 2, or 3 (as a string).
    If the difficulty arg is not declared, the program defaults to 2, i.e., medium (or 'normal') difficulty.
    The FORMULA changes based on that arg:
    1 is EASY, i.e., number of lives = number of singular letters in word to guess multiplied by 200%
    2 is MEDIUM, i.e., number of lives = number of singular letters in word to guess multiplied by 150%
    3 is HARD, i.e., number of lives = number of singular letters in word to guess
    Note that the results of the calculations are rounded to the nearest integer.
    """
    if difficulty == '1':
        lives = round(singular_letters_in_word_to_guess * 2)
        print(f'Difficulty set to easy: you have {lives} guesses before being hanged. '
              f'To learn how the number of lives is determined, please take a look at the help.')
        return lives
    elif difficulty == '3':
        lives = round(singular_letters_in_word_to_guess)
        print(f'Difficulty set to hard: you have {lives} guesses before being hanged. '
              f'To learn how the number of lives is determined, please take a look at the help.')
        return lives
    else:
        lives = round(singular_letters_in_word_to_guess * 1.5)
        print(f'Difficulty set to normal: you have {lives} guesses before being hanged. '
              f'To learn how the number of lives is determined, please take a look at the help.')
        return lives