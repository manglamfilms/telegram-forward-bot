# Telegram Forward Bot

यह एक सरल Telegram Forward Bot है जो उपयोगकर्ता द्वारा भेजे गए संदेशों को एक निर्दिष्ट चैट (Channel/Group) में फॉरवर्ड करता है।

## सेटअप निर्देश

1. [BotFather](https://t.me/BotFather) से अपना Telegram Bot Token प्राप्त करें।
2. `config.py` फाइल में `BOT_TOKEN` और `DESTINATION_CHAT_ID` सेट करें।
3. निर्भरताएँ इंस्टॉल करने के लिए:
   ```sh
   pip install -r requirements.txt
