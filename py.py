from random import randint

guesses_made = 0

print('Приветствую, ты запустил игру Угадай Число. Я загадываю а твоя задача отгадать число.. ')
print()
print('На это тебе будет дано 4 попытки. ')
print()
name = input('Введите ваше имя:')


while guesses_made < 4:
    bot = randint(1, 20)
    user_choice = int(input(name + ', Введите значение. От 1 до 20: '))
    guesses_made += +1

    if user_choice > bot:
        print('Твое число больше загаданного! ')

    elif user_choice < bot:
        print('Твое число меньше загаданного!')

    else:
        break


if bot == user_choice:
    print('Ничего себе, ты угадал!')

else:
    print('Ты лошара. ' + 'Я загадал число {0}'.format(bot))






