import io
import os
import platform
import codecs

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# -------------------------------------------------------------------------------
#For Local Repo
current_dir = "C:\\Users\\Hassan Elahi\\Desktop\\Urdu-Speech-to-Text-Google-Cloud\\DataSet\\wav\\"
arr = list([])
#--------------------------------------------------------------------------------



def Speech2Text(file):
    
    
    if(platform.system() != 'Windows'):
        current_dir = os.getcwd()
    
    file_name = current_dir + file
    print(file_name)
    
    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ur-PK')
    
    # Detects speech in the audio file
    response = client.recognize(config, audio)
    
    
    text = " ".join([result.alternatives[0].transcript for result in response.results])
    arr.append(file_name.split('\\')[-1]+":"+text)
    print(file_name.split('\\')[-1]+":"+text)



if __name__ == '__main__':
    
    #Setting Envionment vaiable for Google Credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "E:/cred.json"
    client = speech.SpeechClient()
    Speech2Text("hin_0001.wav")

    with io.open('wav2Urdu.txt', 'w',encoding='utf-8') as f:
        for item in arr:
            f.write("{}\n".format(item))

    