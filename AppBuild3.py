# import required module
import os

import speech_recognition as sr
from google.cloud import translate_v2 as translate

# explicit function to take input commands
# and recognize them
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_service_key.json'

r = sr.Recognizer()
with sr.Microphone() as source:

        # seconds of non-speaking audio before
        # a phrase is considered complete
        print('Listening')
        r.pause_threshold = 0.7
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='kn-In')

            # for listening the command in indian english
            print("the query is printed='", Query, "'")

        # handling the exception, so that assistant can
        # ask for telling again the command
        except Exception as e:
            print(e)
            print("Say that again sir")


translate_client = translate.Client()
text = Query
target = 'en-IN'
output = translate_client.translate(
text,
target_language=target)
print(output['translatedText'])
# Driver Code

# call the function

