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

# Replace the following with the desired private group chat ID
desired_group_chat_id = 1914730364

@client.on(events.NewMessage(chats=desired_group_chat_id))
async def downloader(event):
    result = await event.download_media()
    # You can add custom logic here to handle the downloaded media
    print(f"Downloaded media from chat {desired_group_chat_id}: {result}")
    
    # Upload the downloaded image to your saved messages
    await client.send_file('me', result, caption=f"Uploaded media from chat {desired_group_chat_id}!")

async def main():
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
