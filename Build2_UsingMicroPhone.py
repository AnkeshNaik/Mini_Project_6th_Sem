# import json
# import os
# from google.cloud import speech
# from google.cloud import translate_v2 as translate
#
#
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_service_key.json'
# speech_client = speech.SpeechClient()
#
# # Transcribing Local media File, file size< 10 mb and duration< 1 min
#
# # Step Number 1-->Loading the Media Files(local)
# media_file_name = 'KND-1.mp3'
#
# with open(media_file_name, 'rb') as f1:
#     byte_data = f1.read()
# audio_mp3 = speech.RecognitionAudio(content=byte_data)
#
# # Step Number 2-->Configure the Media Files Output
#
# config_mp3 = speech.RecognitionConfig(
#     sample_rate_hertz=48000,
#     enable_automatic_punctuation=True,
#     language_code='kn-IN',
# )
#
# ##Step3. TRanscribing the recognition
#
# response_standard_mp3 = speech_client.recognize(
#     config=config_mp3,
#     audio=audio_mp3
# )
# textFromAudio=response_standard_mp3.results[0].alternatives[0].transcript
# # print(response_standard_mp3.results[0].alternatives[0].transcript)
# print(textFromAudio)
#
# translate_client = translate.Client()
# text = textFromAudio
# target = 'en-IN'
# output = translate_client.translate(
#     text,
#     target_language=target)
# print(output['translatedText'])
#
import speech_recognition as s_r
print(s_r.__version__) # just to print the version not required
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source) #reduce noise
    audio = r.listen(source) #take voice input from the microphone
# print(r.recognize_google(audio)) #to print voice into text
print(audio)