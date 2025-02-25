from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = "YOUR_BOT_TOKEN"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Send me a message, and I'll forward it!")

@dp.message_handler(content_types=types.ContentType.ANY)
async def forward_message(message: types.Message):
    target_chat_id = "DESTINATION_CHAT_ID"  # जहाँ मैसेज फॉरवर्ड होगा
    await bot.forward_message(target_chat_id, message.chat.id, message.message_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
