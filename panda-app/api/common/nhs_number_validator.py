import re

from api.common.consts import NHS_NUMBER_REGEX


STARTING_WEIGHTING_FACTOR = 10
NHS_NUMBER_DIVISOR = 11

def validate_nhs_number(nhs_number: str) -> bool:
    if not _basic_validation(nhs_number):
        return False

    return _validate_checksum(nhs_number)


def _basic_validation(nhs_number: str) -> bool:
    nhs_number_pattern = re.compile(NHS_NUMBER_REGEX)
    return nhs_number_pattern.match(nhs_number) is not None

def _validate_checksum(nhs_number: str) -> bool:
    total_weighting = 0

    for i in range(len(nhs_number) - 1):
        weighting_factor = STARTING_WEIGHTING_FACTOR - i
        total_weighting += int(nhs_number[i]) * weighting_factor

    remainder = total_weighting % NHS_NUMBER_DIVISOR

    if remainder == 1:
        return False

    if remainder == 0:
        remainder = 11

    check_number = NHS_NUMBER_DIVISOR - remainder

    return check_number == int(nhs_number[-1])
