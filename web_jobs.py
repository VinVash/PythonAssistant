import webbrowser
import os


def open_facebook():
    webbrowser.open("https://facebook.com")

def open_google():
    webbrowser.open("https://google.com")

def open_youtube():
    webbrowser.open("https://youtube.com")

def close_browser():
    os.system('pkill brave')

    