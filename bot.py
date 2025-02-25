

import asyncio
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = "7414662064:AAEauJcIDlFoQGaJlLBheABK_iuB0RMkP88"
DESTINATION_CHAT_ID = "YOUR_DESTINATION_CHAT_ID"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()  # ✅ सही तरीका

@dp.message()
async def forward_message(message: types.Message):
    await bot.forward_message(DESTINATION_CHAT_ID, message.chat.id, message.message_id)

async def main():
    await dp.start_polling(bot)  # ✅ सही तरीका Aiogram v3 के लिए

if __name__ == "__main__":
    asyncio.run(main())  # ✅ asyncio को सही से रन करना
