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
    """Input tuple of ints and return tuple of lists of ints."""
    attackers = combatants[0]
    defenders = combatants[1]

    attack_rolls = []
    defence_rolls = []

    attack_rolls = roll.main(attackers, 6)
    defence_rolls = roll.main(defenders, 6)

    return (attack_rolls, defence_rolls)


def devine_winner(attack_rolls, defence_rolls):
    """Take two lists of ints and return tuple."""
    attackrolls.sort()
    defence_rolls.sort()

    attack_wins = 0
    attack_losses = 0
    defence_wins = 0
    defence_losses = 0

    for i in xrange(len(defence_rolls), 0, -1):
        if defence_rolls[i] >= attack_rolls[i]:
            defence_wins = defence_wins + 1
            attack_losses = attack_losses + 1
        else:
            attack_wins = attack_wins + 1
            defence_losses = defence_losses + 1


    attack_wl = (attack_wins,attack_losses)
    defence_wl = (defence_wins,defence_losses)
    
    return (attack_wl, defence_wl)


def restart():
    """Determine if another go is needed."""
    pass


if __name__ == '__main__':
    pass

