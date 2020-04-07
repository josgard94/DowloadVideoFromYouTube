"""
Author: Edgard Diaz
Date: April  07th  2020

Dowload videos from YouTube with this application developed with python 3.

These modules need to be installed:

    pip installa pytube3
    pip install pyinstaller 

To compile the project use
    pyinstaller  --clean --win-private-assemblies --noupx --onedir --onefile main.py

"""

from pytube import YouTube
import keyboard

url = input('Url: ')

folder = input('Save download to: ')

video = YouTube(url)

print(video.title)

stream = video.streams.first()

stream.download(folder)

print('Video descargado')

print('Presione la tecla esc para terminar.')
while True:

    if keyboard.is_pressed('esc'):
    	exit()

exit()
