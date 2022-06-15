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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import turtle

window = Tk()
window.update_idletasks()
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
    weatherWindow.title("Da Weather")
    width, height = weatherWindow.winfo_screenwidth(), weatherWindow.winfo_screenheight()
    weatherWindow.geometry('%dx%d+0+0' % (width, height))

    setLocation(weatherWindow, None, 'https://forecast.weather.gov/MapClick.php?lat=40.1552&lon=-75.2204', None, None, )


def setLocation(window, canvas, website, entryBox, newLocationButton):
    try:
        canvas.destroy()
        entryBox.destroy()
        newLocationButton.destroy()
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

    if dayName == "Times" or 'night' in dayName:
        for i in range(0, 5):
            createWeatherPanels(i, i % 2 == 0, days, soup, canvas, x, hazard)
            x += (width * (1 / 5))
    else:
        for i in range(0, 5):
            createWeatherPanels(i, i % 2 != 0, days, soup, canvas, x, hazard)
            x += (width * (1 / 5))

    entryBoxWeather = Entry(window, font=("Helvetica 20"))
    entryBoxWeather.insert(0, "Format: Zip or City/Twp")
    entryBoxWeather.bind("<FocusIn>", lambda event: entryBoxWeather.delete(0, "end"))
    canvas.create_window(width / 2, height / 20, window=entryBoxWeather)


    newLocationButton = Button(window, text="Set Location", wraplength=200, justify=CENTER,
                        command=lambda: changeLocation(window, canvas, website, entryBoxWeather, newLocationButton),
                               font=("Helvetica 20 bold"), bg="white", fg="DarkBlue")
    newLocationButton.place(relx=.65, rely=.05, anchor=CENTER)



def changeLocation(window, canvas, website, entryBox, newLocationButton):
    op = Options()
    op.add_argument('--headless')
    driver = webdriver.Chrome(options=op)
    driver.implicitly_wait(.5)
    driver.get(website)

    textBox = driver.find_element(By.ID, "inputstring")
    textBox.send_keys(entryBox.get())

    selection = driver.find_element(By.CLASS_NAME, "autocomplete-suggestion")
    selection.click()


    website = driver.current_url
    setLocation(window, canvas, website, entryBox, newLocationButton)

    entryBox.insert(0, "Format: Zip or City/Twp")
    entryBox.bind("<FocusIn>", lambda event: entryBox.delete(0, "end"))

def openGames(value):
    if value == 1:
        setUpSudoku()
    elif value == 2:
        setUpFlappyBird()
    elif value == 3:
        setUpPong()


