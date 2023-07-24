# -*- coding:utf-8 -*-
import asyncio
import logging
from decouple import config
from telethon import TelegramClient, events

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

api_id = config('API_ID')
api_hash = config('API_HASH')

client = TelegramClient(
    'mahdiashtian',
    api_id,
    api_hash,
)

client.start()

# Replace YOUR_DESIRED_CHAT_ID with the chat ID you want to download media from
desired_chat_id = 1914730364

@client.on(events.NewMessage)
async def downloader(event):
    # Check if the message is from the desired chat ID and contains media
    if event.chat_id == desired_chat_id and event.media:
        result = await event.download_media()
        # You can add custom logic here to handle the downloaded media
        print(f"Downloaded media from chat {desired_chat_id}: {result}")
        
        # Upload the downloaded image to your saved messages
        await client.send_file('me', result, caption="Uploaded image from a specific chat!")

asyncio.get_event_loop().run_forever()
client.run_until_disconnected()
