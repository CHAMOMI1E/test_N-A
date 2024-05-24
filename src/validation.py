from typing import List


def validation_banknotes(banknotes_count: List[int]):
    try:
        if len(banknotes_count) == 5 and all(isinstance(i, int) and i >= 0 for i in banknotes_count):
            return banknotes_count
        else:
            return 0
    except TypeError:
        return 0
