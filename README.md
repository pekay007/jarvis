# Jarvis (Just A Rather Very Intelligent System)

A Personal Assistant for Linux, MacOS and Windows

Jarvis is a simple personal assistant for Linux, MacOS and Windows which works on the command line. He can talk to you if you enable his voice. He can tell you the News, he can find locations and other places near you. He can do some great stuff like scientific calculations for you.

## Getting Started

In order to start Jarvis just clone [this repository](https://github.com/pekay007/jarvis.git) and run `python installer`.

Run **Jarvis** from anywhere by command `jarvis`

On Mac OS X run `source jarvis1.0.py`

On Windows run `jarvis1.0.py`

You can start by double clicking and opening jarvis1.0.py


## Optional Dependencies

- Any pyttsx3 text-to-speech engine (``sapi5, nsss or espeak``) for Jarvis to talk out loud (e.g. Ubuntu do ``sudo apt install espeak``)
- Portaudio + python-devel packages for voice control
- ``notify-send`` on Linux if you want to receive *nice* and desktop-notification instead of *ugly* pop up windows (e.g. Ubuntu do ``sudo apt install libnotify-bin``)
- ``ffmpeg`` if you want ``music`` to download songs as .mp3 instead of .webm


## Steps To Install 


`sudo apt install python3`

`sudo apt install python3-pip`

`git clone https://github.com/pekay007/jarvis.git`

`cd jarvis`

`sudo pip install virtualenv`

`pip install pyttsx3`

`pip install speechRecognition`

`pip install wikipedia`

`pip install psutil`

`pip install pyjokes`

`pip install pyautogui`

`pip install wolframalpha`

`python3 jarvis1.0.py`


