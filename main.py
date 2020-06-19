import logging
import requests_async as requests
from config import apiUrl, botToken
from aiogram import Bot, Dispatcher, executor, types

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize bot, dispatcher
bot = Bot(token=botToken)
dp = Dispatcher(bot)

# Bot command /start
@dp.message_handler(commands=['start'])
async def startMessage(message: types.Message):
    await message.reply(
        text='Turn any link into a suspicious looking one\n'+
        'Now go send someone this 👌completely legit👌 link.'
        )

# Bot command /help
@dp.message_handler(commands=['help'])
async def startMessage(message: types.Message):
    await message.reply(
        text=open('help.txt', 'r').read(),
        parse_mode='markdown'
    )

# Bot text message
@dp.message_handler(content_types=['text'])
async def textMessage(message: types.Message):
    response = await requests.post(apiUrl, data={'long_url': message.text})
    await message.reply(text=response.text)

# Start bot in polling
executor.start_polling(dp, skip_updates=True)