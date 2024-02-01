import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


API_TOKEN = '6160540168:AAGi4xMuzYIxiKYgm5Q-jfykjhFNy5FAm_U'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



button1 = KeyboardButton("Men haqimda")
button2 = KeyboardButton("Ijtimoiy tarmoqlarda men")
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(text="Salom. Mening ismim <b>Bekzod</b>. Men haqimdagi botga xush kelibsiz. Ma'lumotlar uchun pasdagi tugmalar orqali bilib olasiz.",parse_mode='HTML', reply_markup=keyboard)



@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == 'Men haqimda':
        await message.answer(text="Mening ismim: <b>Bekzod Yadgorov</b> \nYoshim: <b>13 da</b> \nTug'ilgan sana: <b>14.03.2010</b> \nHobby: <b>IT, suzish, stol tennis, uxlash</b>", parse_mode='HTML')
    elif message.text == 'Ijtimoiy tarmoqlarda men':
        await message.answer("Telegram: @ydbekzod \nInstagram: https://instagram.com/yd.bekzod \nTel nomer: +998 91 032 32 58")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)