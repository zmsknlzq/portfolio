# This module is only useful in case the program is launched by double click instead of terminal command, because it
# allows for setting the optional arguments that cannot be set otherwise.

def option_setters(min_length: int, max_length: int, difficulty_level: str) -> (int, int, bool, str, bool):
    """
    Data-types of the returned tuple: (int, int, bool, str, bool)
    This function returns settings for the following options:
    - minimum word length (6 <= int <= 18)
    - maximum word length (minimum word length <= int <= 18)
    - help consultation (bool)
    - difficulty setting ('1' or '2' or '3' as str)
    - high-score visualization (bool)
    """
    # confirming or changing minimum word length
    is_ml_confirmed = input(f'Current minimum word length is {min_length}.\n'
                            f'Please type "O/o" or "Y/y" to confirm or another key to change the '
                            f'minimum length, then press Enter to continue: ')
    if is_ml_confirmed.lower() != 'o' and is_ml_confirmed.lower() != 'y':
        new_ml_set = False
        while not new_ml_set:
            try:
                new_min_length = int(input('Type in a number between 6 and 18 (both included) to set a new minimum '
                                           'length, then press Enter to continue: '))
                if 6 <= new_min_length <= 18:
                    new_ml_set = True
                else:
                    print('Sorry, you need to enter a number between 6 and 18, both included.')
            except ValueError as exception:
                print('Sorry, you need to enter a number.')
    else:
        new_min_length = min_length

    # confirming or changing maximum word length
    is_maxlen_confirmed = input(f'Current minimum word length is {new_min_length} and maximum word length is '
                                f'{max_length}.\nPlease type "O/o" or "Y/y" to confirm or another key to change the '
                                f'maximum length, then press Enter to continue: ')
    if is_maxlen_confirmed.lower() != 'o' and is_maxlen_confirmed.lower() != 'y':
        new_maxlen_set = False
        while not new_maxlen_set:
            try:
                new_max_length = int(input(f'Type in a number between {new_min_length} and 18 (both included) to set a'
                                           f'new maximum length, then press Enter to continue: '))
                if new_min_length <= new_max_length <= 18:
                    new_maxlen_set = True
                else:
                    print(f'Sorry, you need to enter a number between {new_min_length} and 18, both included.')
            except ValueError as exception:
                print('Sorry, you need to enter a number.')
    else:
        new_max_length = max_length

    # confirming or changing the game's difficulty
    is_difficulty_confirmed = input(f'Current difficulty is {difficulty_level}/3.\n'
                                    f'Please type "O/o" or "Y/y" to confirm or another key to change the '
                                    f'difficulty, then press Enter to continue: ')
    if is_difficulty_confirmed.lower() != 'o' and is_difficulty_confirmed.lower() != 'y':
        new_difficulty_set = False
        while not new_difficulty_set:
            try:
                new_difficulty = input(f'Type in an integer number between 1 (easy) and 3 (hard) (both included) to set'
                                       f' a new level of difficulty, then press Enter to continue: ')
                if new_difficulty in ['1', '2', '3']:
                    new_difficulty_set = True
                else:
                    print(f'Sorry, you need to enter a number between 1 (easy) and 3 (hard) (both included).')
            except ValueError as exception:
                print('Sorry, you need to enter a number between 1 (easy) and 3 (hard) (both included).')
    else:
        new_difficulty = difficulty_level

    # asking if user wants to see the high score
    want_to_see_hs = input('Do you want to see the high score? Please type "O/o" or "Y/y" if yes or another key if no,'
                           ' then press Enter to continue: ')
    if want_to_see_hs.lower() != 'o' and want_to_see_hs.lower() != 'y':
        want_to_see_hs = False
    else:
        want_to_see_hs = True

    # asking if user wants to see the help
    want_to_see_help = input(
        'Do you want to see the help? Please type "O/o" or "Y/y" if yes or another key if no, '
        'then press Enter to continue: ')
    if want_to_see_help.lower() != 'o' and want_to_see_help.lower() != 'y':
        want_to_see_help = False
    else:
        want_to_see_help = True

    return new_min_length, new_max_length, want_to_see_hs, new_difficulty, want_to_see_help