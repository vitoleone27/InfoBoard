#!/usr/bin/python

from tkinter import *
import tkinter.messagebox
import webbrowser

window = Tk()
window.title("Info Board")
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width, height))

def openWeather():
    webbrowser.open('https://weather.com/weather/today/l/0bf9c2fb36e8620ba2743f3959a103d36e9ddab6fe86c9b47940cc129e36af97')

def createAllButtons():
    createButton(window, "Reminders", 0, 0)
    createButton(window, "Weather", 0, 550)
    createButton(window, "Jokes", width - 450, 0)
    createButton(window, "Sports", width - 450, 550)
    createButton(window, "Close", 850, 700)

def createButton(window, name, x, y):
    if name == "Reminders":
        button = Button(window, text=name, command=openWeather, height = 25, width = 50)
    elif name == "Weather":
        button = Button(window, text=name, command=openWeather, height = 25, width = 50)
    elif name == "Jokes":
        button = Button(window, text=name, command=openWeather, height = 25, width = 50)
    elif name == "Sports":
        button = Button(window, text=name, command=openWeather, height = 25, width = 50)
    else:
        button = Button(window, text=name, command=window.destroy, width = 25)
    button.place(x=x, y=y)

createAllButtons()

window.mainloop()