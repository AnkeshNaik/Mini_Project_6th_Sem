import os
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_service_key.json'

translate_client = translate.Client()
text = 'Good Morning. GoodBye. And Hello'
target = 'bn'
output = translate_client.translate(
    text,
    target_language=target)
print(output)
