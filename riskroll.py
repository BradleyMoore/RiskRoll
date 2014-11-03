from app.RollDice import roll


def get_number_of_combatants():
    """Take no input and return tuple of ints."""
    num_of_attackers = [1,2,3]
    num_of_defenders = [1,2]
    attackers = 0
    defenders = 0

    while attackers not in num_of_attackers:
        attackers = int(raw_input('How many attackers? [1,2,3]\n>'))
    while defenders not in num_of_defenders:
        defenders = int(raw_input('How many defenders? [1,2]\n>'))

    return (attachers, defenders)


def fight(combatants):
    """Input tuple of ints and return tuple of ints."""
    attackers = combatants[0]
    defenders = combatants[1]




def devine_winner(attack_roll, defend_roll):
    """Take two lists of ints and return tuple."""
    pass


def restart():
    """Determine if another go is needed."""
    pass


if __name__ == '__main__':
    pass

