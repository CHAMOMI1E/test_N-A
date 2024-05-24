from src.atm import ATM

if __name__ == '__main__':
    obj = ATM()

    obj.deposit([1, 2, 3, 4, 5, 6])

    obj.deposit([1, 2, 3, 4, 5])
    obj.deposit([1, 2, 3, 4, 5])


