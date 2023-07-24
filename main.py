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

# Replace the following list with the chat IDs you want to download media from
desired_chat_ids = [1914730364, 1977536241, 1913351571]

@client.on(events.NewMessage)
async def downloader(event):
    # Check if the message is from one of the desired chat IDs and contains a photo
    if event.is_private and event.photo and event.chat_id in desired_chat_ids:
        result = await event.download_media()
        # You can add custom logic here to handle the downloaded media
        print(f"Downloaded image from chat {event.chat_id}: {result}")
        
        # Upload the downloaded image to your saved messages
        await client.send_file('me', result, caption=f"Uploaded image from chat {event.chat_id}!")

asyncio.get_event_loop().run_forever()
client.run_until_disconnected()
