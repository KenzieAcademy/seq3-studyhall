"""
A Dad Joke Wheel of Fortune-style Game!
"""

import os
import re
import sys
import requests

# game settings
joke_request_attempts = 3
guessed_letters = []
wrong_letters = []
INITIAL_GUESSES = 5
guesses_remaining = INITIAL_GUESSES
score = 0

# in-game messages
thanks = "Thanks for playing!"


def get_joke():
    headers = {'accept': 'application/json'}
    for _ in range(joke_request_attempts):
        response = requests.get('https://icanhazdadjoke.com/', headers=headers)
        data = response.json()
        text = data['joke']

        # restrict joke format from API response to a
        # joke sentence followed by a punchline sentence
        joke_match = re.search(r'(.+[.?!])(.+[.?!])', text)
        if joke_match:
            joke = joke_match.group(1).strip()
            punchline = joke_match.group(2).strip()
            return joke, punchline

    print('Did not find a well-formatted joke within API limits.')
    sys.exit(1)


def update_blanks(punchline):
    display = []
    for char in punchline.lower():
        if not char.isalpha() or char in guessed_letters:
            display.append(char)
        else:
            display.append('_')
    display[0] = display[0].upper()
    return ' '.join(display)


def continue_game(msg):
    """Asks the user if they would like to play more."""
    choice = input(msg)
    if choice not in ('y', 'n'):
        continue_game(msg)
    return True if choice == 'y' else False


def init(lost=False):
    """Initialize all game settings."""
    global guesses_remaining, score
    guesses_remaining = INITIAL_GUESSES
    if lost:
        score = 0
    guessed_letters.clear()
    wrong_letters.clear()


def main():
    global guesses_remaining, score
    init()
    joke, punchline = get_joke()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{joke}")
        unguessed = update_blanks(punchline)
        if '_' not in unguessed:
            print(punchline)

            # give the player their points and display them
            score += (100 // INITIAL_GUESSES) * guesses_remaining
            print(f'\nYour score: {score}')

            will_continue = continue_game('Continue? ')
            if will_continue:
                # re-initialize game
                init()
                # get a new joke
                joke, punchline = get_joke()
                continue
            else:
                print(thanks)
                break
        print(unguessed)
        print(f"\nGuesses remaining: {guesses_remaining}\n")
        print(f"Wrong guesses: {' '.join(wrong_letters)}")
        guess = input("Guess a letter: ").lower()
        if guess not in punchline:
            wrong_letters.append(guess)
            if guess not in guessed_letters:
                guesses_remaining -= 1
        if guess not in guessed_letters:
            guessed_letters.append(guess)
        if not guesses_remaining:
            print('Game over.')
            start_new_game = continue_game('New game? ')
            if start_new_game:
                # re-initialize game
                init(lost=True)
                # get a new joke
                joke, punchline = get_joke()
            else:
                print(thanks)
                break


if __name__ == '__main__':
    main()
