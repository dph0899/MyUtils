"""Working with channels"""


import sys

from telethon import TelegramClient
from telethon.tl.types import Channel


async def get_channel_id_by_course_name(client: TelegramClient, course_name: str):
    """Get channel id by course name"""
    channel_id_list = []
    async for dialog in client.iter_dialogs():
        if isinstance(dialog.entity, Channel) and dialog.name == course_name:
            channel_id_list.append(dialog.id)
    if len(channel_id_list) != 1:
        print(str(len(channel_id_list)) +
              " channel(s) found for course " + course_name)
        sys.exit()
    else:
        return channel_id_list[0]
