from utils import *
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
from telethon import TelegramClient, sync
from config import *

client = TelegramClient("ava_bot", api_id, api_hash)
client.start()
def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != prev_time

prev_update_time = ""

while True:
    if time_has_changed(prev_update_time):
        prev_update_time = convert_time_to_string(datetime.now()).replace(":", "_")
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file =  client.upload_file(f"image_time/{prev_update_time}.jpg")
        client(UploadProfilePhotoRequest(file=file))