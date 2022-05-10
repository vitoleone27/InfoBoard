#!/usr/bin/python

from tkinter import *
import tkinter.messagebox
import webbrowser
from bs4 import BeautifulSoup
import requests

window = Tk()
window.title("Info Board")
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width, height))

def openWeather():
    weatherWindow = Toplevel(window)
    weatherWindow.title("Weather")
    width, height = weatherWindow.winfo_screenwidth(), weatherWindow.winfo_screenheight()
    weatherWindow.geometry('%dx%d+0+0' % (width, height))
    canvas = Canvas(weatherWindow, width=width, height=height, bg="DarkBlue")

    contents = requests.get('http://forecast.weather.gov/MapClick.php?lat=40.6222&lon=-75.3932')
    soup = BeautifulSoup(contents.text, 'html.parser')

    locations = soup.find('div', class_='panel panel-default').find_next_sibling('div')
    locations = locations.find('h2', class_='panel-title')
    canvas.create_text(850, 100, text=locations.string, fill="white", font=("Helvetica 15 bold"))

    forecasts = soup.find_all('img', class_='forecast-icon')
    startY = 200
    for forecast in forecasts:
        canvas.create_text(850, startY, text=forecast['alt'], fill="white", font=("Helvetica 15 bold"))
        startY += 50

    createButton(weatherWindow, "Close", 850, 700)

    canvas.pack()

def openSports():
    webbrowser.open("https://www.espn.com/")

def createAllButtons():
    createButton(window, "Reminders", 0, 0)
    createButton(window, "Weather", 0, 550)
    createButton(window, "Jokes", width - 450, 0)
    createButton(window, "Sports", width - 450, 550)
    createButton(window, "Close", 850, 700)

def createButton(window, name, x, y):
    buttonText = StringVar()
    if name == "Reminders":
        button = Button(window, text=name, command=openWeather, height = 25, width = 50)
    elif name == "Weather":
        button = Button(window, text=name, command=openWeather, height = 25, width = 50)
    elif name == "Jokes":
        button = Button(window, text=name, command=openWeather, height = 25, width = 50)
    elif name == "Sports":
        button = Button(window, text=name, command=openSports, height = 25, width = 50)
    else:
        button = Button(window, text=name, command=window.destroy, width = 25)
    button.place(x=x, y=y)

createAllButtons()

window.mainloop()