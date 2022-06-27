import logging

from aiogram import Bot, Dispatcher, executor, types
from imlo import checkWord
from transliterate import to_latin, to_cyrillic

API_TOKEN = '5562163623:AAGBU-76SqX5Ilbea9nzqbH_OkTqzukuXI0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("👋Assalomu alaykum uz_imlo botiga Xush kelibsiz!")

@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring!")

@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    words = word.split()
    for word in words:
        is_latin = False
        for item in word.lower():
            if 96 < ord(item) < 123:
                is_latin = True
        if is_latin:
            word = to_cyrillic(word.lower())
        result = checkWord(word)
        if is_latin:
            word = to_latin(word.capitalize())
        if result['available']:
            response = f"✅ {word.capitalize()}"
        else:
            response = f"❌ {word.capitalize()}"
            for text in result['matches']:
                if is_latin:
                    text = to_latin(text)
                response += f"\n✅ {text.capitalize()}"
        await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)