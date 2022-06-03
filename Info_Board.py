#!/usr/bin/python

from tkinter import *
import tkinter.messagebox
import webbrowser
from bs4 import BeautifulSoup
import requests
import math
import time
from datetime import datetime
from tkinter.ttk import Style
from tkinter import ttk
import mysql.connector
from mysql import connector
from selenium import webdriver

window = Tk()
window.title("Info Board")
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width, height))
window.configure(bg="black")


def cleanString(description):
    try:
        spaces = 0
        for i in range(1, len(description)):
            if description[i].isupper() and description[i - 1] != " ":
                description = description[:i] + " " + description[i:]
            elif description[i:i + 4] == "then" and description[i - 1] != " " and description[i - 1] != "\r":
                description = description[:i] + " " + description[i:]
            if description[i] == " " and spaces % 2 != 0 and description[i - 1] != "\r":
                description = description[:i] + "\r" + description[i + 1:]
                spaces += 1
            elif description[i] == " ":
                spaces += 1
        return description
    except:
        return description


def apostropheFixer(string):
    try:
        sum = 0
        for i in range(0, len(string)):
            i += sum
            if string[i] == "\'" or string[i] == "\"":
                string = string[:i] + "\\" + string[i:]
                sum += 1
        return string
    except:
        return string


def createWeatherPanels(index, indexLocation, days, soup, canvas, x, hazard):
    descriptions = soup.find_all('p', class_='short-desc')
    if hazard:
        descriptions.pop(0)
    tempHighs = soup.find_all('p', class_="temp temp-high")
    tempLows = soup.find_all('p', class_="temp temp-low")
    low = 0
    high = 0

    dayName = cleanString(days[index].get_text())
    if indexLocation:
        temp = tempLows[low].get_text()
        low += 1
    else:
        temp = tempHighs[high].get_text()
        high += 1
    cleanDescription = cleanString(descriptions[index].get_text())
    weatherReport = dayName + "\r\r" + temp + "\r\r" + cleanDescription
    label = Label(canvas, text="\r" + weatherReport.strip(), width=18, height=10, anchor="n", fg="blue", bg="white",
                  font=("Helvetica 25 bold"), wraplength=300)
    canvas.create_window(x, height / 2, window=label)


def openWeather():
    weatherWindow = Toplevel(window)
    weatherWindow.title("Weather")
    width, height = weatherWindow.winfo_screenwidth(), weatherWindow.winfo_screenheight()
    weatherWindow.geometry('%dx%d+0+0' % (width, height))

    setLocation(weatherWindow, None, 'https://forecast.weather.gov/MapClick.php?lat=40.1552&lon=-75.2204')


def setLocation(window, canvas, website):
    try:
        canvas.destroy()
    except:
        print()
    canvas = Canvas(window, width=width, height=height, bg="DarkBlue")

    contents = requests.get(website)
    soup = BeautifulSoup(contents.text, 'html.parser')

    location = soup.find('div', class_='panel panel-default').find_next_sibling('div')
    location = location.find('h2', class_='panel-title')
    currentTemp = soup.find('p', class_='myforecast-current-lrg')
    currentTempDescription = soup.find('p', class_='myforecast-current')
    canvas.create_text(width / 2, height / 8, text=location.string.strip() + ": " + currentTemp.get_text(),
                       fill="white", font=("Helvetica 60 bold underline"))
    canvas.create_text(width / 2, height / 8 + 100, text=currentTempDescription.get_text(), fill="white",
                       font=("Helvetica 30 italic"))
    createButton(window, "Close")
    canvas.pack()

    days = soup.find_all('p', class_='period-name')
    x = width / 10
    hazard = False
    if "NOW" in days[0].get_text():
        days.pop(0)
        hazard = True
    dayName = cleanString(days[0].get_text())

    if dayName == "Times":
        for i in range(0, 5):
            createWeatherPanels(i, i % 2 == 0, days, soup, canvas, x, hazard)
            x += (width * (1 / 5))
    else:
        for i in range(0, 5):
            createWeatherPanels(i, i % 2 != 0, days, soup, canvas, x, hazard)
            x += (width * (1 / 5))

    newLocationButton = Button(window, text="Set Location", wraplength=100, justify=CENTER,
                        command=lambda: setLocation(window, canvas, )font=("Helvetica 25 bold"), bg="white", fg="DarkBlue")
    newLocationButton.place(relx=.6, rely=.1, anchor=CENTER)

    entryBox = Entry(window)
    canvas.create_window(width/2, height/10, window = entryBox)