def setUpSudoku():
    sudokuWindow = Toplevel(window)
    sudokuWindow.title("How Smart Are Ya")
    width, height = sudokuWindow.winfo_screenwidth(), sudokuWindow.winfo_screenheight()
    sudokuWindow.geometry('%dx%d+0+0' % (width, height))
    canvas = Canvas(sudokuWindow, width=width, height=height, bg="Magenta")
    canvas.pack()

    createButton(sudokuWindow, "Close")

    background = Label(canvas, bg = "black", width = 84, height = 86)
    canvas.create_window(width * .5, height * .075, window=background)

    entryBoxList = []
    global correct
    correct = False
    xInc = 0
    for i in range(0,9):
        entryBox = Entry(canvas, font=("Helvetica 50 bold"), width = 2)
        canvas.create_window(width * (.3275 + xInc), height * .05, window=entryBox)
        xInc += .04125
        if i == 2 or i == 5:
            xInc += .0075
        entryBoxList.append(entryBox)
    xInc = 0
    for i in range(0,9):
        entryBox = Entry(canvas, font=("Helvetica 50 bold"), width = 2)
        canvas.create_window(width * (.3275 + xInc), height * .125, window=entryBox)
        xInc += .04125
        if i == 2 or i == 5:
            xInc += .0075
        entryBoxList.append(entryBox)
    xInc = 0
    for i in range(0,9):
        entryBox = Entry(canvas, font=("Helvetica 50 bold"), width = 2)
        canvas.create_window(width * (.3275 + xInc), height * .2, window=entryBox)
        xInc += .04125
        if i == 2 or i == 5:
            xInc += .0075
        entryBoxList.append(entryBox)
    xInc = 0

    for i in range(0,9):
        entryBox = Entry(canvas, font=("Helvetica 50 bold"), width = 2)
        canvas.create_window(width * (.3275 + xInc), height * .3, window=entryBox)
        xInc += .04125
        if i == 2 or i == 5:
            xInc += .0075
        entryBoxList.append(entryBox)

    xInc = 0
    for i in range(0,9):
        entryBox = Entry(canvas, font=("Helvetica 50 bold"), width = 2)
        canvas.create_window(width * (.3275 + xInc), height * .375, window=entryBox)
        xInc += .04125
        if i == 2 or i == 5:
            xInc += .0075
        entryBoxList.append(entryBox)
    xInc = 0
    for i in range(0,9):
        entryBox = Entry(canvas, font=("Helvetica 50 bold"), width = 2)
        canvas.create_window(width * (.3275 + xInc), height * .45, window=entryBox)
        xInc += .04125
        if i == 2 or i == 5:
            xInc += .0075
        entryBoxList.append(entryBox)
    xInc = 0
    for i in range(0,9):
        entryBox = Entry(canvas, font=("Helvetica 50 bold"), width = 2)
        canvas.create_window(width * (.3275 + xInc), height * .55, window=entryBox)
        xInc += .04125
        if i == 2 or i == 5:
            xInc += .0075
        entryBoxList.append(entryBox)

    xInc = 0
    for i in range(0,9):
        entryBox = Entry(canvas, font=("Helvetica 50 bold"), width = 2)
        canvas.create_window(width * (.3275 + xInc), height * .625, window=entryBox)
        xInc += .04125
        if i == 2 or i == 5:
            xInc += .0075
        entryBoxList.append(entryBox)
    xInc = 0
    for i in range(0,9):
        entryBox = Entry(canvas, font=("Helvetica 50 bold"), width = 2)
        canvas.create_window(width * (.3275 + xInc), height * .7, window=entryBox)
        xInc += .04125
        if i == 2 or i == 5:
            xInc += .0075
        entryBoxList.append(entryBox)

    tries = 1
    tryLabel = Label(canvas, text = "Tries:\n"+str(tries), bg = "magenta", fg= "white", font=("helvetica 50"))
    canvas.create_window(width*.85, height*.25, window=tryLabel)

    enterButton = Button(canvas, text="SUBMIT", font=("Helvetica 20 bold"), fg="magenta", bg="white",
            activeforeground = "white", activebackground = "magenta", command= lambda: checkGame(canvas,entryBoxList, correct, tries, tryLabel, enterButton))
    enterButton.place(relx=.8575, rely=.5, anchor=CENTER)

def checkSquares(squareList, correct):
    try:
        index = 0
        for i in range(0,9):
            if i % 3 == 1:
                index = i*9
            squareSet = set()
            squareSet.add(int(squareList[i].get().strip()))
            squareSet.add(int(squareList[i+1].get().strip()))
            squareSet.add(int(squareList[i+2].get().strip()))
            squareSet.add(int(squareList[i+9].get().strip()))
            squareSet.add(int(squareList[i+10].get().strip()))
            squareSet.add(int(squareList[i+11].get().strip()))
            squareSet.add(int(squareList[i+18].get().strip()))
            squareSet.add(int(squareList[i+19].get().strip()))
            squareSet.add(int(squareList[i+20].get().strip()))
            print(len(squareSet))
            if len(squareSet()) < 9:
                correct = False
                break
            else:
                index +=3
    except:
        correct=False
        return correct
    return correct

