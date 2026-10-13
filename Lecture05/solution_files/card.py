"""Exercise 7: the script, fixed so that flake8 reports nothing."""

value = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
for number in range(2, 11):
    value[number] = number
suit = {0: 'Spades', 1: 'Hearts', 2: 'Diamonds', 3: 'Clubs'}


def the_name_of_your_card(v, s=0, *args, **kwargs):
    """Name of card as a string."""
    if v < 1 or v > 13 or s not in (0, 1, 2, 3):
        raise ValueError
    return ("I have read your mind and predict your card is the "
            f"{value[v]} of {suit[s]}.")


print(the_name_of_your_card(2, s=3))
