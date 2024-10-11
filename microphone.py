import SpeechRecognition as sr
r = sr.Recognizer()
with sr.Microphone(device_index=0) as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    
    # Recognize the speech
    try:
        print("Text: " + r.recognize_google(audio_text))
    except sr.UnknownValueError:
        print("Sorry, I did not get that")
    except sr.RequestError:
        print("Sorry, the API is unreachable")
