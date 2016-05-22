import pyaudio;
import wave;
import sys;
import audioop;
import speech_recognition as sr
import string
import smtplib
from email.mime.text import MIMEText
#This program will listen and when it hears specific words will send an email telling the program running on device 2 to do something
#Play music is unneeded but I will leave it for future use possibly
USER_NAME = 'largespiderfactory@gmail.com'
PASSWORD = "DaddyLonglegs"
DEBUG = True
MESSAGE_FORMAT = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" # %(fromAddr,to,subject,text)


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

def sendEmail(recipient,message):
    #HMMMM....THIS IS TERRIBLE.  WHATEVER IT PROBABLY WILL WORK
    SMTP_SERVER_URL = 'localhost'
    mailserver = smtplib.SMTP('smtp.gmail.com:587')
    if DEBUG: 
        mailserver.set_debuglevel(1)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
    mailserver.login(USER_NAME,PASSWORD)
    mailserver.sendmail('', recipient, message)
    mailserver.close()
def sendEmailWithFields(to,subject,text):
    message = MESSAGE_FORMAT%('', to, subject, text)
    sendEmail(to,message)


#THIS IS WHERE, IF A WORD WAS DETECTED, IT WILL BE USED TO CALL AN ACTION TO TAKE.
def takeAction(word):
    if word=="radioactive" or word=="green":
        print "Radioactive detected"
        to = 'largespiderfactory@gmail.com'
        subject = 'Radioactive'
        text = ''
        sendEmailWithFields(to,subject,text)
    if word=="sneak":
        print "PLAY PINK PANTHER"
        to = 'largespiderfactory@gmail.com'
        subject = 'Spy'
        text = ''
        sendEmailWithFields(to,subject,text)
    if word=="muffet":
        print "PLAY A WHOLE NEW WORLD OR WHATEVER"
        to = 'largespiderfactory@gmail.com'
        subject = 'Ebola'
        text = ''
        sendEmailWithFields(to,subject,text)
    if word=="trying":
        print "Requiem start"
        to = 'largespiderfactory@gmail.com'
        subject = 'Fight'
        text = ''
        sendEmailWithFields(to,subject,text)
    if word=="down":
        print "Requiem start"
        to = 'largespiderfactory@gmail.com'
        subject = 'IBS'
        text = ''
        sendEmailWithFields(to,subject,text)


def checking(audio):
# This is a try catch statement in order to try to check if there is a understandable word that was said.  
    try:
        word=brain.recognize_google(audio);
        print word
        takeAction((word+"").lower())
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
        
