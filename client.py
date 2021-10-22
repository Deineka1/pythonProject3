from aiogram import types, Dispatcher
from create_bot import dp, bot

# from aiogram.types import ReplyKeyboardRemove

# # @dp.message_handler(commands=['Меню_клиента'])
# async def menu_custom(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Что Вам принести?')
#
# # @dp.message_handler(commands=['Меню_клиента'])
# async def menu_custom(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Выберите блюдо из меню')
#
# # @dp.message_handler(commands=['Меню_клиента'])
# async def menu_custom(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Доставляем все втечение часа!')


    # Кнопки прописываем для кнопки на месте

# @dp.message_handler(commands=['На_месте'])
# async def na_meste(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Официант')
#
# # @dp.message_handler(commands=['На_месте'])
# async def na_meste1(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Меню')
#
# # @dp.message_handler(commands=['На_месте'])
# async def na_meste2(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Счет')
#
#     # Кнопки для меню с собой
#
# # @dp.message_handler(commands=['С_собой'])
# async def s_soboy(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Меню')
#
#     # Кнопки для меню доставка
#
# # @dp.message_handler(commands=['Доставка'])
# async def dostavka(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Меню')


# @dp.message_handler(commands=['Доставка'])
# async def dostavka1(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Посмотреть заказ')

# def register_handlers_client(dp : Dispatcher):
#     dp.register_message_handler(menu_custom, commands=['На_месте'])
#     dp.register_message_handler(menu_custom, commands=['С_собой'])
#     dp.register_message_handler(menu_custom, commands=['Доставка'])
    # dp.register_message_handler(na_meste, commands=['Официант'])
    # dp.register_message_handler(na_meste1, commands=['Меню'])
    # dp.register_message_handler(na_meste2, commands=['Счет'])
    # dp.register_message_handler(s_soboy, commands=['Меню'])
    # dp.register_message_handler(dostavka, commands=['Меню'])
    # dp.register_message_handler(dostavka1, commands=['Посмотреть_заказ'])

