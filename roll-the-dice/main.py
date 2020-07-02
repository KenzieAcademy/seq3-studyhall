"""
Roll some dice and try to be the one with
the highest rolls!
"""

import random

num_players = 2  # TODO: make this dynamic (command line arguments?)
num_dice = 2     # TODO: make this dynamic (command line arguments?)
num_sides = 6    # TODO: make this dynamic (command line arguments?)
num_times = 5    # TODO: make this dynamic (command line arguments?)
dice_rolls = []  # TODO: revisit, maybe use a dictionary


def main():
    # roll the dice
    for n in range(num_times):
        rolls = []
        for player in range(num_players):
            total = 0
            for i in range(num_dice):
                total += random.randint(1, num_sides)
            # store dice rolls
            rolls.append(total)
            print(f'Player {player+1}: {total}')
        dice_rolls.append(rolls)

    # see who had the highest roll each round
    tally = [0, 0]  # TODO: revisit this - is it the right structure to use?
    while dice_rolls:
        round_rolls = dice_rolls.pop(0)
        # compare dice rolls
        if round_rolls[0] > round_rolls[1]:
            # player1 wins this round
            tally[0] += 1
        elif round_rolls[0] < round_rolls[1]:
            # player2 wins this round
            tally[1] += 1
        else:
            # it's a tie!
            # TODO: re-roll the dice!
            pass

    # show results
    print("*" * 25)
    print("Results:")
    print(f"Player 1: {tally[0]}, Player 2: {tally[1]}")

    # declare a winner
    if tally[0] > tally[1]:
        # player 1 is the winner!
        print('Player 1 wins!')
    elif tally[0] < tally[1]:
        # player 2 is the winner!
        print('Player 2 wins!')
    else:
        # it's a tie
        print("It's a sad day...nobody won!")
    print("*" * 25)


if __name__ == '__main__':
    main()
