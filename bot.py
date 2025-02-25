import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN = "YOUR_BOT_TOKEN"
DESTINATION_CHAT_ID = "DESTINATION_CHAT_ID"  # जहाँ मैसेज फॉरवर्ड होगा

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Send me a message, and I'll forward it!")

@dp.message()
async def forward_message(message: Message):
    await bot.forward_message(DESTINATION_CHAT_ID, message.chat.id, message.message_id)

async def main():
    dp.include_router(dp)  # Router को Dispatcher में जोड़ना
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
