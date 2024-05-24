from typing import List


def banknotes_validation(banknotesCount: List[int]):
    if type(banknotesCount) == list and len(banknotesCount) == 5:
        return banknotesCount
    else:
        return 0
