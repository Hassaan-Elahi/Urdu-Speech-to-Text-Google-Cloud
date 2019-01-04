
import io
import os
import platform
import glob
import codecs
import pickle

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# -------------------------------------------------------------------------------
#For Local Repo
current_dir = "C:\\Users\\Hassan Elahi\\Desktop\\Urdu-Speech-to-Text-Google-Cloud\\"
arr = list([])
#--------------------------------------------------------------------------------



def Speech2Text(file):
    
    if(platform.system() != 'Windows'):
        current_dir = os.getcwd()
        file_name = current_dir + "/DataSet/wav/" +file
    else:
        current_dir = "C:\\Users\\Hassan Elahi\\Desktop\\Urdu-Speech-to-Text-Google-Cloud\\"
        file_name = current_dir + "DataSet\\wav\\" + file
        
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
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cred.json"
    client = speech.SpeechClient()
    
    c = 0
    if (platform.system() != 'Windows'):
        for file in glob.glob('DataSet/wav/*.wav'):
            Speech2Text(file.split('/')[-1])
            
    
    else:
        
        for file in glob.glob('DataSet\\wav\\*.wav'):
            Speech2Text(file.split("\\")[-1])
            
    
    with open('wav2Urdu.pkl', 'wb') as f:
        pickle.dump(arr, f)
        
    with io.open('wav2Urdu.txt', 'w',encoding='utf-8') as f:
        for item in arr:
            f.write("{}\n".format(item))

    