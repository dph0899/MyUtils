# import os
# import sys

# from telethon import TelegramClient, errors

# from .tele.channel import get_channel_id_by_course_name

# client = TelegramClient('anon', api_id, api_hash)
# courses_dir = sys.argv[1]








# async def first_message(channel_id, topic_name, course_name):
#     msg = await client.send_message(channel_id, topic_name)
#     with open(course_name, 'a') as f:
#         f.write(topic_name + ": " + "https://t.me/c/" +
#                 str(channel_id)[4:] + "/" + str(msg.id) + "\n")


# async def upload():
#     courses_names = os.listdir(courses_dir)
#     for course_name in courses_names:
#         # await client.send_message("me", course_name)
#         course_dir = courses_dir + '\\' + course_name
#         topics_names = os.listdir(course_dir)
#         topics_names.sort(key=natural_sort_key)
#         channel_id = await get_channel_id_by_course_name(course_name)
#         for topic_name in topics_names:
#             topic_dir = course_dir + '\\' + topic_name
#             files_names = os.listdir(topic_dir)
#             await first_message(channel_id, topic_name, course_name)
#             for file_name in files_names:
#                 file_path = topic_dir + '\\' + file_name
#                 if file_name[-3:] == "mp4":
#                     await client.send_file(entity=channel_id, file=file_path, supports_streaming=True,
#                                            caption=file_name)
#                 else:
#                     await client.send_file(entity=channel_id, file=file_path,
#                                            caption=file_name)


# async def download():
#     channel_id = await get_channel_id_by_course_name(courses_dir)
#     current_topic = "ahihi failed"
#     async for message in client.iter_messages(channel_id, reverse=True):
#         if (message.file or message.video) and message.raw_text:
#             try:
#                 await message.download_media(r'/run/media/dph/New Volume/' + courses_dir + r'/' + current_topic + r'/' + message.raw_text)
#             except errors.FileReferenceExpiredError:
#                 refetched_message = await client.get_messages(channel_id, ids=message.id)
#                 await refetched_message.download_media(r'/run/media/dph/New Volume/' + courses_dir + r'/' + current_topic + r'/' + refetched_message.raw_text)
#         elif message.raw_text:
#             current_topic = message.raw_text


# async def main():
#     await download()

# with client:
#     client.loop.run_until_complete(main())