def openGames():
    print()


def connectToMySQL():
    cnx = mysql.connector.connect(password='vito', user='vito')
    cursor = cnx.cursor()
    return cursor, cnx


def openJokesAndRiddles():
    JokesAndRiddlesWindow = Toplevel(window)
    JokesAndRiddlesWindow.title("Today's Lineup")
    width, height = JokesAndRiddlesWindow.winfo_screenwidth(), JokesAndRiddlesWindow.winfo_screenheight()
    JokesAndRiddlesWindow.geometry('%dx%d+0+0' % (width, height))
    canvas = Canvas(JokesAndRiddlesWindow, width=width, height=height, bg="Yellow")
    buttonWidth = int(width * .02604167)
    createButton(JokesAndRiddlesWindow, "Close")
    canvas.pack()

    DB_NAME = 'JokesAndRiddles'
    cursor, connection = connectToMySQL()

    cursor.execute("USE {}".format(DB_NAME))

    cursor.execute("SELECT riddle FROM Riddles ORDER BY RAND() LIMIT 1")
    riddle = cursor.fetchone()
    riddle = riddle[0]

    riddleLabel = Label(canvas, text=riddle, width=28, height=7, fg="black", bg="yellow", font=("Times 45 bold"),
                        wraplength=700, justify=CENTER)
    canvas.create_window(width / 4.5, height * .225, window=riddleLabel)

    riddle = apostropheFixer(riddle)

    answerLabel = Label(canvas, width=22, height=7, bg="yellow", font=("Times 45 bold"), wraplength=300, justify=CENTER)
    canvas.create_window(width / 4.5, height * .7, window=answerLabel)

    cursor.execute("SELECT body, id FROM Jokes ORDER BY RAND() LIMIT 1")
    joke = cursor.fetchone()
    jokeId = joke[1]
    joke = joke[0]



    jokeLabel = Label(canvas, text=joke, fg="black", bg="yellow", font=("Times 45 bold"), wraplength=700,
                      justify=CENTER)
    canvas.create_window(width * .8, height * .25, window=jokeLabel)

    jokeButton = Button(JokesAndRiddlesWindow, text="New Joke", wraplength=50, justify=CENTER,
                        command=lambda: newJoke(jokeLabel, deleteButton), font=("Helvetica 15"), bg="cyan", fg="black")
    jokeButton.place(relx=.6, rely=.25, anchor=CENTER)

    deleteButton = Button(JokesAndRiddlesWindow, text="X", justify=CENTER,
                          command=lambda: deleteJoke(jokeLabel, jokeId, deleteButton), font=("Helvetica 20 bold"),
                          bg="Red", fg="black")
    deleteButton.place(relx=.6, rely=.1, anchor=CENTER)

    answerButton = Button(JokesAndRiddlesWindow, text="Show Answer", command=lambda: showAnswer(riddle, answerLabel),
                          width=int(buttonWidth / 2), font=("Helvetica 15"), bg="green", fg="white")
    answerButton.place(relx=.22, rely=.5, anchor=CENTER)

    riddleButton = Button(JokesAndRiddlesWindow, text="New Riddle", wraplength=60, justify=CENTER,
                          command=lambda: newRiddle(riddleLabel, answerLabel, answerButton),
                          font=("Helvetica 15"), bg="cyan", fg="black")
    riddleButton.place(relx=.1, rely=.5, anchor=CENTER)

    entryBox = Entry(JokesAndRiddlesWindow)
    canvas.create_window(width/2, height * .75, window = entryBox)

    addJokeButton = Button(JokesAndRiddlesWindow, text="Add Joke", wraplength=60, justify=CENTER,
                          command=lambda: addJoke(jokeLabel, deleteButton, entryBox),
                          font=("Helvetica 15"), bg="purple", fg="white")
    addJokeButton.place(relx=.5, rely=.5, anchor=CENTER)

