"""
Synthesizes speech from the AI Text

Google link
https://cloud.google.com/text-to-speech

"""
import os

from google.cloud import texttospeech
from google.cloud import texttospeech_v1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your_json_filename.json"


# Instantiates a client
client = texttospeech_v1.TextToSpeechClient()

text="""
Put your text here that you want to convert to Voice
"""

# Set the text input to be synthesized
synthesis_input = texttospeech_v1.SynthesisInput(text=text)

# Build the voice request, select the language code ("en-US") and the ssml

# Choose a voice based on this link: https://cloud.google.com/text-to-speech/docs/voices

voice = texttospeech_v1.VoiceSelectionParams(
    language_code="en-US", 
    name="en-US-Wavenet-F"
)

# Select the type of audio file you want returned
audio_config = texttospeech_v1.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

output_name = "special_001.mp3"
# The response's audio_content is binary.
with open(output_name, "wb") as out:
    # Write the response to the output mp3 file.
    out.write(response.audio_content)
    print('Audio content written to file ' + output_name)