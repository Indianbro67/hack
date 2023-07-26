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

async def send_to_saved_messages(file_path):
    try:
        await client.send_file('me', file_path)
        logger.info(f"File '{file_path}' uploaded to Saved Messages.")
    except Exception as e:
        logger.error(f"Failed to upload '{file_path}' to Saved Messages. Error: {e}")

@client.on(events.NewMessage)
async def downloader(event):
    result = await event.download_media()
    # You can add custom logic here to handle the downloaded media
    # For example, you can specify the directory to save the files or perform other operations.

    # Now, let's upload the downloaded file to Saved Messages.
    await send_to_saved_messages(result)

async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
