import pyttsx3
engine = pyttsx3.init()
voices = engine.getproperty("voices")
voice = engine.setproperty("voice"[1].id)

# text input
text = input("enter text :")

def speek(text):
    engine.say(text)
    engine.runandwait()
speek(text)