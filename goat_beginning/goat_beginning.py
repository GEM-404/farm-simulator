import sys

from random import choice


def get_goats_at_beginning() -> int:
    goat_number = 300

    if len(sys.argv) > 1:
        goat_number = sys.argv[1]
        if goat_number.isnumeric():
            goat_number = int(goat_number)
        else:
            goat_number = 300

    return goat_number


def goat_dict_populator(goat_number: int) -> \
        tuple[dict[str, str], dict[str, str]]:
    """We will assign goat_ids from the goat_number given"""

    values: tuple[str, str] = ("M", "F")
    goat_age_max: int = 10

    goat_id_and_age: dict[str, str] = {}
    goat_id_and_gender: dict[str, str] = {}

    for goat in range(1, goat_number):
        goat_id_and_age[f"{goat}"] = choice([str(goat_age)
                                            for goat_age in
                                            range(1, goat_age_max)])

        goat_id_and_gender[f"{goat}"] = choice(values)

    return (goat_id_and_age, goat_id_and_gender)
