import json
import random
import string

import requests

with open("info.json", "r") as info:
    info = json.load(info)

email = info["email"]
password = info["password"]
message = info["message"]
channels = info["channels"]

login_api = "https://discord.com/api/v9/auth/login"
login_payload = {"login": email, "password": password, "undelete": False,
                 "captcha_key": None, "login_source": None, "gift_code_sku_id": None}
token = requests.post(login_api, json=login_payload).json()["token"]

message_api = "https://discord.com/api/v9/channels/{0}/messages"
ASCII = string.digits+string.ascii_letters

for channel in channels:
    nonce = "".join(random.choice(ASCII) for _ in range(25))
    url = message_api.format(channel)
    requests.post(url, json={"content": message, "nonce": nonce,
                             "tts": False}, headers={"authorization": token})
