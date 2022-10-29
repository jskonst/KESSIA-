import requests
import json
import config

FOLDER_ID = config.folder_id
IAM_TOKEN = config.voice_token

with open("test.ogg", "rb") as f:
    data = f.read()


params = "&".join([
    "topic=general",
    "folderId=%s" % FOLDER_ID,
    "lang=ru-RU"
])

url = f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}"

headers = {
    'Authorization': 'Bearer ' + IAM_TOKEN,
}
with requests.post(url, data=data, headers=headers, stream=True) as resp:
    if resp.status_code != 200:
        raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))
    print(resp.json())

