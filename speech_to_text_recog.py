import speech_recognition as sr
from time import sleep


def assistant():
    r = sr.Recognizer()

    # The filename will represent the audio file to be read. input your desired clear audio and put here:

    audioFile = sr.AudioFile('Filename.wav')
    with audioFile as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        print("Reading inputs...")

    try:
        call = r.recognize_google(audio, language='en-Us')
        sleep(1)
        print("\n")
        print(call)

    except :
        print("An error occured. Invalid network")

        return "None"

    return call

call = assistant()
sleep(4)
print("Exitting...")
sleep(2)
