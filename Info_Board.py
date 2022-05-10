#!/usr/bin/python

from tkinter import *
import tkinter.messagebox
import webbrowser

top = Tk()
top.title("Info Board")
top.geometry('1000x1000+250+250')


def openWeather():
    webbrowser.open('https://weather.com/weather/today/l/0bf9c2fb36e8620ba2743f3959a103d36e9ddab6fe86c9b47940cc129e36af97')

labelText = StringVar()
labelText.set("Reminders")
labelReminders = Label(top, textvariable=labelText, height=4)
labelReminders.pack()

reminderButtonText = StringVar()
reminderButton = Button(top, text="Reminders", width=50)
reminderButton.pack()

weatherButtonText = StringVar()
weatherButton = Button(top, text="Weather", width=50, command=openWeather)
weatherButton.pack()

jokeButtonText = StringVar()
jokeButton = Button(top, text="Jokes", width=50)
jokeButton.pack()

sportsButtonText = StringVar()
sportsButton = Button(top, text="Sports Scores", width=50)
sportsButton.pack()

closeButtonText = StringVar()
closeButton = Button(top, text="Close", width=25, command=top.destroy)
closeButton.pack()

top.mainloop()

