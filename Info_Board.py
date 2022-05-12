#!/usr/bin/python

from tkinter import *
import tkinter.messagebox
import webbrowser
from bs4 import BeautifulSoup
import requests
from sys import getsizeof

window = Tk()
window.title("Info Board")
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width, height))

def cleanString(description):
    try:
        spaces = 0
        for i in range(0, len(description)):
            if description[i].isupper() and i != 0 and description[i-1] != " ":
                description = description[:i] + " " + description[i:]
            elif description[i:i+4] == "then" and description[i-1] != " ":
                description = description[:i] + " " + description[i:]
            if description[i] == " ":
                if spaces % 2 != 0:
                    description = description[:i] + "\r" + description[i:]
                spaces += 1
        return description
    except:
        return description

def openWeather():
    weatherWindow = Toplevel(window)
    weatherWindow.title("Weather")
    width, height = weatherWindow.winfo_screenwidth(), weatherWindow.winfo_screenheight()
    weatherWindow.geometry('%dx%d+0+0' % (width, height))
    canvas = Canvas(weatherWindow, width=width, height=height, bg="DarkBlue")

    contents = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.1944&lon=-75.2429')
    soup = BeautifulSoup(contents.text, 'html.parser')

    location = soup.find('div', class_='panel panel-default').find_next_sibling('div')
    location = location.find('h2', class_='panel-title')

    canvas.create_text(width/2, height/8, text=location.string.strip(), fill="white", font=("Helvetica 50 bold"))

    days = soup.find_all('p', class_='period-name')
    descriptions = soup.find_all('p', class_='short-desc')
    tempLows = soup.find_all('p', class_="temp temp-low")
    ##forecasts = soup.find_all('img', class_='forecast-icon')

    ##for forecast in forecasts:
       ## canvas.create_text(width/2-25, startY, text=forecast['alt'], fill="white", font=("Helvetica 15"))
      ##  startY += 50
    i = 0
    j = 0
    for day in days:
        dayName = cleanString(day.get_text())
        cleanDescription = cleanString(descriptions[i].get_text())
        canvas.create_text(width*(j/8), height/3, text=dayName, fill="white", font=("Helvetica 25 bold"))
        canvas.create_text(width*(j/8), height/2, text=cleanDescription, fill="white", font=("Helvetica 15"))
        i += 1
        j += 1

    createButton(weatherWindow, "Close")

    canvas.pack()

def openSports():
    webbrowser.open("https://www.espn.com/")

def createAllButtons():
    createButton(window, "Reminders")
    createButton(window, "Weather")
    createButton(window, "Jokes")
    createButton(window, "Sports")
    createButton(window, "Close")

def createButton(window, name):
    buttonText = StringVar()
    if name == "Reminders":
        button = Button(window, text=name, command=openWeather, height = 25, width = 50)
        button.place(x=0, y=0)
    elif name == "Weather":
        button = Button(window, text=name, command=openWeather, height = 25, width = 50)
        button.place(x=0, y=550)
    elif name == "Jokes":
        button = Button(window, text=name, command=openWeather, height = 25, width = 50)
        button.place(x=width - 480, y=0)
    elif name == "Sports":
        button = Button(window, text=name, command=openSports, height = 25, width = 50)
        button.place(x=width - 480, y=550)
    else:
        button = Button(window, text=name, command=window.destroy, width = 25, font=("Helvetica 15"))
        button.place(relx=.5, rely=.8, anchor=CENTER)

createAllButtons()

window.mainloop()