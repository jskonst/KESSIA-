import requests
import config

def translate(text, direction='ru'):
    IAM_TOKEN = config.translate_token
    folder_id = config.folder_id
    target_language = direction
    body = {
        "targetLanguageCode": target_language,
        "texts": text,
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
    
    result_array = response.json().get("translations", []) 
    if len(result_array) > 0:
        return result_array[0].get("text", "")



if __name__ == "__main__":
    res = translate("Hello world")
    print(res)
    res = translate("hello world", 'zh')
    print(res)