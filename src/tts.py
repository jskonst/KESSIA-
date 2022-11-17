import requests
import config
import pyaudio
import wave

def synthesize(folder_id, iam_token, text):
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    headers = {
        'Authorization': 'Bearer ' + iam_token,
    }

    data = {
        'text': text,
        'lang': 'en-EN', # вынести в параметр
        'voice': 'john', # и это тоже 'filipp',
        'folderId': folder_id,
        'format': 'lpcm',
        'sampleRateHertz': 8000,
    }

    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

        for chunk in resp.iter_content(chunk_size=None):            
            yield chunk



if __name__ == "__main__":
    str_to_generate = "Проверка генерации текста"
    filename = "out.raw"

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=8000,
                output=True)


    with open(filename, "wb") as f:
        for audio_content in synthesize(config.folder_id, config.voice_token, str_to_generate):
            stream.write(audio_content)
            f.write(audio_content)
    

    stream.stop_stream()
    stream.close()
    p.terminate()
