from aiogram import types, Dispatcher
from create_bot import dp, bot
from Keyboards.client_kb import kb_client, kb_client_menu, kb_client_na_meste, kb_client_ssoboy, kb_client_dostavka, kb_admin
#from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMAdmin (StatesGroup):
    login = State()
    password = State()



# @dp.message_handler(commands=['start']) # научим бота реагировать на комманду старт, можно прописать хэлп
async def process_start_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Приветствуем Вас!',  reply_markup=kb_client)
 #   await message.delete() # эта комманда удаляет сообщение "/start" из чата
#

# Кнопка Меню администратора
async def menu_admin_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Авторизуйтесь', reply_markup=kb_admin)
#    await bot.send_message(message.from_user.id, 'Введите Логин')
    # async def login(message):
    #     if message.text == '1111':
    #         await bot.send_message(message.from_user.id, 'Введите пароль')
    #     else:
    #         await bot.send_message(message.from_user.id, 'Нет пользователя с таким логином')
    #     if message.text == '2222':
    #         await bot.send_message(message.from_user.id, 'Вход выполнен')
    #     else:
    #         await bot.send_message(message.from_user.id, 'Не верный пароль')

    # Кнопки Меню Админа

#async def admin_dostavka_order(message: types.Message):
 #   await bot.send_message(message.from_user.id, 'Доставки на сегодня: ')

async def admin_dostavka_order(message: types.Message):
    await bot.send_message(message.forward_from_message_id, 'Доставки на сегодня: ')

    # Кнопка Ресторан
async def admin_restorant(message: types.Message):
    await bot.send_message(message.from_user.id, 'Заказы на сегодня: ')

    # Кнопка Прибыль
async def admin_profit(message: types.Message):
    await bot.send_message(message.from_user.id, 'Прибыль составляет: ')

    # Кнопка Отчет
async def admin_report(message: types.Message):
    await bot.send_message(message.from_user.id, 'Отчет за сегодня: ')


# Кнопка Меню клиента
async def menu_custom_command(message: types.Message):
     await bot.send_message(message.from_user.id, 'Выберите способ получения заказа', reply_markup=kb_client_menu)


    # Кнопки для меню Меню клиента

# Кнопка На месте
async def menu_custom1(message : types.Message):
    await bot.send_message(message.from_user.id, 'Что Вам принести?', reply_markup=kb_client_na_meste)

# Кнопка С собой
async def menu_custom2(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите блюдо из меню', reply_markup=kb_client_ssoboy)

# Кнопка Доставка
async def menu_custom3(message: types.Message):
    await bot.send_message(message.from_user.id, 'Доставляем все втечение часа!', reply_markup=kb_client_dostavka)


    # Кнопки для меню На месте

# Кнопка Официант
async def na_meste_waiter(message : types.Message):
    await bot.send_message(message.from_user.id, 'Официант подойдет в ближайшее время ')

# Кнопка Меню
async def na_meste_menu(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберете блюдо')

# Кнопка Счет
async def na_meste_bill(message : types.Message):
    await bot.send_message(message.from_user.id, 'Счет')


    # Кнопки для меню С собой

# Кнопка Меню
async def s_soboy_menu(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберете блюдо', )


    # Кнопки для меню Доставка

# Кнопка Меню
async def dostavka_menu(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберете блюдо')

# Кнопка Посмотреть заказ
async def dostavka_order(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ваш заказ: ')


# #@dp.message_handler() #  обьявляем декаратор
async def bot_message(message : types.Message):# обьявляем асинхронную функцию для приема одновременных сообщений от пользователей. Что т.к. эта функция асинхронная это
#      # боту не подвисать при приеме нескольких сообщений от разных пользователей сразу
# #     #await message.answer(message.text) # бот отвечает на сообщение которое пришло этим же сообщение, эхобот
# #     #await message.reply(message.text) # бот отвечает на сообщение с упоминанием автора сообщения
    await bot.send_message(message.from_user.id, message.text) # бот отвечает пользователю в личку
#
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_dostavka_order, commands=['Доставки'])
    dp.register_message_handler(admin_restorant, commands=['Ресторан'])
    dp.register_message_handler(admin_profit, commands=['Прибыль'])
    dp.register_message_handler(admin_report, commands=['Отчет'])

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(menu_admin_command, commands=['Меню_админа'])
    dp.register_message_handler(menu_custom_command, commands=['Меню_клиента'])
    dp.register_message_handler(menu_custom1, commands=['На_месте'])
    dp.register_message_handler(menu_custom2, commands=['С_собой'])
    dp.register_message_handler(menu_custom3, commands=['Доставка'])
    dp.register_message_handler(na_meste_waiter, commands=['Официант'])
    dp.register_message_handler(na_meste_menu, commands=['Меню'])
    dp.register_message_handler(na_meste_bill, commands=['Счет'])
    dp.register_message_handler(s_soboy_menu, commands=['Меню_с_собой'])
    dp.register_message_handler(dostavka_menu, commands=['Меню_доставка'])
    dp.register_message_handler(dostavka_order, commands=['Посмотреть_заказ'])

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(bot_message)

