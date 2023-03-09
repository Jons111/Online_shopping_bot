from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, \
    CallbackQuery, ReplyKeyboardRemove, LabeledPrice

from keyboards.default.menu_uchun import menu_buttons
from loader import dp,base,bot
from states.holatlar import Sotib_olish

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menu_buttons)
    await Sotib_olish.type_tanlash_holati.set()

@dp.message_handler(state=Sotib_olish.type_tanlash_holati,commands = "start")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_buttons)
    await Sotib_olish.type_tanlash_holati.set()

@dp.message_handler(state=Sotib_olish.type_tanlash_holati,text = "Korzinka")
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    maxsulotlar = base.select_maxsulotlar_from_korzinka(tg_id=user_id)
    for  maxsulot in maxsulotlar:
        max_id = maxsulot[0]
        max_nomi = maxsulot[1]
        max_narxi = maxsulot[2]
        max_rasmi = maxsulot[3]
        max_soni = maxsulot[4]
        await bot.send_message(chat_id=user_id,text="Sotib olingan maxsulotlar",reply_markup=ReplyKeyboardRemove())
        """(1, 'Cola', 11000, 'https://t.me/UstozShogird/17932', 1, 5883029982, '.....')"""
        await bot.send_photo(chat_id=user_id, photo=max_rasmi,
                             caption=f"Nomi : {max_nomi}\n"
                                     f"Narxi : {max_narxi}\n"
                                     f"Malumoti : {max_soni}\n",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text="+", callback_data=f'plus {max_id}'),
                                         InlineKeyboardButton(text=f"{max_soni}", callback_data=f'soni {max_id}'),
                                         InlineKeyboardButton(text=f"-", callback_data=f'minus {max_id}'),
                                     ],
                                     [
                                         InlineKeyboardButton(text=f"Delete", callback_data=f'del {max_id}'),
                                         InlineKeyboardButton(text=f"Xarid qilish", callback_data=f'tolov {max_id}'),
                                     ]
                                 ]
                             ))
        await Sotib_olish.max_tanlash_holati.set()


@dp.message_handler(state=Sotib_olish.type_tanlash_holati)
async def bot_start(message: types.Message):
    text = message.text
    tur = base.select_type(nomi=text)
    if not tur:
        await message.answer(f"Salom, bunday menu mavjud emas qayta kiriting", reply_markup=menu_buttons)
        await Sotib_olish.type_tanlash_holati.set()
    else:
        maxsulotlar = base.select_maxsulotlar(tur_id=tur[0])

        j = 0
        index = 0
        keys = []
        for menu in maxsulotlar:
            if j % 2 == 0 and j != 0:
                index += 1
            if j % 2 == 0:
                keys.append([KeyboardButton(text=f'{menu[1]}', )])
            else:
                keys[index].append(KeyboardButton(text=f'{menu[1]}', ))
            j += 1

        keys.append([KeyboardButton(text='Ortga')])
        maxsulotlar_buttons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
        await message.answer(f"Maxsulotlarni tanlang, {message.from_user.full_name}!",reply_markup=maxsulotlar_buttons)
        await Sotib_olish.max_tanlash_holati.set()

@dp.message_handler(state=Sotib_olish.max_tanlash_holati,text="Ortga")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_buttons)
    await Sotib_olish.type_tanlash_holati.set()


@dp.message_handler(state=Sotib_olish.max_tanlash_holati,commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_buttons)
    await Sotib_olish.type_tanlash_holati.set()

@dp.message_handler(state=Sotib_olish.max_tanlash_holati)
async def bot_start(message: types.Message):
    text = message.text
    user_id = message.from_user.id
    maxsulot = base.select_maxsulot(nomi=text)
    "(3, 'Cola', 11000, 'https://t.me/UstozShogird/17932', 'Bu cola', 2)"
    max_id = maxsulot[0]
    max_nomi = maxsulot[1]
    max_narxi = maxsulot[2]
    max_rasmi = maxsulot[3]
    max_malumot = maxsulot[4]
    await bot.send_photo(chat_id=user_id,photo=max_rasmi,
                         caption=f"Nomi : {max_nomi}\n"
                                 f"Narxi : {max_narxi}\n"
                                 f"Malumoti : {max_malumot}\n",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text="Sotib olish",callback_data=f'buy {max_id}')
                                 ]
                             ]
                         ))


