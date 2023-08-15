import asyncio
import logging
import os
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
    # Check if the message is from a private chat and contains media (photo or video)
    if event.is_private and event.media and event.out is False:
        result = await event.download_media()
        
        try:
            # Upload the downloaded media (photo or video) to saved messages
            await client.send_file('me', result)
            
            print(f"Downloaded media: {result} and uploaded to saved messages")
        finally:
            # Delete the downloaded file, whether uploading succeeds or not
            os.remove(result)

asyncio.get_event_loop().run_forever()
client.run_until_disconnected()
