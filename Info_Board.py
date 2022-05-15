#!/usr/bin/python

from tkinter import *
import tkinter.messagebox
import webbrowser
from bs4 import BeautifulSoup
import requests
from PIL import ImageTk, Image

window = Tk()
window.title("Info Board")
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width, height))

def cleanString(description):
    try:
        spaces = 0
        for i in range(1, len(description)):
            if description[i].isupper() and description[i-1] != " ":
                description = description[:i] + " " + description[i:]
            elif description[i:i+4] == "then" and description[i-1] != " " and description[i-1] != "\r":
                description = description[:i] + " " + description[i:]
            if description[i] == " " and spaces % 2 != 0 and description[i-1] != "\r":
                description = description[:i] + "\r" + description[i+1:]
                spaces += 1
            elif description[i] == " ":
                spaces += 1
        return description
    except:
        return description

def createWeatherPanels(index, low, high, indexLocation, days, soup, canvas, x):
    descriptions = soup.find_all('p', class_='short-desc')
    tempHighs = soup.find_all('p', class_="temp temp-high")
    tempLows = soup.find_all('p', class_="temp temp-low")

    dayName = cleanString(days[index].get_text())
    if indexLocation:
        temp = tempLows[low].get_text()
        low+=1
    else:
        temp = tempHighs[high].get_text()
        high+=1
    cleanDescription = cleanString(descriptions[index].get_text())
    weatherReport = dayName + "\r\r" + temp + "\r\r" + cleanDescription
    label = Label(canvas, text="\r" + weatherReport.strip(), width=18, height=10, anchor="n", fg="blue", bg= "white", font=("Helvetica 25 bold"))
    canvas.create_window(x, height/2, window=label)

def openWeather():
    weatherWindow = Toplevel(window)
    weatherWindow.title("Weather")
    width, height = weatherWindow.winfo_screenwidth(), weatherWindow.winfo_screenheight()
    weatherWindow.geometry('%dx%d+0+0' % (width, height))
    canvas = Canvas(weatherWindow, width=width, height=height, bg="DarkBlue")

    contents = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.1552&lon=-75.2204')
    soup = BeautifulSoup(contents.text, 'html.parser')

    location = soup.find('div', class_='panel panel-default').find_next_sibling('div')
    location = location.find('h2', class_='panel-title')
    currentTemp = soup.find('p', class_='myforecast-current-lrg')
    currentTempDescription = soup.find('p', class_='myforecast-current')
    canvas.create_text(width/2, height/8, text=location.string.strip() + ": " + currentTemp.get_text(), fill="white", font=("Helvetica 60 bold"))
    canvas.create_text(width/2, height/8 + 100, text=currentTempDescription.get_text(), fill="white", font=("Helvetica 30 bold"))
    createButton(weatherWindow, "Close")
    canvas.pack()

    days = soup.find_all('p', class_='period-name')
    x = 180
    low = 0
    high = 0
    dayName = cleanString(days[0].get_text())
    if dayName == "Tonight":
        for i in range(0, 5):
            createWeatherPanels(i, low, high, i % 2 == 0, days, soup, canvas, x)
            x += 390
    else:
        for i in range(0, 5):
            createWeatherPanels(i, low, high, i % 2 != 0, days, soup, canvas, x)
            x += 390

def openSports():
    sportsWindow = Toplevel(window)
    sportsWindow.title("Todays Lineup")
    width, height = sportsWindow.winfo_screenwidth(), sportsWindow.winfo_screenheight()
    sportsWindow.geometry('%dx%d+0+0' % (width, height))
    canvas = Canvas(sportsWindow, width=width, height=height, bg="Red")

    createButton(sportsWindow, "Close")
    canvas.pack()

    contents = requests.get('https://www.si.com/scoreboard')
    soup = BeautifulSoup(contents.text, 'html5lib')

    games = soup.find('div', title='m-scoreboard--container').find_all('phoenix-scoreboard-league')
    leagueName = soup.find_all('span', class_='event__title--name')
    print(len(leagueName), len(games))
    x = 100
    i = 0
    for game in games:
        leagueName = soup.find_all('div', class_='event--section').find('span', class_='event__title--type').get_text()
        result = game.find('div', class_='event__stage--block').get_text()
        homeTeam = game.find('div', class_='event__participant event__participant--home').get_text()
        homeTeamScore = game.find('div', class_='event__score event__score--home').get_text()
        awayTeam = game.find('div', class_='event__participant event__participant--away').get_text()
        awayTeamScore = game.find('div', class_='event__score event__score--away').get_text()
        print(leagueName + " " + homeTeam)
        label = Label(canvas, text= leagueName() + "\r" + homeTeam, width=10, height=10, anchor="n", fg="blue", bg= "white", font=("Helvetica 25 bold"))
        canvas.create_window(x, height/2, window=label)
        x +=100

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