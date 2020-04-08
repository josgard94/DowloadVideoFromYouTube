"""
Author: Edgard Diaz
Date: April  07th  2020

Dowload videos from YouTube with this application developed with python 3.

These modules need to be installed:

    pip install pytube3
    pip install pyinstaller 

To compile the project use
    pyinstaller  --clean --win-private-assemblies --noupx --onedir --onefile main.py

"""

from pytube import YouTube
import keyboard

url = input('Url: ') #Ingresar url del video a descargar

folder = input('Save download to: ') #ingresar la direccion donde el video se guardara

video = YouTube(url) #Obtener el video de Youtube 

print(video.title) #Mostrar el titulo del video que se descargara

stream = video.streams.first()

stream.download(folder) #Descargar video en la carpeta indicada

print('video downloaded in', folder) 

print('Presione la tecla esc para terminar.')
while True:

    if keyboard.is_pressed('esc'):
    	exit()
