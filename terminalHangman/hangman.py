# (c) 2024 Stefano Giovannini

import os
from parser import create_parser
import random
from game_over import game_over_graphics, victory_graphics, title
from score import high_score, show_high_score, double_click_loaded_high_score
from difficulty import set_lives_number
from option_setters import option_setters

def main():
    abs_path = os.path.dirname(os.path.realpath(__file__)) + '\\'

    # parse command line and set options according to args values
    parser = create_parser()
    args = parser.parse_args()
    min_length = 6 if not args.min else args.min if args.max <= args.min and 6 <= args.min <= 18 else 6
    max_length = 18 if not args.max else args.max if args.max >= args.min and 6 <= args.max <= 18 else 18
    if args.high:
        show_high_score(abs_path=abs_path)
    if args.difficulty:
        if args.difficulty == '1':
            difficulty = '1'
        elif args.difficulty == '3':
            difficulty = '3'
        else:
            difficulty = '2'
    else:
        difficulty = '2'

    title()
    # add inputs for settings' confirmation since the game could have been launched by double click
    options_final_values = option_setters(min_length=min_length, max_length=max_length, difficulty_level=difficulty)
    if options_final_values[4]:
        print(
            """
            Terminal Hangman - (c) 2024 Stefano Giovannini - drgiovannini.com

                HELP:
                    MINIMUM word length (between 6 and 18
                    MAXIMUM word length (between 6 and 18)
                    choose if to show high-score
                    DIFFICULTY 1 easy, 3 hard; defaults to 2, medium.
                    The default difficulty is set to 'medium', i.e., the player lives 
                    (max num of rounds before game-over) equals 150 percent of
                    the number of singular letters (SLs) in that word (rounded to nearest int).
                    E.g., if the word is "misanthropically", which contains 13 different letters,   
                    the number of rounds to guess the words will be set to 19 at most.
                    If the difficulty is set to 'easy', lives equal 200 percent of the word's SLs;
                    if it is set to 'hard', it equals SLs.
                    
                Enjoy!
            """
        )
    if options_final_values[2]:
        db_hs = double_click_loaded_high_score(abs_path=abs_path)
        print(
            f"""
            Terminal Hangman - (c) 2024 Stefano Giovannini - drgiovannini.com

                HIGH SCORE: {db_hs}

                Good luck!
            """
        )

    min_length = options_final_values[0]
    max_length = options_final_values[1]
    difficulty = options_final_values[3] # 2 is bool for high score visualization, 4 is bool for help visualization

    # load English words
    with (open(file=f'{abs_path}words_alpha.txt', mode='r')
          as source):
        words = source.readlines()

    game_over = False
    while not game_over:
        word_chosen = False
        while not word_chosen:
            word_to_guess = random.choice(words).strip()
            if min_length <= len(word_to_guess) <= max_length:
                singular_letters_in_this_word = len(list(''.join(set(word_to_guess))))
                word_chosen = True

        print(f'\nThe word to be guessed is {len(word_to_guess)}-letter long.')
        lives = set_lives_number(difficulty=difficulty, singular_letters_in_word_to_guess=singular_letters_in_this_word)

        for letter in word_to_guess:
            print("_", end='')
        
        game_round = 0
        errors = 0
        partially_guessed_word = ''.join(['_' for letter in word_to_guess])
        will_be_hanged = True
        
        while game_round < lives:
            game_round += 1
            print(f'\nROUND {game_round}')
            guess = input('Type in a letter: ')
            if guess.lower() in word_to_guess.lower():
                store_guessed_letter_indices = []
                for index, letter in enumerate(word_to_guess):
                    if guess.lower() == letter.lower():
                        store_guessed_letter_indices.append(index)
                # update partially guessed word
                partially_guessed_word_as_list = list(partially_guessed_word)
                for index in store_guessed_letter_indices:
                    partially_guessed_word_as_list[index] = guess.lower()
                partially_guessed_word = ''.join(partially_guessed_word_as_list)
                print('Right on!')
                print(partially_guessed_word)
                if partially_guessed_word == word_to_guess:
                    will_be_hanged = False
                    print('YOU DID IT!')
                    print('Look at you running away with your life!')
                    victory_graphics()
                    your_score, original_score = high_score(
                        word_length=len(word_to_guess),
                        singular_letters=len(list(''.join(set(word_to_guess)))),
                        number_of_errors=errors,
                        abs_path=abs_path
                    )
                    print(f'Your score is {your_score}')
                    print(f'The original score was {original_score}')
                    print('Thanks for playing.')
                    break
                continue
            else:
                errors += 1
                print('Well, that\'s unfortunate...')
                print('TIC-TOC TIC-TOC TIC-TOC...')
        if will_be_hanged:
            game_over_graphics()
            print(f'The word to guess was: {word_to_guess}')
        new_game = input('NEW GAME (n) or EXIT (any other key)?')
        if new_game.lower() != 'n':
            break

if __name__ == '__main__':
    main()