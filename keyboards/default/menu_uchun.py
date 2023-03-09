from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

from loader import bot,base

menular = base.select_all_types()
j = 0
index= 0
keys = []
for menu in menular:
    if j % 2 == 0 and j != 0:
        index += 1
    if j % 2 == 0:
        keys.append([KeyboardButton(text=f'{menu[1]}', )])
    else:
        keys[index].append(KeyboardButton(text=f'{menu[1]}', ))
    j += 1

keys.append([KeyboardButton(text='Adminga murojaat')])
keys.append([KeyboardButton(text='Korzinka')])
menu_buttons = ReplyKeyboardMarkup(keyboard=keys,resize_keyboard=True)