def checkGame(canvas, squareList, correct, tries, tryLabel, enterButton):
    correct = True
    try:
        if checkSquares(squareList, correct):
            for i in range(0,8):
                if int(squareList[i].get().strip()) == int(squareList[i+1].get().strip()) or int(squareList[i].get().strip()) == int(squareList[i+9].get().strip())or int(squareList[i].get().strip()) == int(squareList[i+18].get().strip())or int(squareList[i].get().strip()) == int(squareList[i+27].get().strip()) or int(squareList[i].get().strip()) == int(squareList[i+36].get().strip())or int(squareList[i].get().strip()) == int(squareList[i+45].get().strip())or int(squareList[i].get().strip()) == int(squareList[i+54].get().strip())or int(squareList[i].get().strip()) == int(squareList[i+63].get().strip())or int(squareList[i].get().strip()) == int(squareList[i+72].get().strip()):
                    correct = False
        else:
            correct = False

    except:
        correct = False

    if not correct:
        tries +=1
        tryLabel.configure(text = "Tries:\n"+str(tries))
        enterButton.configure(command=lambda:checkGame(canvas,squareList, correct, tries, tryLabel, enterButton))
    else:
        canvas.create_text(width / 2, height / 5, text="Smarty Pants!", fill="Magenta", font=("Helvetica 60 bold"))

def playSudoku():
    print("Sudoku")


def setUpFlappyBird():
    playFlappyBird()


def playFlappyBird():
    print("Flappy Bird")


def setUpPong():
    pongWindow = Toplevel(window)
    pongWindow.title("House Rules")
    width, height = pongWindow.winfo_screenwidth(), pongWindow.winfo_screenheight()
    pongWindow.geometry('%dx%d+0+0' % (width, height))
    canvas = Canvas(pongWindow, width=width, height=height, bg="Magenta")
    canvas.pack()

    entryBoxLeft = Entry(canvas, font=("Helvetica 20"))
    entryBoxLeft.insert(0, "Player 1")
    entryBoxLeft.bind("<FocusIn>", lambda event: entryBoxLeft.delete(0, "end"))
    canvas.create_window(width * .4, height * .5, window=entryBoxLeft)

    entryBoxRight = Entry(canvas, font=("Helvetica 20"))
    entryBoxRight.insert(0, "Player 2")
    entryBoxRight.bind("<FocusIn>", lambda event: entryBoxRight.delete(0, "end"))
    canvas.create_window(width * .6, height * .5, window=entryBoxRight)

    options = ["Purple","St. Rose","Jokes","LaSalle"]

    choice = StringVar()
    choice.set("St. Rose")
    themeOptions = OptionMenu(pongWindow, choice, *options)
    themeOptions.configure(width=10, font = ("Helvetica 20 bold"), fg="magenta", bg="white", activeforeground = "white", activebackground = "magenta")
    themeOptions.place(relx = .5, rely = .4, anchor = CENTER)


    var = IntVar()
    easy = Radiobutton(pongWindow, text='Easy', variable=var, width=10, fg="magenta", bg="white", activeforeground = "white", activebackground = "magenta",
                       command=lambda: startButton.configure(
                           command=lambda: playPong(entryBoxLeft.get(), entryBoxRight.get(), var.get(), choice.get())),
                       value=1, font=("Helvetica 20 bold"), selectcolor='white')
    easy.place(relx=.25, rely=.25, anchor=CENTER)
    medium = Radiobutton(pongWindow, text='Medium', variable=var, width=10, fg="magenta", bg="white", activeforeground = "white", activebackground = "magenta",
                         command=lambda: startButton.configure(
                             command=lambda: playPong(entryBoxLeft.get(), entryBoxRight.get(), var.get(), choice.get())),
                         value=2, font=("Helvetica 20 bold"), selectcolor='white')
    medium.place(relx=.5, rely=.25, anchor=CENTER)
    medium.select()
    hard = Radiobutton(pongWindow, text='Hard', variable=var, width=10, fg="magenta", bg="white", activeforeground = "white", activebackground = "magenta",
                       command=lambda: startButton.configure(
                           command=lambda: playPong(entryBoxLeft.get(), entryBoxRight.get(), var.get(), choice.get())),
                       value=3,font=("Helvetica 20 bold"), selectcolor='white')
    hard.place(relx=.75, rely=.25, anchor=CENTER)

    startButton = Button(canvas, text="START", font=("Helvetica 30 bold"), fg="magenta", bg="white", activeforeground = "white", activebackground = "magenta",
                         command=lambda: playPong(entryBoxLeft.get(), entryBoxRight.get(), 2, choice.get()))
    startButton.place(relx=.5, rely=.6, anchor=CENTER)

    createButton(pongWindow, "Close")

