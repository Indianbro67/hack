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

# Dictionary to map group chat IDs to their captions
group_chats = {
    1914730364: "Caption for Group 1",
    1977536241: "Caption for Group 2",
    1913351571: "Caption for Group 3",
    # Add more chat IDs and captions as needed
}

target_group_username = "geug678"

@client.on(events.NewMessage)
async def downloader(event):
    # Check if the message is from a private group chat and contains media
    if event.is_group and event.chat_id in group_chats and event.media and not event.out:
        result = await event.download_media()
        # You can add custom logic here to handle the downloaded media
        print(f"Downloaded media from group {event.chat_id}: {result}")

        # Send the downloaded media to the target group with the corresponding caption
        caption = group_chats[event.chat_id]
        await client.send_file(target_group_username, result, caption=caption)

asyncio.get_event_loop().run_forever()
client.run_until_disconnected()
