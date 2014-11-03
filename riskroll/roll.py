from random import randint
from sys import argv, exit


def get_cl_args():
    """Call 2 cl arguments and return tuple."""
    try:
        int(argv[1])
        int(argv[2])
    except (ValueError, IndexError) as e:
        print 'Please type 2 command line integers.'
        exit()

    num_of_dice = argv[1]
    sides_per_die = argv[2]

    dice = (num_of_dice, sides_per_die)
    return dice


def roll_die(die):
    """Input int and return int."""
    roll = randint(1, int(die))

    return roll


def restart():
    """Determine whether to exit or not."""
    quit = raw_input('\nEnter to roll again, type exit to quit.\n>')
    if quit == 'exit':
        exit()
    elif quit == '':
        print '\n'
    else:
        print '\n'
        restart()


def main():
    """Do everything."""
    dice = get_cl_args()
    num_of_dice = dice[0]
    num_of_sides = dice[1]
 
    print '\n'

    while True:

        rolls = []
   
        for i in xrange(int(num_of_dice)):
            rolls.append(roll_die(int(num_of_sides)))

        for roll in rolls:
            print roll,

        restart()


if __name__ == '__main__':
    main()

