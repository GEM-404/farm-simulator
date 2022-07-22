
"""
A goat farm-simulator to see how many days  a 100 goats
can sustain a farmer if he eats a goat every 2 months.
"""

from goat_beginning.goat_beginning import goat_dict_populator
from goat_beginning.goat_beginning import get_goats_at_beginning


GOAT_NUMBER: int = get_goats_at_beginning()


def goat_definer(goat_number: int) -> tuple[dict[str, str], dict[str, str]]:
    """
    Returns a goat dictionary with all the goats in the farm
    with, goat_id as key, and their age as value
    """
    goat_id_and_age: dict[str, str] = goat_dict_populator(goat_number)[0]
    goat_id_and_gender: dict[str, str] = goat_dict_populator(goat_number)[1]

    return (goat_id_and_age, goat_id_and_gender)


def some_goat_stats(goat_number: int) -> int:
    """
    Returns number of days that a given number of goats
    can sustain the farmer
    """
    # incorporate some logic here...
    days: int = 1_000 * goat_number

    return days


def main():

    days = some_goat_stats(GOAT_NUMBER)
    print(days)


if __name__ == '__main__':
    main()
