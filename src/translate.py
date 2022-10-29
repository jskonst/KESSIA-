import requests
import config

if __name__ == "__main__":
    IAM_TOKEN = config.translate_token
    folder_id = config.folder_id
    target_language = 'ru'
    texts = ["Hello", "World"]

    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                            json=body,
                            headers=headers
                            )

    print(response.text)