def playPong(leftPlayer, rightPlayer, difficulty, theme):
    global paused
    paused = False
    global gameOn
    gameOn = False
    if theme == "Purple":
        backgroundColor = "magenta"
        boardColor = "yellow"
        scoreboardColor = "cyan"
        paddleColor = "yellow"
        ballColor = "cyan"
        gameOverColor = "black"
    elif theme == "St. Rose":
        backgroundColor = "ForestGreen"
        boardColor = "white"
        scoreboardColor = "gold"
        paddleColor = "gold"
        ballColor = "red"
        gameOverColor = "white"
    elif theme == "Jokes":
        backgroundColor = "yellow"
        boardColor = "cyan"
        scoreboardColor = "black"
        paddleColor = "cyan"
        ballColor = "black"
        gameOverColor = "black"
    else:
        backgroundColor = "DarkBlue"
        boardColor = "white"
        scoreboardColor = "white"
        paddleColor = "gold"
        ballColor = "gold"
        gameOverColor = "white"

    if difficulty == 1:
        stickSpeed = 20
        stickWidth = 8
        leftStartDistance = -300
        rightStartDistance = 300
        startHeight = -200
        boardHeight = 300
        boardWidth = rightStartDistance + 100
    elif difficulty == 2:
        stickSpeed = 15
        stickWidth = 6
        leftStartDistance = -200
        rightStartDistance = 200
        startHeight = -120
        boardHeight = 280
        boardWidth = rightStartDistance + 100
    elif difficulty == 3:
        stickSpeed = 10
        stickWidth = 5
        leftStartDistance = -100
        rightStartDistance = 100
        startHeight = -100
        boardHeight = 250
        boardWidth = rightStartDistance + 100

    screen = turtle.Screen()
    turtle.TurtleScreen._RUNNING = True
    screen.title("Pong")
    screen.bgcolor(backgroundColor)
    screen.setup(width=width, height=height)
    board = turtle.Turtle()
    board.speed(0)
    board.color(boardColor)
    board.goto(0, (boardHeight * -1) - 10)
    board.goto(boardWidth * -1, (boardHeight * -1) - 10)
    board.goto(boardWidth * -1, boardHeight + 10)
    board.goto(boardWidth, boardHeight + 10)
    board.goto(boardWidth, (boardHeight * -1) - 10)
    board.goto(0, (boardHeight * -1) - 10)
    board.goto(0, boardHeight + 10)
    board.hideturtle()

    leftPad = turtle.Turtle()
    leftPad.speed(0)
    leftPad.shape("square")
    leftPad.color(paddleColor)
    leftPad.shapesize(stretch_wid=stickWidth, stretch_len=2)
    leftPad.penup()
    leftPad.goto(leftStartDistance, 0)

    rightPad = turtle.Turtle()
    rightPad.speed(0)
    rightPad.shape("square")
    rightPad.color(paddleColor)
    rightPad.shapesize(stretch_wid=stickWidth, stretch_len=2)
    rightPad.penup()
    rightPad.goto(rightStartDistance, startHeight)

    ball = turtle.Turtle()
    ball.speed(40)
    ball.shape("circle")
    ball.color(ballColor)
    ball.penup()
    ball.goto(0,0)
    ball.dx = 10
    ball.dy = -10

    leftScore = 0
    rightScore = 0

    score = turtle.Turtle()
    score.speed(0)
    score.color(scoreboardColor)
    score.penup()
    score.hideturtle()
    score.goto(0, 350)
    score.write("{}: 0      {}: 0".format(leftPlayer,rightPlayer), align='center', font=("Courier", 30, "bold"))

    helpText = turtle.Turtle()
    helpText.color(boardColor)
    helpText.penup()
    helpText.hideturtle()
    helpText.goto(rightStartDistance + 350, 130)
    helpText.write("Left: 'q' = UP, 'z' = DOWN", align='center', font=("Courier", 20, "bold"))
    helpText.goto(rightStartDistance + 350, 100)
    helpText.write("Right: UP = UP, DOWN = DOWN", align='center', font=("Courier", 20, "bold"))
    helpText.goto(rightStartDistance + 350, 25)
    helpText.write("New Game 10 Seconds", align='center', font=("Courier", 20, "bold"))
    helpText.goto(rightStartDistance + 350, 0)
    helpText.write("After \'Game Over\'", align='center', font=("Courier", 20, "bold"))
    helpText.goto(rightStartDistance + 350, -75)
    helpText.write("Highest Scoring Games and", align='center', font=("Courier", 20, "bold"))
    helpText.goto(rightStartDistance + 350, -105)
    helpText.write("Biggest Wins Get Ranked", align='center', font=("Courier", 20, "bold"))

    def leftUp():
        if gameOn == True:
            y = leftPad.ycor()
            y += stickSpeed
            leftPad.sety(y)

    def leftDown():
        y = leftPad.ycor()
        y -= stickSpeed
        leftPad.sety(y)

    def rightUp():
        y = rightPad.ycor()
        y += stickSpeed
        rightPad.sety(y)

    def rightDown():
        y = rightPad.ycor()
        y -= stickSpeed
        rightPad.sety(y)

    def pause():
        global paused
        if gameOn == True:
            paused = True
            pauseMenu = Tk()
            pauseMenu.title("Paused")
            width, height = pauseMenu.winfo_screenwidth(), pauseMenu.winfo_screenheight()
            pauseMenu.geometry('%dx%d+%d+%d' % (width / 2, height / 2, width/4, height/4))
            canvas = Canvas(pauseMenu, width=width / 2, height=height / 2, bg="Cyan")
            canvas.pack()
            resumeButton = Button(pauseMenu, text="Resume", justify=CENTER,
                                  command=lambda: unpause(pauseMenu), font=("Helvetica 20 bold"), bg="magenta", fg="yellow")
            resumeButton.place(relx=.5, rely=.5, anchor=CENTER)

            def quit(screen, pauseMenu):
                pauseMenu.destroy()
                screen.bye()

            quitButton = Button(pauseMenu, text="I'm a Quitter", command=lambda: quit(screen, pauseMenu), font=("Helvetica 15"), bg="red",
                            fg="white")
            quitButton.place(relx=.5, rely=.75, anchor=CENTER)
            pausing()

    def pausing():
        if paused:
            turtle.ontimer(pausing, 250)

    def unpause(pauseMenu):
        pauseMenu.destroy()
        global paused
        paused = False

    screen.onkeypress(leftUp, "q")
    screen.onkeypress(leftDown, "z")
    screen.onkeypress(rightUp, "Up")
    screen.onkeypress(rightDown, "Down")
    screen.onkeypress(pause, "p")
    screen.onkeypress(unpause, "u")
    screen.listen()
    while ((leftScore < 7 and rightScore <7) or (leftScore >= 7 and abs(leftScore - rightScore) < 2) or (
            rightScore >= 7 and abs(rightScore - leftScore) < 2)):
        gameOn = True
        if not paused:
            screen.update()
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            if ball.ycor() > boardHeight:
                ball.sety(boardHeight)
                ball.dy *= -1
            if ball.ycor() < boardHeight*-1:
                ball.sety(boardHeight*-1)
                ball.dy *= -1
            if ball.xcor() > rightStartDistance + 100:
                ball.goto(0, 0)
                leftScore += 1
                ball.dy *= -1
                leftPad.goto(leftStartDistance,0)
                if ball.dy < 0:
                    rightPad.goto(rightStartDistance, startHeight)
                else:
                    rightPad.goto(rightStartDistance, -1 * startHeight)
                score.clear()
                score.write("{}: {}      {}: {}".format(leftPlayer, leftScore, rightPlayer, rightScore), align='center',
                            font=('Courier', 30, "bold"))

            if ball.xcor() < leftStartDistance - 100:
                ball.goto(0, 0)
                rightScore += 1
                ball.dy *= -1
                rightPad.goto(rightStartDistance, 0)
                if ball.dy < 0:
                    leftPad.goto(leftStartDistance, startHeight)
                else:
                    leftPad.goto(leftStartDistance, -1 * startHeight)
                score.clear()
                score.write("{}: {}      {}: {}".format(leftPlayer, leftScore, rightPlayer, rightScore), align='center',
                            font=('Courier', 30, "bold"))

            if (ball.xcor() > rightStartDistance - 50 and ball.xcor() < rightStartDistance - 20) and (
                    ball.ycor() < rightPad.ycor() + stickWidth * 10 and ball.ycor() > rightPad.ycor() - stickWidth * 10):
                ball.setx(rightStartDistance - 50)
                ball.dx *= -1

            if (ball.xcor() < leftStartDistance + 50 and ball.xcor() > leftStartDistance + 20) and (
                    ball.ycor() < leftPad.ycor() + stickWidth * 10 and ball.ycor() > leftPad.ycor() - stickWidth * 10):
                ball.setx(leftStartDistance + 50)
                ball.dx *= -1
        else:
            screen.update()
    gameOn = False
    paused = False
    gameOver = turtle.Turtle()
    gameOver.goto(0,0)
    gameOver.color(gameOverColor)
    if leftScore > rightScore:
        gameOver.write("GAME OVER:", align='center', font=('Courier', 50, "bold"))
        gameOver.goto(0, -75)
        gameOver.write("{} WINS!".format(leftPlayer), align='center', font=('Courier', 50, "bold"))
    else:
        gameOver.write("GAME OVER:", align='center', font=('Courier', 50, "bold"))
        gameOver.goto(0, -75)
        gameOver.write("{} WINS!".format(rightPlayer), align='center', font=('Courier', 50, "bold"))
    gameOver.hideturtle()
    screen.ontimer(screen.bye, 10000)
    screen.exitonclick()


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
    canvas.create_window(width * .8, height * .225, window=jokeLabel)

    jokeButton = Button(JokesAndRiddlesWindow, text="New Joke", wraplength=50, justify=CENTER,
                        command=lambda: newJoke(jokeLabel, deleteButton), font=("Helvetica 15"), bg="cyan", fg="black")
    jokeButton.place(relx=.55, rely=.25, anchor=CENTER)

    deleteButton = Button(JokesAndRiddlesWindow, text="X", justify=CENTER,
                          command=lambda: deleteJoke(jokeLabel, jokeId, deleteButton), font=("Helvetica 20 bold"),
                          bg="Red", fg="black")
    deleteButton.place(relx=.55, rely=.1, anchor=CENTER)

    answerButton = Button(JokesAndRiddlesWindow, text="Show Answer", command=lambda: showAnswer(riddle, answerLabel),
                          width=int(buttonWidth / 2), font=("Helvetica 15"), bg="green", fg="white")
    answerButton.place(relx=.22, rely=.5, anchor=CENTER)

    riddleButton = Button(JokesAndRiddlesWindow, text="New Riddle", wraplength=60, justify=CENTER,
                          command=lambda: newRiddle(riddleLabel, answerLabel, answerButton),
                          font=("Helvetica 15"), bg="cyan", fg="black")
    riddleButton.place(relx=.1, rely=.5, anchor=CENTER)

    entryBox = Entry(JokesAndRiddlesWindow, font=("Helvetica 20"))
    entryBox.insert(0, "Format: Joke")
    entryBox.bind("<FocusIn>", lambda event: entryBox.delete(0, "end"))
    canvas.create_window(width * .8, height * .5, window=entryBox)

    addJokeButton = Button(JokesAndRiddlesWindow, text="Add Joke", wraplength=60, justify=CENTER,
                           command=lambda: addJoke(jokeLabel, deleteButton, entryBox),
                           font=("Helvetica 15"), bg="purple", fg="white")
    addJokeButton.place(relx=.65, rely=.5, anchor=CENTER)

    entryBoxRiddle = Entry(JokesAndRiddlesWindow, font=("Helvetica 20"))
    entryBoxRiddle.insert(0, "Format: Riddle - Answer")
    entryBoxRiddle.bind("<FocusIn>", lambda event: entryBoxRiddle.delete(0, "end"))
    canvas.create_window(width * .8, height * .75, window=entryBoxRiddle)

    deleteRiddleButton = Button(JokesAndRiddlesWindow, text="X", justify=CENTER,
                                command=lambda: deleteRiddle(riddleLabel, answerLabel, riddle, answerButton,
                                                             deleteButton), font=("Helvetica 20 bold"),
                                bg="Red", fg="black")
    deleteRiddleButton.place(relx=.45, rely=.1, anchor=CENTER)

    addRiddleButton = Button(JokesAndRiddlesWindow, text="Add Riddle", wraplength=75, justify=CENTER,
                             command=lambda: addRiddle(riddleLabel, answerLabel, answerButton, deleteRiddleButton,
                                                       entryBoxRiddle),
                             font=("Helvetica 15"), bg="purple", fg="white")
    addRiddleButton.place(relx=.65, rely=.75, anchor=CENTER)