def addJoke(jokeLabel, deleteButton, entryBox):
    DB_NAME = 'JokesAndRiddles'
    cursor, connection = connectToMySQL()

    cursor.execute("USE {}".format(DB_NAME))
    cursor.execute("SELECT MAX(id) FROM Jokes")
    maxId = cursor.fetchone()
    maxId = maxId[0] + 1
    cursor.execute("INSERT INTO Jokes VALUES(\"{}\", \"Original\", {}, \"?\")".format(entryBox.get(), maxId))
    connection.commit()

    cursor.execute("SELECT body, id FROM Jokes WHERE id = {}".format(maxId))
    joke = cursor.fetchone()
    jokeId = joke[1]
    joke = joke[0]
    jokeLabel.configure(text=joke)
    deleteButton.configure(command=lambda: deleteJoke(jokeLabel, jokeId, deleteButton))
    entryBox.delete(0,END)

def newJoke(jokeLabel, deleteButton):
    DB_NAME = 'JokesAndRiddles'
    cursor, connection = connectToMySQL()

    cursor.execute("USE {}".format(DB_NAME))

    cursor.execute("SELECT body, id FROM Jokes ORDER BY RAND() LIMIT 1")
    joke = cursor.fetchone()
    jokeId = joke[1]
    joke = joke[0]
    jokeLabel.configure(text=joke)
    deleteButton.configure(command=lambda: deleteJoke(jokeLabel, jokeId, deleteButton))


def deleteJoke(jokeLabel, jokeId, deleteButton):
    DB_NAME = 'JokesAndRiddles'
    cursor, connection = connectToMySQL()

    cursor.execute("USE {}".format(DB_NAME))
    cursor.execute("DELETE FROM Jokes WHERE id = {}".format(jokeId))
    connection.commit()
    ## add script to acess terminal to update joke dump file

    cursor.execute("SELECT body, id FROM Jokes ORDER BY RAND() LIMIT 1")
    joke = cursor.fetchone()
    jokeId = joke[1]
    joke = joke[0]
    jokeLabel.configure(text=joke)
    deleteButton.configure(command=lambda: deleteJoke(jokeLabel, jokeId, deleteButton))


def newRiddle(riddleLabel, answerLabel, button):
    DB_NAME = 'JokesAndRiddles'
    cursor, connection = connectToMySQL()

    cursor.execute("USE {}".format(DB_NAME))

    cursor.execute("SELECT riddle FROM Riddles ORDER BY RAND() LIMIT 1")
    riddle = cursor.fetchone()
    riddle = riddle[0]

    riddleLabel.configure(text=riddle)

    answerLabel.configure(text="", bg="yellow")

    button.configure(command=lambda: showAnswer(riddle, answerLabel))


def showAnswer(riddle, answerLabel):
    DB_NAME = 'JokesAndRiddles'
    cursor, connection = connectToMySQL()

    cursor.execute("USE {}".format(DB_NAME))
    cursor.execute("SELECT answer FROM Riddles WHERE riddle = \'{}\'".format(riddle))
    answer = cursor.fetchone()
    answerLabel.configure(text=answer[0], fg="black", bg="yellow")


def openReminders():
    remindersWindow = Toplevel(window)
    remindersWindow.title("Remember Me!")
    width, height = remindersWindow.winfo_screenwidth(), remindersWindow.winfo_screenheight()
    remindersWindow.geometry('%dx%d+0+0' % (width, height))
    canvas = Canvas(remindersWindow, width=width, height=height, bg="ForestGreen")
    createButton(remindersWindow, "Close")
    canvas.pack()


    createReminderLists(remindersWindow, canvas,
                        readReminders("/home/pi/Desktop/InfoBoard/reminders.txt"), [], "/home/pi/Desktop/InfoBoard/reminders.txt", None)

def addToList(window, canvas, buttonsList, entryBox, list, fileName):
    if "-" in entryBox.get():
        list.append(entryBox.get()+"\n")
    file = open(fileName, "w")
    file.truncate(0)
    for element in list:
        file.write(element)
    file.close()
    createReminderLists(window,canvas,list, buttonsList, fileName, entryBox)

