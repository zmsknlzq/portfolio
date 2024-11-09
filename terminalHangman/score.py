def high_score(word_length: int, singular_letters: int, number_of_errors: int, abs_path: str) -> (int, int):
    """Creates a new high_score.txt file if none is present,
    otherwise updates it if current score is higher than previous."""
    new_score = score_calculator(wl=word_length, sl=singular_letters, ne=number_of_errors)
    with open(file=f'{abs_path}high_score.txt', mode='r') as source:
        hs = source.read()
        hs = 0 if hs == '' else int(hs)
    if new_score > hs:
        print('GREAT! NEW HIGH SCORE!')
        with open(file=f'{abs_path}high_score.txt', mode='w') as source:
            source.write(str(new_score))
    return new_score, hs

def score_calculator(wl: int, sl: int, ne: int) -> int:
    """
    wl is the length of the word to guess,
    sl is the number of singular letters it contains,
    ne is the number of errors the user made
    -------------------------------------------------
    The rationale is the following:
    So, for example:
    the word to be guessed is "misanthropically".
    Word difficulty = word length * number of singular letters = 16 * 13 = 208
    Then, if there were any errors, I would decrease the score by multiplying the number of errors for the
    number of singular letters.
    Let's assume the user made three errors, the penalty would amount to 3*13, and the
    total score would be 208 - 39.
    The rationale is that longer words allow for higher scores while being more penalised.
    """
    score = wl * sl - ne * sl if ne != 0 else wl * sl
    return score

def show_high_score(abs_path: str) -> None:
    """
    If the arg -H, --high is passed at launch,
    at the beginning of the game the high score is printed.
    """
    try:
        with open(file=f'{abs_path}high_score.txt', mode='r') as source:
            hs = source.read()
            if hs != '':
                print(f'HIGH SCORE: {hs}')
            else:
                print('No high score found.')
    except FileNotFoundError as exception:
        print('No high score found.')

def double_click_loaded_high_score(abs_path: str) -> str:
    """
    If the game is launched by double click and the user
    wants to see the high score, this function is run.
    """
    try:
        with open(file=f'{abs_path}high_score.txt', mode='r') as source:
            hs = source.read()
            if hs != '':
                return hs
            else:
                return '0'
    except FileNotFoundError as exception:
        return '0'
