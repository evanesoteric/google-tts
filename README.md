# Google-TTS
### Use Google's Cloud Text-to-Speech (TTS) API to generate audio files from a text document with Python.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## How to use
- Clone this repository
    ```git clone https://github.com/ArcaneSolutionsLLC/google-tts.git```
- Create a virtual environment
    ```python -m venv venv```
- Install the required packages
    ```pip install -r requirements.txt```
- Create a [Google Cloud Text-to-Speech](https://console.cloud.google.com/apis/api/texttospeech.googleapis.com) app
- Create a Google API [Service Account](https://console.cloud.google.com/apis/api/texttospeech.googleapis.com/credentials)
- Download the service account JSON key to the project directory
- Add your text to the _text.txt_ file
- Run the app
    ```python app.py```
- Listen to the generated audio file _output.mp3_

Alternatively you can use the provided _run.sh_ file to do the following in a single command:
- Overwrite _text.txt_ file with your clipboard contents
- Run _app.py_ to convert the text to audio
- Stream the audio
 
The _run.sh_ script requires that _xsel_ and _vlc_ are installed.

[Supported Voices and Languages](https://cloud.google.com/text-to-speech/docs/voices)
