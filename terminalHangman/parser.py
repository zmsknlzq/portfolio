import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Terminal Hangman - (c) 2024 Stefano Giovannini")
    parser.add_argument("-m", "--min", help="set MINIMUM word length (between 6 and 18)", type=int)
    parser.add_argument("-M", "--max", help="set MAXIMUM word length (between 6 and 18)", type=int)
    parser.add_argument("-H", "--high", help="show high-score", action='store_true') # no values needed
    parser.add_argument("-d", "--difficulty",
                        help="""
                        set DIFFICULTY 1 easy, 3 hard; defaults to 2 medium The default difficulty is set to 'medium', 
                        i.e., the player lives (max num of rounds before game-over) equals 150 percent of
                        the number of singular letters (SLs) in that word (rounded to nearest int).
                        E.g., if the word is "misanthropically", which contains 13 different letters, the number of 
                        rounds to guess the words will be set to 19 at most. If the difficulty is set to 'easy',
                        lives equal 200 percent of the word's SLs; if it is set to 'hard', it equals SLs.
                        """
                        )
    return parser