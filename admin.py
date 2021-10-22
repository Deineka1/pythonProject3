# from aiogram import types, Dispatcher
#from create_bot import dp, bot
#
#

#
#
# # Кнопки для ввода логина и пароля
#
# # @dp.message_handler(commands=['Login'])
# async def menu_admin(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Введите Ваш логин')
#     await message.delete()  # эта комманда удаляет сообщение "Login" из чата
#
# # @dp.message_handler(commands=['Password'])
# async def menu_admin(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Введите ваш пароль')
#     await message.delete()  # эта комманда удаляет сообщение "Password" из чата
#
#
# # Кнопки для меню админа
#
# # @dp.message_handler(commands=['Меню_админа'])
# async def menu_admin(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Доставка')
#
#
# # @dp.message_handler(commands=['Меню_админа'])
# async def menu_admin(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Ресторан')
#
#
# # @dp.message_handler(commands=['Меню_админа'])
# async def menu_custom(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Прибыль')
#
#
# # @dp.message_handler(commands=['Меню_админа'])
# async def menu_admin(message : types.Message):
#     await bot.send_message(message.from_user.id, 'Отчет')
#
#
#def register_handlers_admin(dp: Dispatcher):
#    dp.register_message_handler(menu_admin_command, commands=['Меню_админа'])

#     dp.register_message_handler(menu_admin, commands=['Login'])
#     dp.register_message_handler(menu_admin, commands=['Password'])
#     dp.register_message_handler(menu_admin, commands=['Доставка'])
#     dp.register_message_handler(menu_admin, commands=['Ресторан'])
#     dp.register_message_handler(menu_admin, commands=['Прибыль'])
#     dp.register_message_handler(menu_admin, commands=['Отчет'])
