import urllib2
import pyaudio;
import wave;
import sys;
import audioop;
import speech_recognition as sr
import urllib           
import feedparser         
import imaplib
import smtplib
from email.mime.text import MIMEText

username = "largespiderfactory@gmail.com"
password = "DaddyLonglegs"
DEBUG = True
MESSAGE_FORMAT = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" # %(fromAddr,to,subject,text)

radioactive=wave.open("radioactive.wav",'rb')
jaws=wave.open("Jaws_X.wav",'rb')
RFAD=wave.open("fightMusic.wav",'rb')
#GG=wave.open("GonnaGive.mp3",'rb')
PP=wave.open("PinkPanther.wav",'rb')
WNW=wave.open("WholeNewWorld.wav",'rb')

mouth=pyaudio.PyAudio();


def playMusic(file):
    CHUNK=1028;
    stream=mouth.open(format = mouth.get_format_from_width(file.getsampwidth()),channels= file.getnchannels(),rate =file.getframerate(),output=True);
    stuff = file.readframes(CHUNK);
    while len(stuff) > 0:
        # TODO:  ADD A CANCEL BUTTON.  PROBABLY USING PYGAME.  
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
    mailserver.login(username,password)
    mailserver.sendmail('', recipient, message)
    mailserver.close()
def sendEmailWithFields(to,subject,text):
    message = MESSAGE_FORMAT%('', to, subject, text)
    sendEmail(to,message)
_URL = "https://mail.google.com/gmail/feed/atom"
class my_opener (urllib.FancyURLopener):
    # Override
    def get_user_passwd(self, host, realm, clear_cache=0):
        return (username, password)
def auth():
    opener = my_opener()
    f = opener.open(_URL)
    feed = f.read()
    return feed

def readmail(feed):
    atom = feedparser.parse(feed)
    try:
        print atom.entries[0].title;
        return atom.entries[0].title;
    except:
        return "NONE"

def react(word):
    if(word=="PLEASE WAIT" or word=="NONE"):
        print "WAITING";
    else:
        #SEND EMAIL TO AVOID CONFUSION
        to = 'largespiderfactory@gmail.com'
        subject = 'PLEASE WAIT'
        text = ''
        sendEmailWithFields(to,subject,text)
    if(word=='Radioactive'):
        playMusic(jaws);
    if(word=='Fight'):
        playMusic(RFAD);
    if(word=='Spy'):
        playMusic(PP);
    if(word=='Ebola'):
        playMusic(WNW);
    


while True:
    key=auth();
    instructions=readmail(key);
    react(instructions)

  

    
    