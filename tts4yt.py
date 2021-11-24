import(os)

requires google authentication - file called tts4youtube-9b5f2bd91b9c.json

{
  "type": "service_account",
  "project_id": "tts4youtube",
  "private_key_id": "PRIVATEKEYIDGOESHERE",
  "private_key": "-----BEGIN PRIVATE KEY-----\nPRIVATEKEYGOESHERE\n-----END PRIVATE KEY-----\n",
  "client_email": "SERVICEACCOUNTEMAILGOESHERE",
  "client_id": "CLIENTIDGOESHERE",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tts4youtubesvcact%40tts4youtube.iam.gserviceaccount.com"
}

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "PATHTOJSONCREDENTIALSFILEGOESHERE.json"

import pandas as pd
import os
os.getcwd()
df = pd.read_csv('vehs.csv')

list(df)
items = df['Item description']
[i.replace('*',' ') for i in items]

itemlist = items.tolist()

from google.cloud import texttospeech

#key='KEY'

# Instantiates a client
client = texttospeech.TextToSpeechClient()
responses = {}


x = 0

descriptions = [LISTOFDESCRIPTIONS]

for i in descriptions:

    x = x + 1
    
    # Remove problematic characters
    i = i.replace('*',' ')

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=i)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    with open('%s_output.mp3' % x, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file %s_output.mp3' % x)



    if x > 5:
        print("Process Completed")
        break
    else:
        print('File # ' + str(x) + ' Complete')
