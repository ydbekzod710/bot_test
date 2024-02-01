import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


API_TOKEN = '6352216978:AAEil683u6vIgK6bDCN1rxd0sfwdzWa24eM'
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)





button1 = KeyboardButton("📍Manzillimiz")
button2 = KeyboardButton("Ijtimoiy Tarmoqlarda Biz")

button3 = KeyboardButton("")
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(text="Salom.Bizning   <b>Janoshkashop</b> do'konimizdan ayollar kiyimi  hamda ichki kiyimlarini sotib olishingiz mumkin🛍",parse_mode='HTML', reply_markup=keyboard)


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '📍Manzillimiz':
        await message.answer( "Bizning Manzilimiz :Dahbet ko'chasi Emirxan Hotel  Qarshisida ", parse_mode='HTML')
    elif message.text == 'Ijtimoiy Tarmoqlarda Biz':
        await message.answer("Telegram:https://t.me/janoshkashop  \nInstagram: https://www.instagram.com/janoshka.shop/\nTel nomer: +998 93 7255225    \nAdmin Bilan Bog'lanish:https://t.me/janonaa17")


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)