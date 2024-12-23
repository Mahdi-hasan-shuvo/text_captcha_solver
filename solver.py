from time import sleep  
import speech_recognition as sr  
import sounddevice as sd  
import io  
import wave  

# Set parameters  
duration = 8  # seconds  
sample_rate = 44100  
channels = 2  
def record_audio():
    # Record audio  
    # sleep(2)  # Sleep for 2 seconds before recording  
    print("Waite ...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='int16')  
    sd.wait()  # Wait until recording is finished  
    # print("Recording finished.")  
    # Create an in-memory WAV buffer  
    buffer = io.BytesIO()  
    with wave.open(buffer, 'wb') as wf:  
        wf.setnchannels(channels)  
        wf.setsampwidth(2)  # 16-bit audio  
        wf.setframerate(sample_rate)  
        wf.writeframes(audio.tobytes())  
    # Recognize speech  
    buffer.seek(0)  
    recognizer = sr.Recognizer()  
    with sr.AudioFile(buffer) as source:  
        audio_data = recognizer.record(source)  
        try:  
            text = recognizer.recognize_google(audio_data)  
            # print("Recognized text:", text.strip())  
            return text.strip()
        except sr.UnknownValueError:  
            print("Could not understand audio")  
        except sr.RequestError as e:  
            print(f"Request error; {e}")

    

