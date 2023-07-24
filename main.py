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

async def get_group_entity():
    # Replace YOUR_GROUP_USERNAME with the username of the private group you want to download from
    group_username = 'YOUR_GROUP_USERNAME'
    group_entity = await client.get_entity(group_username)
    return group_entity

async def main():
    await client.start()
    logger.info("Client is ready.")
    
    # Get the group entity
    group_entity = await get_group_entity()

    @client.on(events.NewMessage(chats=group_entity))
    async def downloader(event):
        # Check if the message contains media
        if event.media:
            result = await event.download_media()
            # You can add custom logic here to handle the downloaded media
            print(f"Downloaded media from the group: {result}")

            # Upload the downloaded media to your saved messages
            await client.send_file('me', result, caption="Uploaded media from the group!")

    logger.info("Bot is running...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
