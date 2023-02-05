from time import sleep
from tqdm import tqdm, trange
from random import *
from prettytable import *

#основные переменные
id = 0
user_choice = 0
user_money = 1500
bot_money = 1500
croupier_money = 1500

#ставки
middle_bet = user_money // 2
max_bet = user_money

#стикер-пак
listd_stikers = ['''
---------------
|             |
|             |
|             |
|      A♦    |
|             |
|             |
|             |
---------------
                ''',
                '''
---------------
|             |
|             |
|             |
|      A♥    |
|             |
|             |
|             |
---------------
                ''',
                '''
---------------
|             |
|             |
|             |
|      A♣    |
|             |
|             |
|             |
---------------
                ''',
'''
---------------
|             |
|             |
|             |
|      A♠    |
|             |
|             |
|             |
---------------
''',

'''
---------------
|             |
|             |
|             |
|      K♦    |
|             |
|             |
|             |
---------------
''',

'''
---------------
|             |
|             |
|             |
|      K♥    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      K♣    |
|             |
|             |
|             |
---------------
''',

'''
---------------
|             |
|             |
|             |
|      K♠    |
|             |
|             |
|             |
---------------
''',

'''
---------------
|             |
|             |
|             |
|      Q♦    |
|             |
|             |
|             |
---------------
''',

'''
---------------
|             |
|             |
|             |
|      Q♥    |
|             |
|             |
|             |
---------------
''',


'''
---------------
|             |
|             |
|             |
|      Q♣    |
|             |
|             |
|             |
---------------
''',

'''
---------------
|             |
|             |
|             |
|      Q♠    |
|             |
|             |
|             |
---------------
''',

'''
---------------
|             |
|             |
|             |
|      J♦    |
|             |
|             |
|             |
---------------
''',

'''
---------------
|             |
|             |
|             |
|      J♥    |
|             |
|             |
|             |
---------------
''',

'''
---------------
|             |
|             |
|             |
|      J♣    |
|             |
|             |
|             |
---------------
''',


'''
---------------
|             |
|             |
|             |
|      J♠    |
|             |
|             |
|             |
---------------
''',

'''
---------------
|             |
|             |
|             |
|      10♦   |
|             |
|             |
|             |
---------------
''',


'''
---------------
|             |
|             |
|             |
|      10♥   |
|             |
|             |
|             |
---------------
''',

'''
---------------
|             |
|             |
|             |
|      10♣   |
|             |
|             |
|             |
---------------
''',

'''
---------------
|             |
|             |
|             |
|      10♠   |
|             |
|             |
|             |
---------------
''',


'''
---------------
|             |
|             |
|             |
|      9♦    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      9♥    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      9♣    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      9♠    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      8♦    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      8♥    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      8♣    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      8♠    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      7♦    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      7♥    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      7♣    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      7♠    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      6♦    |
|             |
|             |
|             |
---------------
''',
'''
---------------
|             |
|             |
|             |
|      6♥    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      6♣    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      6♠    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      5♦    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      5♥    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      5♣    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      5♠    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      4♦    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      4♥    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      4♣    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      4♠    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      3♦    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      3♥    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      3♣    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      3♠    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      2♦    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      2♥    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      2♣    |
|             |
|             |
|             |
---------------
''','''
---------------
|             |
|             |
|             |
|      2♠    |
|             |
|             |
|             |
---------------
'''
]

value_of_stikers = [1, 1, 1, 1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2]
bot_choice_list = [1, 2, 3, 4, 5]

def progress(dl, vr):
    for i in trange(dl):
        sleep(vr)
progress(60, 0.01)



print('HELLO!\nYOU OPENED Blackjack! (V: 0.1)\nA little bit of rules: \n\t•You can choose: \n\t To play solo \n\t To play with 1 bot \n\t•You need to set bigger sum point of cards than croupier')

start_game = input(''' ----ooO---------------
|                     |
|                     |
|   ГОТОВЫ НАЧАТЬ?    |
|        Да/Нет       |
|                     |
'---------------ooO---- ''').lower()

def bot_play():
    sum_bot = 0
    bot_choise = choice(bot_choice_list)
    for i in range(bot_choise):
        print('Dealers choosing the card..')
        def progress(dl, vr):
            for i in trange(dl):
                sleep(vr)
        progress(60, 0.05)
        bot_card = choice(listd_stikers)
        print(bot_card)
        sum_bot += value_of_stikers[listd_stikers.index(bot_card)]
        print(sum_bot)

    return sum_bot


