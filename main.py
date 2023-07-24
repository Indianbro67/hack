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
    # Download the media (if any) from the message
    result = await event.download_media()
    # You can add custom logic here to handle the downloaded media

    # Get the chat ID of the incoming message
    chat_id = event.chat_id
    print(f"Received message in chat with ID: {chat_id}")

    # Send the chat ID to the saved messages
    await client.send_message('me', f"Received message in chat with ID: {chat_id}")

async def main():
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    client.loop.run_until_complete(main())
