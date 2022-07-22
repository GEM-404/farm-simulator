
import sys
sys.path.insert(0, '/home/masha/farm_simulator/goat_beginning')

from goat_beginning import goat_dict_populator
from goat_beginning import get_goats_at_beginning

GOAT_NUMBER = get_goats_at_beginning()

MAX_FEM_REPRODUCTION_AGE = 7
MIN_FEM_REPRODUCTION_AGE = 3

MAX_MALE_REPRODUCTION_AGE = 8
MIN_MALE_REPRODUCTION_AGE = 2

GOAT_GENDER_DICT = goat_dict_populator(GOAT_NUMBER)[1]
GOAT_AGE_DICT = goat_dict_populator(GOAT_NUMBER)[0]


def female_goats() -> dict:
    return {key: GOAT_AGE_DICT[key] for key
            in GOAT_GENDER_DICT.keys()
            if GOAT_GENDER_DICT[key] == 'F'}


def male_goats() -> dict:
    return {key: GOAT_AGE_DICT[key] for key
            in GOAT_GENDER_DICT.keys()
            if GOAT_GENDER_DICT[key] == 'M'}


def female_that_can_reproduce() -> int:
    fem_goats = female_goats()

    reproductive_fem_goats = {key: fem_goats[key] for key
                              in fem_goats.keys()
                              if
                              int(fem_goats[key]) > MIN_FEM_REPRODUCTION_AGE
                              and
                              int(fem_goats[key]) < MAX_FEM_REPRODUCTION_AGE}

    return len(reproductive_fem_goats)


def male_that_can_reproduce() -> int:
    he_goats = male_goats()

    reproductive_male_goats = {key: he_goats[key] for key
                               in he_goats.keys()
                               if
                               int(he_goats[key]) > MIN_MALE_REPRODUCTION_AGE
                               and
                               int(he_goats[key]) < MAX_MALE_REPRODUCTION_AGE}

    return len(reproductive_male_goats)


def main():
    # Please, refactor this code, there is a lot of code repetition.
    print(f"{female_that_can_reproduce()=}")
    print(f"{male_that_can_reproduce()=}")


if __name__ == '__main__':
    main()
