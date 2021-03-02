import speech_recognition as sr
import search
import talk as t

listener = sr.Recognizer()

def run():
    command = listen()
    sCommand = command.split()
    if ch(['search', 's'], sCommand[0]) != None:
        com = ch(['search', 's'], sCommand[0])
        search.srch(command.replace(com + ' ', ''))
    elif ch(['play', 'p'], sCommand[0]) != None:
        com = ch(['play', 'p'], sCommand[0])
        search.play(command.replace(com + ' ', ''))
    else:
        t.talk("Sory, I did not understand you")
        return


def listen():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            global sound
            sound = listener.recognize_google(voice)
            sound = sound.lower()
            if sound == None:
                sound = 'empty'
    except:
        pass
    return sound

def wat():
    s = listen()
    if s == 'dorian':
        print('listening...')
        run()
    pass

def ch(cList, command):
    for x in cList:
        if x == command:
            return x
    return None

while True:
    wat()
