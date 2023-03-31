import json
import os
from google.cloud import speech
from google.cloud import translate_v2 as translate


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_service_key.json'
speech_client = speech.SpeechClient()

# Transcribing Local media File, file size< 10 mb and duration< 1 min

# Step Number 1-->Loading the Media Files(local)
media_file_name = 'ankesh2.wav'

with open(media_file_name, 'rb') as f1:
    byte_data = f1.read()
audio_mp3 = speech.RecognitionAudio(content=byte_data)

# Step Number 2-->Configure the Media Files Output

config_mp3 = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='kn-IN',
    audio_channel_count = 2
)

##Step3. TRanscribing the recognition

response_standard_mp3 = speech_client.recognize(
    config=config_mp3,
    audio=audio_mp3
)
textFromAudio=response_standard_mp3.results[0].alternatives[0].transcript
# print(response_standard_mp3.results[0].alternatives[0].transcript)
print(textFromAudio)

translate_client = translate.Client()
text = textFromAudio
target = 'en-IN'
output = translate_client.translate(
    text,
    target_language=target)
print(output['translatedText'])

