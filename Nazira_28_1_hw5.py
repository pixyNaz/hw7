import random
from decouple import config

def casino():
    money = config('MY_MONEY', cast=int)
    while True:
        win_slot = random.randint(1,31)
        slot = int(input('Выберите слот: '))
        if slot > 30:
            print('We have only 30 slots')
            continue
        bet = int(input('Сделайте ставку: '))
        if bet > money:
            print(f'you have not enough money. your balance {money}')
        if win_slot == slot:
            money += bet * 2
        else:
            money -= bet
        print(f'slot of win {win_slot}')

        answer = input('Вы хотите продолжит игру? yes or no')
        if answer == 'yes':
            print(f'balance: {money}')
            continue
        elif answer == 'no':
            print(f'balance: {money}')
            break
        else:
            print('write yes or no')


if __name__ == '__main__':
    casino()



