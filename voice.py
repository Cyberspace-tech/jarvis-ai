import tempfile
import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel
import pyttsx3

engine = pyttsx3.init()

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():

    print("🎤 Listening...")

    duration = 5
    sample_rate = 16000

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ) as temp_file:

        sf.write(
            temp_file.name,
            audio,
            sample_rate
        )

        segments, _ = model.transcribe(
    temp_file.name,
    task="transcribe"
)



    text = " ".join(
        segment.text for segment in segments
    )

    print("You:", text)

    return text