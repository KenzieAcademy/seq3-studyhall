"""
Tower of Hanoi game.
"""

import os
from itertools import zip_longest

towers = [[3, 2, 1], [], []]
total_moves = 0
errors = []
ERROR_TOWER_NUMBER = 'Invalid tower number. Try again.'
ERROR_TOWER_EXIST = 'Cannot move from empty tower. Try again.'
ERROR_TOWER_RULE = 'Cannot place larger disk onto smaller disk. Try again.'


def print_towers():
    """Display the current representation of the towers."""
    print_tower1 = towers[0][::]
    print_tower1.extend([' '] * (3 - len(towers[0])))
    print_tower2 = towers[1][::]
    print_tower2.extend([' '] * (3 - len(towers[1])))
    print_tower3 = towers[2][::]
    print_tower3.extend([' '] * (3 - len(towers[2])))
    for a, b, c in zip_longest(print_tower1[::-1],
                               print_tower2[::-1],
                               print_tower3[::-1]):
        print(a, b, c)
    print('- - -')
    print('1 2 3')


def does_tower_exist(tower):
    """Returns whether the tower number exists."""
    return tower in range(1, len(towers)+1)


def is_tower_empty(tower):
    """Returns whether the tower is empty."""
    return not bool(len(towers[tower-1]))


def move_disk(from_tower, to_tower):
    """Moves a disk from one tower to another."""
    global total_moves
    from_tower -= 1
    to_tower -= 1
    # larger disk cannot go on top of a smaller one
    if len(towers[to_tower]):
        disk = towers[from_tower][-1]
        dest_top = towers[to_tower][-1]
        if disk > dest_top:
            # player tried to move a larger disk onto a smaller one
            errors.append(ERROR_TOWER_RULE)
            return False

    # move disk
    disk = towers[from_tower].pop()
    towers[to_tower].append(disk)
    total_moves += 1
    return True


def main():
    """Main game loop."""
    global has_error

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Total Moves: {total_moves}\n')
        print_towers()
        if towers[2] == [3, 2, 1]:
            # player has won the game
            break
        if errors:
            print(f'\n{errors.pop()}')
        errors.clear()
        choice_from = int(input('\nFrom tower: '))
        if not does_tower_exist(choice_from):
            errors.append(ERROR_TOWER_NUMBER)
            continue
        elif is_tower_empty(choice_from):
            errors.append(ERROR_TOWER_EXIST)
            continue
        choice_to = int(input('To tower: '))
        if not does_tower_exist(choice_to):
            errors.append(ERROR_TOWER_NUMBER)
            continue
        success = move_disk(choice_from, choice_to)
        if not success:
            continue

    print("\nCongratulations! You are a tower master!")


if __name__ == '__main__':
    main()
