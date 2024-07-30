import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
            transcription = recognizer.recognize_sphinx(audio_data)  # Using Sphinx
            return transcription
    except sr.UnknownValueError:
        print("Sphinx could not understand the audio")
        return None

# Path to the converted .wav file
wav_file_path = "/Users/tadashikumazawa/Downloads/Gloria Wu, MD.wav"

transcription = transcribe_audio(wav_file_path)
if transcription:
    print(transcription)
