import random


def roll_dice():
    print('You rolled: ', random.randint(1, 6))


def options():
    a = input('Play or quit the game:\n\nPres p for play or q to exit the game: \n')
    if a == 'p':
        roll_dice()
        options()
    else:
        exit()


if __name__ == '__main__':
    options()