def addRiddle(riddleLabel, answerLabel, answerButton, deleteRiddleButton, entryBox):
    DB_NAME = 'JokesAndRiddles'
    cursor, connection = connectToMySQL()

    cursor.execute("USE {}".format(DB_NAME))
    entry = entryBox.get()
    element = entry.split("-")
    riddle = element[0]
    answer = element[1]

    cursor.execute("INSERT INTO Riddles VALUES(\"{}\", \"{}\")".format(element[0], element[1]))
    connection.commit()

    riddleLabel.configure(text=riddle)
    answerLabel.configure(text='')
    answerButton.configure(command=lambda: showAnswer(riddle, answerLabel))
    deleteRiddleButton.configure(
        command=lambda: deleteRiddle(riddleLabel, answerLabel, riddle, answerButton, deleteRiddleButton))
    entryBox.delete(0, END)
    entryBox.insert(0, "Format: Riddle - Answer")
    entryBox.bind("<FocusIn>", lambda event: entryBox.delete(0, "end"))


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
    entryBox.delete(0, END)
    entryBox.insert(0, "Format: Joke")
    entryBox.bind("<FocusIn>", lambda event: entryBox.delete(0, "end"))


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


def deleteRiddle(riddleLabel, answerLabel, riddle, answerButton, deleteButton):
    DB_NAME = 'JokesAndRiddles'
    cursor, connection = connectToMySQL()

    cursor.execute("USE {}".format(DB_NAME))
    cursor.execute("DELETE FROM Riddles WHERE riddle = \'{}\'".format(riddle))
    connection.commit()
    ## add script to acess terminal to update joke dump file

    cursor.execute("SELECT riddle, answer FROM Riddles ORDER BY RAND() LIMIT 1")
    element = cursor.fetchone()
    riddle = element[0]

    answer = element[1]
    riddleLabel.configure(text=riddle)
    answerLabel.configure(text='')
    answerButton.configure(command=lambda: showAnswer(riddle, answerLabel))
    deleteButton.configure(command=lambda: deleteRiddle(riddleLabel, answerLabel, riddle, answerButton, deleteButton))


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
                        readReminders("/home/pi/Desktop/InfoBoard/reminders.txt"), [],
                        "/home/pi/Desktop/InfoBoard/reminders.txt", None)


