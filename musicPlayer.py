import pyaudio;
import wave;
import sys;
import audioop;
import speech_recognition as sr
import string
import smtplib
from email.mime.text import MIMEText
import pygame as pg;
from sys import exit
# initialising pygame and the mixer module from pygame
pg.mixer.init()
pg.init()
#opening the pygame window(needed for keyboard inputs)
pg.display.set_mode((1000,1000))
radioactive=wave.open("radioactive.wav",'rb')
jaws=wave.open("Jaws_X.wav",'rb')
RFAD=wave.open("fightMusic.wav",'rb')
#GG=wave.open("GonnaGive.mp3",'rb')
PP=wave.open("PinkPanther.wav",'rb')
WNW=wave.open("WholeNewWorld.wav",'rb')
IBS=wave.open("Itsy Bitsy Spider.wav",'rb')

mouth=pyaudio.PyAudio();

def playMusic(file):
    CHUNK=1028;
    stream=mouth.open(format = mouth.get_format_from_width(file.getsampwidth()),channels= file.getnchannels(),rate =file.getframerate(),output=True);
    stuff = file.readframes(CHUNK);
    while len(stuff) > 0:
        pg.event.pump();
        stream.write(stuff)
        stuff = file.readframes(CHUNK)
        if pg.key.get_focused():
            keys=pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                stuff=[];
    stream.stop_stream()
    stream.close()

while True:
    #Making sure event queue are updated 
	pg.event.pump();
	#if statement to check if keyboard is connected and is working
	if pg.key.get_focused():
		#setting a variable equal to the state of all the keys
		keys=pg.key.get_pressed()
		if keys[pg.K_1]:
			playMusic(radioactive);
        	print "1 WAS HIT";
		if keys[pg.K_2]:
			playMusic(jaws);
        	print "2 WAS HIT";
        if keys[pg.K_3]:
            playMusic(WNW);
            print "3 WAS HIT"
        if keys[pg.K_4]:
            playMusic(IBS);
            print "4 was hit"
