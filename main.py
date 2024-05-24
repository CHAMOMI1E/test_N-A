from src.atm import ATM

if __name__ == '__main__':
    atm = ATM()

    atm.deposit([0, 0, 1, 2, 1])
    atm.deposit([0, 0, 1, 2, 1, 2])  # error
    atm.deposit(0)  # error
    atm.withdraw(600)  # [0, 0, 1, 0, 1]
    atm.deposit([0, 1, 0, 1, 1])
    atm.withdraw(600)  # [-1]
    atm.withdraw(550)  # [0, 1, 0, 0, 1]