def addToList(window, canvas, buttonsList, entryBox, list, fileName):
    if "-" in entryBox.get():
        list.append(entryBox.get() + "\n")
    file = open(fileName, "w")
    file.truncate(0)
    for element in list:
        file.write(element)
    file.close()
    createReminderLists(window, canvas, list, buttonsList, fileName, entryBox)


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

    entryBox = Entry(window, font=("Helvetica 25"), bg="ForestGreen", fg="gold")
    entryBox.insert(0, "Format: reminder - d/m/y")
    entryBox.bind("<FocusIn>", lambda event: entryBox.delete(0, "end"))
    canvas.create_window(width / 2, 50, window=entryBox)

    for element in list:
        elementText = element.split("-")
        label = Label(window, text=elementText[0].strip(), fg="gold", bg="ForestGreen",
                      font=("Helvetica 25 bold"))
        canvas.create_window(100, y, anchor='w', window=label)
        doneButton = Button(window, text=elementText[1].strip(), justify=CENTER, width=10,
                            command=lambda index=i, currButtons=buttonsList: createReminderLists(window, canvas,
                                                                                                 newList(index,
                                                                                                         tempList),
                                                                                                 currButtons, fileName,
                                                                                                 entryBox),
                            font=("Helvetica 25 bold"), bg="Gold", fg="ForestGreen")
        doneButton.place(relx=.9, y=y, anchor=CENTER)
        buttonsList.append(doneButton)
        y += 60
        i += 1

    file = open(fileName, "w")
    file.truncate(0)
    for element in list:
        file.write(element)
    file.close()

    addButton = Button(window, text="Add", justify=CENTER, width=5,
                       command=lambda: addToList(window, canvas, buttonsList, entryBox, list, fileName),
                       bg="gold", fg="ForestGreen", font=("Helvetica 25 bold"))
    addButton.place(x=width * .65, y=50, anchor=CENTER)
    buttonsList.append(addButton)

    remindersButton = Button(window, text="Reminders", justify=CENTER, width=10,
                             command=lambda currButtons=buttonsList: createReminderLists(window, canvas,
                                                                                         readReminders(
                                                                                             "/home/pi/Desktop/InfoBoard/reminders.txt"),
                                                                                         currButtons,
                                                                                         "/home/pi/Desktop/InfoBoard/reminders.txt",
                                                                                         entryBox),
                             font=("Helvetica 25 bold"), bg="gold", fg="ForestGreen")
    movieButton = Button(window, text="Movies", justify=CENTER, width=10,
                         command=lambda currButtons=buttonsList: createReminderLists(window, canvas,
                                                                                     readReminders(
                                                                                         "/home/pi/Desktop/InfoBoard/movieReminders.txt"),
                                                                                     currButtons,
                                                                                     "/home/pi/Desktop/InfoBoard/movieReminders.txt",
                                                                                     entryBox),
                         font=("Helvetica 25 bold"), bg="gold", fg="ForestGreen")
    remindersButton.place(relx=.9, rely=.05, anchor=CENTER)
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
                        bg="ForestGreen", fg="white", activeforeground='ForestGreen')
        button.place(x=0, y=0)
    elif name == "Weather":
        button = Button(window, text=name, command=openWeather, height=buttonHeight, width=buttonWidth, bg="DarkBlue",
                        fg="white", activeforeground='DarkBlue')
        button.place(x=0, rely=.5)
    elif name == "Jokes/Riddles":
        button = Button(window, text=name, command=openJokesAndRiddles, height=buttonHeight, width=buttonWidth,
                        bg="yellow", fg="black", activeforeground='gold1')
        button.place(relx=.75, y=0)
    else:
        button = Button(window, text=name, command=window.destroy, width=int(buttonWidth / 2), font=("Helvetica 15"),
                        bg="red", fg="white")
        button.place(relx=.5, rely=.8, anchor=CENTER)