@dp.callback_query_handler(state=Sotib_olish.max_tanlash_holati,)
async def bot_start(xabar: CallbackQuery):
    malumot = xabar.data .split(' ')

    if malumot[0]=='buy':
        max_id = malumot[1]
        maxsulot = base.select_maxsulot(id=max_id)
        user_id = xabar.from_user.id
        max_nomi = maxsulot[1]
        """
        (2, "Lag'mon", 16000, 'https://t.me/UstozShogird/17932', "Bu Uyg'ur lag'moni", 1)
        """
        korzinka_maxsulot = base.select_maxsulot_from_korzinka(tg_id=user_id,nomi=max_nomi)
        print(korzinka_maxsulot,'*************************')
        if not korzinka_maxsulot:
            max_narxi = maxsulot[2]
            max_rasm = maxsulot[3]
            max_soni = 1
            ism = xabar.from_user.first_name

            base.korzinkaga_qoshish(ism=ism,tg_id=user_id,nomi=max_nomi,narxi=max_narxi,son=max_soni,rasm=max_rasm)
            await bot.send_message(chat_id=user_id,text='Maxsulot sotib olindi')
            await Sotib_olish.max_tanlash_holati.set()
        else:
            """(1, 'Cola', 11000, 'https://t.me/UstozShogird/17932', 1, 5883029982, '.....')"""
            max_nomi = korzinka_maxsulot[1]
            max_soni = korzinka_maxsulot[4]+1
            user_id = korzinka_maxsulot[5]
            base.update_korzinka(son=max_soni,tg_id=user_id,nomi=max_nomi)
            await bot.send_message(chat_id=user_id, text='Maxsulot sotib olindi')
            await Sotib_olish.max_tanlash_holati.set()

    elif malumot[0]=='plus':
        message_id = xabar.message.message_id
        print(message_id)
        korzinka_maxsulot = base.select_maxsulot_from_korzinka(id=malumot[1])
        max_id=  korzinka_maxsulot[0]
        max_nomi = korzinka_maxsulot[1]
        max_soni = korzinka_maxsulot[4] + 1
        user_id = korzinka_maxsulot[5]
        base.update_korzinka(son=max_soni, tg_id=user_id, nomi=max_nomi)
        await bot.edit_message_reply_markup(chat_id=user_id,message_id=message_id,reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text="+", callback_data=f'plus {max_id}'),
                                         InlineKeyboardButton(text=f"{max_soni}", callback_data=f'soni {max_id}'),
                                         InlineKeyboardButton(text=f"-", callback_data=f'minus {max_id}'),
                                     ],
                                     [
                                         InlineKeyboardButton(text=f"Delete", callback_data=f'del {max_id}'),
                                         InlineKeyboardButton(text=f"Xarid qilish", callback_data=f'tolov {max_id}'),
                                     ]
                                 ]
                             ))
        await Sotib_olish.max_tanlash_holati.set()

    elif malumot[0]=='minus':
        message_id = xabar.message.message_id
        print(message_id)
        korzinka_maxsulot = base.select_maxsulot_from_korzinka(id=malumot[1])
        max_id=  korzinka_maxsulot[0]
        max_nomi = korzinka_maxsulot[1]
        max_soni = korzinka_maxsulot[4] - 1
        user_id = korzinka_maxsulot[5]
        base.update_korzinka(son=max_soni, tg_id=user_id, nomi=max_nomi)
        await bot.edit_message_reply_markup(chat_id=user_id,message_id=message_id,reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text="+", callback_data=f'plus {max_id}'),
                                         InlineKeyboardButton(text=f"{max_soni}", callback_data=f'soni {max_id}'),
                                         InlineKeyboardButton(text=f"-", callback_data=f'minus {max_id}'),
                                     ],
                                     [
                                         InlineKeyboardButton(text=f"Delete", callback_data=f'del {max_id}'),
                                         InlineKeyboardButton(text=f"Xarid qilish", callback_data=f'tolov {max_id}'),
                                     ]
                                 ]
                             ))
        await Sotib_olish.max_tanlash_holati.set()

    elif malumot[0]=='del':



        user_id = xabar.from_user.id
        message_id = xabar.message.message_id
        max_id = malumot[1]
        base.delete_maxsulot_from_korzinka(id=max_id)
        await bot.delete_message(chat_id=user_id,message_id=message_id)
        await Sotib_olish.max_tanlash_holati.set()

    elif malumot[0] =='tolov':
        payment_token = "371317599:TEST:1675139898651"
        korzinka_maxsulot = base.select_maxsulot_from_korzinka(id=malumot[1])
        print(korzinka_maxsulot)
        max_id = korzinka_maxsulot[0]
        max_nomi = korzinka_maxsulot[1]
        max_narxi = korzinka_maxsulot[2]
        max_soni = korzinka_maxsulot[4]
        umumiy_summa = max_narxi*max_soni*100
        user_id = xabar.from_user.id


        await bot.send_invoice(chat_id=user_id,title="Sotib olish",
                               description=f"Maxsulot nomi :{max_nomi}",payload='222',
                               provider_token=payment_token,
                               currency='UZS',
                               prices=[LabeledPrice(label="Umumiy summa ",amount=umumiy_summa)]

                               )














