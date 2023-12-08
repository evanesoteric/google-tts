import os
from google.cloud import texttospeech

def text_to_speech_from_file(filename, output_file="output.mp3"):
    # Set your credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "api-key.json"

    # Read the text from the file
    with open(filename, "r") as file:
        text = file.read()

    # Initialize the client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code and the SSML voice gender
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Polyglot-1",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    # Select the type of audio file you want
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Write the response to an output file
    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f"Audio content written to {output_file}")

if __name__ == "__main__":
    text_to_speech_from_file("text.txt")
