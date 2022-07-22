
"""
We expect goats that have passed their age_limit
of 10 years to either die or get eaten.
"""

import sys
import time

sys.path.insert(0, '/home/masha/farm_simulator/goat_beginning/')

from goat_beginning import goat_dict_populator
from goat_beginning import get_goats_at_beginning


GOAT_MAX_LIFE: int = 10
GOAT_NUMBER = get_goats_at_beginning()
GOAT_DICT: dict[str, str] = goat_dict_populator(GOAT_NUMBER)[0]


def get_goat_max_life(goat_id: str) -> bool:
    """Returns whether a goat has lived his life fully"""

    goat_id_and_age: dict[str, str] = GOAT_DICT

    return int(goat_id_and_age[goat_id]) > GOAT_MAX_LIFE


def goats_left() -> int:
    return len(GOAT_DICT)


def goats_continue_living(GOAT_NUMBER: int) -> bool:

    if GOAT_NUMBER < 2:
        return False

    return True


def goat_start_living() -> float:
    """We want a second in our lives to be a second in a goat's life as well"""
    goat_life_start: float = time.time()
    goat_life_end: float = time.time()

    farmer_sustained: bool = goats_continue_living(GOAT_NUMBER)

    while farmer_sustained:
        continue

    return goat_life_end - goat_life_start


def goat_death(goat_id: str) -> None:
    """Gets eaten or dies from old age, anyhow, he is out of goat_dict"""

    del GOAT_DICT[goat_id]


def goat_killing_or_eating() -> None:
    """If a goat has maxed out his/her life, he either dies or gets eaten"""

    # We'll be going through the whole dict taking out goats that
    # have maxed out on their lives or eating them at will.
    # If no goat has maxed out on his life, eat one at will.

    for goat_id in range(1, GOAT_NUMBER):
        if int(GOAT_DICT[str(goat_id)]) > GOAT_MAX_LIFE:
            goat_death(str(goat_id))

    pass


def main():
    for goat in range(1, GOAT_NUMBER):
        print(get_goat_max_life(str(goat)))


if __name__ == '__main__':
    main()
