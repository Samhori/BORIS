import pyaudio;
import wave;
import sys;
import audioop;
import speech_recognition as sr

radioactive=wave.open("radioactive.wav",'rb')
jaws=wave.open("Jaws_X.wav",'rb')
RFAD=wave.open("fightMusic.wav",'rb')
#GG=wave.open("GonnaGive.mp3",'rb')
PP=wave.open("PinkPanther.wav",'rb')
WNW=wave.open("WholeNewWorld.wav",'rb')

brain = sr.Recognizer()
ears=sr.Microphone()
mouth=pyaudio.PyAudio();

def playMusic(file):
    CHUNK=1028;
    stream=mouth.open(format = mouth.get_format_from_width(file.getsampwidth()),channels= file.getnchannels(),rate =file.getframerate(),output=True);
    stuff = file.readframes(CHUNK);
    while len(stuff) > 0:
        stream.write(stuff)
        stuff = file.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
         

#THIS IS WHERE, IF A WORD WAS DETECTED, IT WILL BE USED TO CALL AN ACTION TO TAKE.
def takeAction(word):
    if word=="Radioactive":
        playMusic(radioactive);
    if word=="fight":
        playMusic(RFAD);
    if word=="shark":
	playMusic(jaws);
    if word=="spy":
	playMusic(PP);
    if word=="world":
	playMusic(WNW);


def checking(audio):
# This is a try catch statement in order to try to check if there is a understandable word that was said.  
    try:
        word=brain.recognize_google(audio);
        print word
        takeAction(word)
    except sr.UnknownValueError:
        print "SPEAK CLEARER AND BE BETTER"
    except sr.RequestError as e:
        print "DIDN'T WORK"

#Adjusting for background noise
with ears as source:
    brain.adjust_for_ambient_noise(source)
#This is how long to wait before finishing the phrase. Default is .8
brain.pause_threshold = 0.5
#checking for sound and passing it into checking in a infinite loop.
while True:
    with ears as source:
        #print("LISTENING!");
        audio = brain.listen(source);
        checking(audio)
mouth.terminate();
        