def createReminderLists(window, canvas, list, buttonsList, fileName, entryBox):
    try:
        for button in buttonsList:
            button.destroy()
        entryBox.destroy()
    except:
        print()
    canvas.delete("all")

    y = height / 6
    i = 0
    tempList = list

    entryBox = Entry(window)
    canvas.create_window(width/2, 50, window = entryBox)

    for element in list:
        elementText = element.split("-")
        label = Label(window, text=elementText[0].strip(), anchor = 'w', fg = "white", bg = "ForestGreen",
                      font=("Helvetica 25 bold"))
        canvas.create_window(200, y, window=label)
        doneButton = Button(window, text=elementText[1].strip(), justify=CENTER, width = 5,
                            command=lambda index=i, currButtons = buttonsList: createReminderLists(window, canvas, newList(index, tempList), currButtons, fileName, entryBox),
                            font=("Helvetica 25 bold"), bg="red", fg="white")
        doneButton.place(relx=.8, y=y, anchor=CENTER)
        buttonsList.append(doneButton)
        y += 60
        i += 1

    file = open(fileName, "w")
    file.truncate(0)
    for element in list:
        file.write(element)
    file.close()


    addButton = Button(window, text="Add", justify=CENTER, width=5, command=lambda: addToList(window, canvas, buttonsList, entryBox, list, fileName), bg="white", fg="ForestGreen")
    addButton.place(x=width * (3/4), y=50, anchor=CENTER)
    buttonsList.append(addButton)


    remindersButton = Button(window, text="Reminders", justify=CENTER, width = 10,
                            command=lambda currButtons = buttonsList: createReminderLists(window, canvas,
                                readReminders("/home/pi/Desktop/InfoBoard/reminders.txt"), currButtons, "/home/pi/Desktop/InfoBoard/reminders.txt", entryBox), font=("Helvetica 25 bold"), bg="white", fg="ForestGreen")
    movieButton = Button(window, text="Movies", justify=CENTER, width = 10,
                            command=lambda currButtons = buttonsList: createReminderLists(window, canvas,
                                readReminders("/home/pi/Desktop/InfoBoard/movieReminders.txt"), currButtons, "/home/pi/Desktop/InfoBoard/movieReminders.txt", entryBox), font=("Helvetica 25 bold"), bg="white", fg="ForestGreen")
    remindersButton.place(relx=.9, rely= .05, anchor=CENTER)
    movieButton.place(relx=.1, rely=.05, anchor=CENTER)

def newList(index, list):
    list.pop(index)
    return list


def readReminders(inputFile):
    file = open(inputFile, "r")
    reminders = file.readlines()
    return reminders


def createAllButtons():
    createButton(window, "Reminders")
    createButton(window, "Weather")
    createButton(window, "Jokes/Riddles")
    createButton(window, "Games")
    createButton(window, "Close")


def createButton(window, name):
    buttonText = StringVar()
    buttonWidth = int(width * .02604167)
    buttonHeight = int(height * .02314815)

    if name == "Reminders":
        button = Button(window, text=name, command=openReminders, height=buttonHeight, width=buttonWidth,
                        bg="ForestGreen", fg="white")
        button.place(x=0, y=0)
    elif name == "Weather":
        button = Button(window, text=name, command=openWeather, height=buttonHeight, width=buttonWidth, bg="DarkBlue",
                        fg="white")
        button.place(x=0, rely=.5)
    elif name == "Jokes/Riddles":
        button = Button(window, text=name, command=openJokesAndRiddles, height=buttonHeight, width=buttonWidth,
                        bg="yellow", fg="black")
        button.place(relx=.75, y=0)
    elif name == "Games":
        button = Button(window, text=name, command=openGames, height=buttonHeight, width=buttonWidth, bg="magenta",
                        fg="white")
        button.place(relx=.75, rely=.5)
    else:
        button = Button(window, text=name, command=window.destroy, width=int(buttonWidth / 2), font=("Helvetica 15"),
                        bg="red", fg="white")
        button.place(relx=.5, rely=.8, anchor=CENTER)


createAllButtons()

##need to make a label then just call "tieRefresh right after"
def timeRefresh():
    date = datetime.now()
    currentTime = time.strftime("%I:%M:%S %p", time.localtime())
    currentDate = date.strftime("%m/%d")
    label.config(text=currentTime + "\r" + currentDate)
    window.after(1000, timeRefresh)


font = ('Arial', 80)
label = Label(window, font=font, fg="white", bg="black")
label.place(relx=.5, rely=.45, anchor=CENTER)

timeRefresh()

window.mainloop()