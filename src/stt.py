import requests
import json
import config

FOLDER_ID = config.folder_id
IAM_TOKEN = config.voice_token

# TODO - cleanup
# with open("test.ogg", "rb") as f:
#     data = f.read()


def stt(data):
    params = "&".join([
    "topic=general",
    "folderId=%s" % FOLDER_ID,
    "lang=ru-RU",
    "format=lpcm",
    "sampleRateHertz=16000",
    ])
    headers = {
        'Authorization': 'Bearer ' + IAM_TOKEN,
    }
    url = f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}"

    with requests.post(url, data=data, headers=headers, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))
        result = resp.json().get("result", "")
        return result