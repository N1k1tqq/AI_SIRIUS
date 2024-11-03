from pydub import AudioSegment
from vosk import Model, KaldiRecognizer
import wave


model_path = 'model/vosk-model-ru-0.42'

model = Model(model_path)

def mp3_to_wav(input_audio_filepath, output_audio_filepath):
    audio = AudioSegment.from_file(input_audio_filepath)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)
    audio.export(output_audio_filepath, format="wav", parameters=["-acodec", "pcm_s16le"])


def transcribe_audio(file_path):
    wf = wave.open(file_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            print("Процесс распознавания...")
    result = rec.FinalResult()
    return result

input_audio_filepath = 'files/audio.mp3'
output_audio_filepath = 'files/output_audio.wav'
mp3_to_wav(input_audio_filepath, output_audio_filepath)
audio_file_path = 'files/output_audio.wav'
text = transcribe_audio(audio_file_path)


with open("files/transcribed_text.txt", "w") as text_file:
    text_file.write(text)
    print("Текст успешно сохранен в файл 'transcribed_text.txt'.")
with open("files/transcribed_text.txt", "r") as text_file:
    lines = text_file.readlines()
    with open("files/resolt.txt", "w") as resolt:
        resolt.write(lines[-2][12:-2:])