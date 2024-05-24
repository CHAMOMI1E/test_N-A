from typing import List

from src.validation import banknotes_validation


class ATM:
    def __init__(self):
        self.__banknotes: List[int] = [0, 0, 0, 0, 0]

    # Сложность данной функции O(1), так как это простая операция присваивания в списке фиксированной длины
    def deposit(self, banknotes_count: List[int]):
        banknotes_count = banknotes_validation(banknotes_count)
        if banknotes_count:
            for banknote in range(len(self.__banknotes)):
                self.__banknotes[banknote] += banknotes_count[banknote]
            return print(self.__banknotes)
        else:
            return print(-1)

    def withdraw(self, amount: int):
        pass

    def __str__(self):
        return f"На данный момент в банкомате осталось: {self.__banknotes}"