def game_colo():
    print(f'Now you have {user_money}$')
    print('You need to choose table to play: \t\n•Low table\t\n•Middle table\t\n•High table')
    user_choice_table = int(input('Choose 1/2/3:'))
    if user_choice_table == 1 and user_money >= 50:
        low_tabel()

    elif user_choice_table == 2 and user_money >= 100:
        middle_table()

    elif user_choice_table == 3 and user_money >= 200:
        high_table()

    else:
        print('You chose incorrent symbol. \nBACKING TO LOBBY')
        def progress(dl, vr):
            for i in trange(dl):
                sleep(vr)
        progress(60, 0.01)


def game_with_one_bot():
    pass

def low_tabel():
    user_money1 = user_money
    first_user_card = choice(listd_stikers)
    second_user_card = choice(listd_stikers)
    third_user_card = choice(listd_stikers)
    four_user_card = choice(listd_stikers)
    five_user_card = choice(listd_stikers)
    sum_player = 0
    id = True
    while id == True:
        print(f'(◑‿◐) Croupier: \t\n You can place a min bet - 50. Middle bet {middle_bet}. Max bet {max_bet}. Or you can back (4)')
        user_bet = int(input('\tChoose 1/2/3: '))
        if user_bet == 1:
            user_money1 -= 50
            print(f'(◑‿◐) Croupier: Money at stake - 50$')
            print('(◑‿◐) Croupier shuffles the cards..')

            def progress(dl, vr):
                for i in trange(dl):
                    sleep(vr)
            progress(60, 0.01)

            print(f'YOUR CARDS: {first_user_card}, {second_user_card}')
            sum_player = value_of_stikers[listd_stikers.index(first_user_card)] + value_of_stikers[listd_stikers.index(second_user_card)]
            print(f'SUM OF YOUR POINT IS - {sum_player}')
            print('Would u like to continue? Or enough?: ')
            user_choice_to_continue = input().lower()
            if user_choice_to_continue == 'da' or user_choice_to_continue == 'да' or user_choice_to_continue == '+' or user_choice_to_continue == 'yes' and sum_player < 21:
                print(f'YOUR CARDS: {first_user_card}, {second_user_card}, {third_user_card}')
                sum_player += value_of_stikers[listd_stikers.index(third_user_card)]
                print(f'SUM OF YOUR POINT IS - {sum_player}')
                print('Would u like to continue? Or enough?: ')
                user_choice_to_continue = input().lower()
                if user_choice_to_continue == 'da' or user_choice_to_continue == 'да' or user_choice_to_continue == '+' or user_choice_to_continue == 'yes' and sum_player < 21:
                    print(f'YOUR CARDS: {first_user_card}, {second_user_card}, {third_user_card}, {four_user_card}')
                    sum_player += value_of_stikers[listd_stikers.index(four_user_card)]
                    print(f'SUM OF YOUR POINT IS - {sum_player}')
                    print('Would u like to continue? Or enough?: ')
                    user_choice_to_continue = input().lower()
                    if user_choice_to_continue == 'da' or user_choice_to_continue == 'да' or user_choice_to_continue == '+' or user_choice_to_continue == 'yes' and sum_player < 21:
                        print(f'YOUR CARDS: {first_user_card}, {second_user_card}, {third_user_card}, {four_user_card}, {five_user_card}')
                        sum_player += value_of_stikers[listd_stikers.index(four_user_card)]
                        print('SUM OF YOUR POINT IS - ', sum_player)
                        print('!!!Dealers queue!!!')
                        sum_bot = bot_play()
                        print(f'Dealer sum - {sum_bot}')
                        if sum_player > 21 and sum_bot <= 21:
                            print(f'LOSS! Your cash - {user_money1}$')
                            id = False
                            return user_money1

                        elif sum_player < sum_bot and sum_bot <= 21:
                            print(f'LOSS! Your cash - {user_money1}$')
                            id = False
                            return user_money1

                        elif sum_player == sum_bot:
                            print(f'Draw! Your cash - {user_money1 + 50}$')
                            id = False
                            return user_money1

                        elif sum_player > 21 and sum_bot > 21:
                            print(f'Draw! Your cash - {user_money1 + 50}$')
                            id = False
                            return user_money1

                        elif sum_bot > 21 and sum_player <= 21:
                            print(f'YOU WON! Your cash - {user_money1 + 100}$')
                            id = False
                            return user_money1

                        elif sum_player > sum_bot and sum_player <= 21:
                            print(f'YOU WON! Your cash - {user_money1 + 100}$')
                            id = False
                            return user_money1

                    else:
                        print('!!!Dealers queue!!!')
                        sum_bot = bot_play()
                        print(f'Dealer sum - {sum_bot}')
                        if sum_player > 21 and sum_bot <= 21:
                            print(f'LOSS! Your cash - {user_money1}$')
                            id = False
                            return user_money1

                        elif sum_player < sum_bot and sum_bot <= 21:
                            print(f'LOSS! Your cash - {user_money1}$')
                            id = False
                            return user_money1

                        elif sum_player == sum_bot:
                            print(f'Draw! Your cash - {user_money1 + 50}$')
                            id = False
                            return user_money1

                        elif sum_player > 21 and sum_bot > 21:
                            print(f'Draw! Your cash - {user_money1 + 50}$')
                            id = False
                            return user_money1

                        elif sum_bot > 21 and sum_player <= 21:
                            print(f'YOU WON! Your cash - {user_money1 + 100}$')
                            id = False
                            return user_money1

                        elif sum_player > sum_bot and sum_player <= 21:
                            print(f'YOU WON! Your cash - {user_money1 + 100}$')
                            id = False
                            return user_money1

                else:
                    print('!!!Dealers queue!!!')
                    sum_bot = bot_play()
                    print(f'Dealer sum - {sum_bot}')
                    if sum_player > 21 and sum_bot <= 21:
                        print(f'LOSS! Your cash - {user_money1}$')
                        id = False
                        return user_money1

                    elif sum_player < sum_bot and sum_bot <= 21:
                        print(f'LOSS! Your cash - {user_money1}$')
                        id = False
                        return user_money1

                    elif sum_player == sum_bot:
                        print(f'Draw! Your cash - {user_money1 + 50}$')
                        id = False
                        return user_money1

                    elif sum_player > 21 and sum_bot > 21:
                        print(f'Draw! Your cash - {user_money1 + 50}$')
                        id = False
                        return user_money1

                    elif sum_bot > 21 and sum_player <= 21:
                        print(f'YOU WON! Your cash - {user_money1 + 100}$')
                        id = False
                        return user_money1

                    elif sum_player > sum_bot and sum_player <= 21:
                        print(f'YOU WON! Your cash - {user_money1 + 100}$')
                        id = False
                        return user_money1

            else:
                print('!!!Dealers queue!!!')
                sum_bot = bot_play()
                print(f'Dealer sum - {sum_bot}')
                if sum_player > 21 and sum_bot <= 21:
                    print(f'LOSS! Your cash - {user_money1}$')
                    id = False
                    return user_money1

                elif sum_player < sum_bot and sum_bot <= 21:
                    print(f'LOSS! Your cash - {user_money1}$')
                    id = False
                    return user_money1

                elif sum_player == sum_bot:
                    print(f'Draw! Your cash - {user_money1 + 50}$')
                    id = False
                    return user_money1

                elif sum_player > 21 and sum_bot > 21:
                    print(f'Draw! Your cash - {user_money1 + 50}$')
                    id = False
                    return user_money1

                elif sum_bot > 21 and sum_player <= 21:
                    print(f'YOU WON! Your cash - {user_money1 + 100}$')
                    id = False
                    return user_money1

                elif sum_player > sum_bot and sum_player <= 21:
                    print(f'YOU WON! Your cash - {user_money1 + 100}$')
                    id = False
                    return user_money1

        else:
            id = False
            return user_money1

def middle_table():
    print(f'(◑‿◐) Croupier: \t\n You can place a min bet - 100. Middle bet {middle_bet}. Max bet {max_bet}.')

def high_table():
    print(f'(◑‿◐) Croupier: \t\n You can place a min bet - 200. Middle bet {middle_bet}. Max bet {max_bet}.')

if start_game == 'da' or start_game == '+' or start_game == 'yes' or start_game == 'да':
    while True:
        print('LOBBY:')
        print('You need to choose kind of game: \n\t To play solo \n\t To play with bot')
        user_choice = int(input('Choose 1 or 2:'))
        if user_choice == 1:
            game_colo()
            user_money = low_tabel()


        elif user_choice == 2:
            game_with_one_bot()

        else:
            print('You chose incorrent symbol. \nBACKING TO LOBBY')
            def progress(dl, vr):
                for i in trange(dl):
                    sleep(vr)
            progress(60, 0.01)


else:
    print('Good luck, have fun!')


