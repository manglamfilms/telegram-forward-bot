
import asyncio
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = "7414662064:AAEauJcIDlFoQGaJlLBheABK_iuB0RMkP88"
DESTINATION_CHAT_ID = "YOUR_DESTINATION_CHAT_ID"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()  # Dispatcher को अलग बनाओ

@dp.message()
async def forward_message(message: types.Message):
    await bot.forward_message(DESTINATION_CHAT_ID, message.chat.id, message.message_id)

async def main():
    dp.include_router(dp)  # ❌ यह लाइन हटाओ, क्योंकि Dispatcher को Router में नहीं जोड़ा जाता
    await dp.start_polling(bot)  # Dispatcher को सीधे बॉट के साथ स्टार्ट करो

if __name__ == "__main__":
    asyncio.run(main())
