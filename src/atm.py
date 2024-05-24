from typing import List

from src.validation import validation_banknotes


class ATM:
    def __init__(self):
        self.denominations = [10, 50, 100, 200, 500]
        self.__banknotes: List[int] = [0, 0, 0, 0, 0]

    def deposit(self, banknotes_count: List[int]) -> None:
        banknotes_count = validation_banknotes(banknotes_count)
        if banknotes_count:
            for banknote in range(len(self.__banknotes)):
                self.__banknotes[banknote] += banknotes_count[banknote]
        else:
            return print("Неправильно введены значения, проверьте их!")

    def withdraw(self, amount: int) -> None:
        temp_banknotes = self.__banknotes[:]
        result = [0] * len(self.denominations)

        for i in range(len(self.denominations)-1, -1, -1):
            denomination = self.denominations[i]
            if amount == 0:
                break
            if denomination <= amount and temp_banknotes[i] > 0:
                count = min(amount // denomination, temp_banknotes[i])
                result[i] = count
                amount -= denomination * count

        if amount == 0:
            for i in range(len(self.denominations)):
                self.__banknotes[i] -= result[i]
            print(result)
        else:
            print([-1])

    def __str__(self):
        return f"На данный момент в банкомате осталось: {self.__banknotes}"