createAllButtons()

gameButton = Button(window, text="Games", command=lambda: openGames(0), width=int(width * .02604167),
                    height=int(height * .02314815), bg="magenta", fg="white", activeforeground='magenta')
gameButton.place(relx=.75, rely=.5)


def setGame(button, game, gameButton):
    gameButton.configure(command=lambda: openGames(game))


var = IntVar()
game1 = Radiobutton(window, text='Sudoku', variable=var, command=lambda: setGame(game1, var.get(), gameButton),
                    value=1, bg="magenta", fg="white", font=("Helvetica 20 bold"), selectcolor='magenta', activeforeground='magenta')
game1.place(relx=.75, rely=.5)
game2 = Radiobutton(window, text='Flappy Bird', variable=var, command=lambda: setGame(game2, var.get(), gameButton),
                    value=2, bg="magenta", fg="white", font=("Helvetica 20 bold"), selectcolor='magenta', activeforeground='magenta')
game2.place(relx=.83, rely=.5)
game3 = Radiobutton(window, text='Pong', variable=var, command=lambda: setGame(game3, var.get(), gameButton),
                    value=3, bg="magenta", fg="white", font=("Helvetica 20 bold"), selectcolor='magenta', activeforeground='magenta')
game3.place(relx=.9375, rely=.5)


##need to make a label then just call "tieRefresh right after"
def timeRefresh():
    date = datetime.now()
    currentTime = time.strftime("%I:%M:%S %p", time.localtime())
    currentDate = date.strftime("%m/%d/%y")
    label.config(text=currentTime + "\r" + currentDate)
    window.after(1000, timeRefresh)


font = ('Arial', 80)
label = Label(window, font=font, fg="white", bg="black")
label.place(relx=.5, rely=.45, anchor=CENTER)

timeRefresh()

window.mainloop()