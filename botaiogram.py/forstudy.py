import logging
import random

from aiogram import types, Bot, Dispatcher, executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from random import choice


logging.basicConfig(level=logging.INFO)

bot = Bot('5939292642:AAGWWXGouVgfj5nAkdVM1S4-8024EJD0q9A')
memstore = MemoryStorage()
dp = Dispatcher(bot, storage=memstore)




user: dict = {'in_game': False,
              'secret_number': None,
              'attempts': 1,
              'total_games': 0,
              'wins': 0,
              'is_game_over': 0,
              'losses': 0,
              'approach': 0}

reg: dict = {'reg_id': False,
             'user_name': ''}

admin: dict = {'admin_activate': False,
               'chat_id': False}





@dp.message_handler(commands=['start'], state=None)
async def process_start_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Приветствую! \n Это бот LDLN! \n Тебе стоит узнать больше обо мне. \n Напиши /help')

@dp.message_handler(commands=['help'], state=None)
async def process_help_message(message: types.Message):
    await bot.send_message(message.chat.id, 'У нас есть игра. \nСуть игры заключается в том, чтобы угадать число от 1 до 100 менее чем за 5 попыток. \nКоманды доступеные вам: \n /start - запуск бота \n /help - помощь \n /play - начало игры \n /restart - перезапуск системы \n /reg - регистрация своего имени и вход в систему для получения доп.функций \n /admin - вход от имени администратора \n /exit_admin - выйти с админ режиима \n /myacc - информация о вашем аккаунте')

@dp.message_handler(commands=['play'], state=None)
async def process_play_message(message: types.Message):
    await bot.send_message(message.chat.id, 'Игра началась! Число загадано! \nПопробуй угадать.')
    user['in_game'] = True
    user['secret_number'] = choice_random_number()


@dp.message_handler(commands=['restart'])
async def restart_game_servises(message: types.Message):
    user['in_game'] = False
    user['attempts'] = 0
    user['is_game_over'] = 0
    await bot.send_message(message.chat.id, 'Рестарт игры..')
    await bot.send_message(message.chat.id, 'Обновление игровых данных прошло успешно!')


@dp.message_handler(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def is_number_the_same_as_bot_choice(message: types.Message):
    wrongs = user['attempts']
    secr = user['secret_number']
    if message.text.isdigit:
        user_number = int(message.text)
        print('Cheat: secret number', user['secret_number'])
        print('user number:', user_number)
        if user['in_game'] == True and user['is_game_over'] == 0:
            if user_number == user['secret_number'] and user['attempts'] != 5:
                await bot.send_message(message.chat.id, 'Вы выиграли!!!')
                await bot.send_message(message.chat.id, f'Число ваших попыток: {wrongs}')
                user['is_game_over'] = 1
                user['wins'] += 1
                user['total_games'] += 1
                user['approach'] += 1

            elif user_number < user['secret_number'] and user['attempts'] != 5:
                await bot.send_message(message.chat.id, 'Ваше число меньше!')
                user['attempts'] += 1
                await bot.send_message(message.chat.id, f'Вами потрачена: {wrongs}-я попытка')
                user['approach'] += 1

            elif user_number > user['secret_number'] and user['attempts'] != 5:
                await bot.send_message(message.chat.id, 'Ваше число больше!')
                user['attempts'] += 1
                await bot.send_message(message.chat.id, f'Вами потрачена: {wrongs}-я попытка')
                user['approach'] += 1

            elif user['attempts'] == 5:
                await bot.send_message(message.chat.id, f'Вами потрачена: {wrongs}-я попытка')
                await bot.send_message(message.chat.id, 'У вас осталось 0 попыток. Game over!')
                user['is_game_over'] = 1
                user['losses'] += 1
                user['total_games'] += 1
                user['approach'] += 1
                await bot.send_message(message.chat.id, f'Загаданное число: {secr}')

    else:
        print('Режим игры не включен. Напишите /play или /restart для рестарта системы!')

@dp.message_handler(commands='reg')
async def registration(message: types.Message):
    reg['reg_id'] = True
    await bot.send_message(message.chat.id, 'Введите свое имя: ')

@dp.message_handler(commands='myacc')
async def show_info(message: types.Message):
    user_name = reg['user_name']
    print('the name of user', user_name)
    await bot.send_message(message.chat.id, reg['user_name'])
    reg['reg_id'] = False
    await bot.send_message(message.chat.id, 'После регестрации вам доступны функции: \n /stat - статистика пользователя')

@dp.message_handler(commands='admin')
async def admin_console(message: types.Message):
    await bot.send_message(message.chat.id, 'Команды доступные вам: \n /check_secret_number \n /send_message_to_me')
    admin['admin_activate'] = True
    print('Пользователь авторизовался в админке')

@dp.message_handler(commands='check_secret_number')
async def check_number(message: types.message):
    num = user['secret_number']
    await bot.send_message(message.chat.id, num)
    print('Один из пользователей подсматривает..')

@dp.message_handler(commands='send_message_to_me')
async def send_message(message: types.Message):
    await bot.send_message(message.chat.id, 'Сейчас ты можешь написать мне )))')
    admin['chat_id'] = True
    print('Вам сейчас кто-то напишет..')


@dp.message_handler(commands='stat')
async def stat(message: types.message):
    approach = user['approach']
    wins = user['wins']
    losses = user['losses']
    await bot.send_message(message.chat.id, f'Количество побед: {wins} \n Количество проигрышей: {losses} \n Общее кол-во попыток: {approach}')


@dp.message_handler(lambda x: x.text)
async def red_information(message: types.Message):
    user_message = message.text
    if reg['reg_id'] == True:
        reg['user_name'] = message.text.title()
        await bot.send_message(message.chat.id, 'Чтобы посмотреть свои данные введите /myacc')

    elif admin['admin_activate'] == True and admin['chat_id'] == True:
        print('Пользователь отправил вам сообщение', user_message)



@dp.message_handler(commands='delete')
async def sushi_answer(callback: types.CallbackQuery):
    pass

def choice_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)