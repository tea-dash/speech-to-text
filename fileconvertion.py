from pydub import AudioSegment

# Path to the .m4a file
m4a_file_path = "/Users/tadashikumazawa/Downloads/Gloria Wu, MD.m4a"

# Path to save the .wav file
wav_file_path = "/Users/tadashikumazawa/Downloads/Gloria Wu, MD.wav"

# Convert .m4a to .wav
audio = AudioSegment.from_file(m4a_file_path, format="m4a")
audio.export(wav_file_path, format="wav")

print("Conversion complete!")
