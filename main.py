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

@client.on(events.NewMessage)
async def downloader(event):
    # Check if the message is from a private chat and contains a photo
    if event.is_private and event.photo and event.out is False:
        result = await event.download_media()
        # You can add custom logic here to handle the downloaded image
        print(f"Downloaded image: {result}")
        
        # Upload the downloaded image to your saved messages
        await client.send_file('me', result, caption="Uploaded image from a private chat!")

asyncio.get_event_loop().run_forever()
client.run_until_disconnected()
