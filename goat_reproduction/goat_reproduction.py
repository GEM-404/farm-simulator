
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


def get_goat_gender(goat_age_dict: dict[str, str],
                    goat_gender_dict: dict[str, str],
                    gender: str) -> dict[str, str]:

    return {key: goat_age_dict[key] for key
            in goat_age_dict.keys()
            if goat_gender_dict[key] == gender}


def get_reproducible_goats(goat_dict: dict[str, str]) -> int:

    return len({key: goat_dict[key] for key
                in goat_dict.keys()
                if
                int(goat_dict[key]) > MIN_FEM_REPRODUCTION_AGE
                and
                int(goat_dict[key]) < MAX_FEM_REPRODUCTION_AGE})


def female_goats() -> dict:
    gender = 'F'
    return get_goat_gender(GOAT_AGE_DICT, GOAT_GENDER_DICT, gender=gender)


def male_goats() -> dict:
    gender = 'M'
    return get_goat_gender(GOAT_AGE_DICT, GOAT_GENDER_DICT, gender=gender)


def female_that_can_reproduce() -> int:
    return get_reproducible_goats(female_goats())


def male_that_can_reproduce() -> int:
    return get_reproducible_goats(male_goats())


def main():
    print(f"{female_that_can_reproduce()=}")
    print(f"{male_that_can_reproduce()=}")


if __name__ == '__main__':
    main()
