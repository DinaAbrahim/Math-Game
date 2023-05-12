#"I hereby certify that this program is solely the result of my own work 
#and is in compliance with the Academic Integrity policy of the course syllabus 
#and the academic integrity policy of the CS department.”

#I ran this code on Windows. 

import Draw
import time
import random

#global variable of SECONDS
SECONDS = 50

#this function sets the canvas size and invokes homeScreen()
def main():
    Draw.setCanvasSize(600, 500)
    homeScreen() 

#this function sets up the home screen
#and invokes homeScreenButtons() and ifPlayGame()
def homeScreen():
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(30)
    Draw.string("Addition Game", 170, 50)
    Draw.setFontSize(20)
    Draw.string("By: Dina Abrahim", 190, 100)
    homeScreenButtons()       
    ifPlayGame()

#this function sets up the home screen buttons   
def homeScreenButtons():
    #Play button
    Draw.filledRect(175, 250, 250, 150)
    Draw.setColor(Draw.BLUE)
    Draw.setFontSize(60)
    Draw.string("Play", 225, 280)
    #Instructions button 
    Draw.filledRect(200, 150, 200, 90)
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(20)
    Draw.string("How to Play", 230, 180)     

#this function brings the player to a new screen 
#if they press on one of the two buttons
def ifPlayGame():
    while True:
        #if the player clicked 
        if Draw.mousePressed():
            #find the x of the click
            newX = Draw.mouseX()
            #find the y of the click 
            newY = Draw.mouseY()
            #if the x and y of the click are in the Play button
            if newX >= 175 and newX <= 425 and newY >= 250 and newY <= 400:
                #invoke playGame()
                playGame()
            #if the x and y of the click are in the How to Play button 
            elif newX >= 200 and newX <= 400 and newY >= 150 and newY <= 290:
                howToPlayGame()

#this function sets up the instructions page and invokes backToHomeScreen()
def howToPlayGame():
    Draw.clear()
    #Title: How to Play 
    Draw.setFontSize(30)
    Draw.setColor(Draw.BLACK)
    Draw.setFontBold(True)
    Draw.string("How to Play", 180, 100)
    #Instructions on how to play the game 
    Draw.setFontSize(20)
    Draw.setFontBold(False)
    Draw.string("The game is simple. You have 50 seconds to", 20, 160)
    Draw.string("get 10 points. Every question you get right you", 20, 200)
    Draw.string("get one point. Every question you get wrong", 20, 240)
    Draw.string("a point is subtracted.", 20, 280)
    #Button to get back to the home screen 
    Draw.filledRect(220, 340, 170, 100)
    Draw.setColor(Draw.BLUE)
    Draw.string("Back to", 255, 355)
    Draw.string("Home Screen", 220, 385)
    #brings the player back to the home screen if they click on the button 
    backToHomeScreen()

#this function brings the player back to the home screen 
#if they press on the button and invokes homeScreen()
def backToHomeScreen():
    while True:
        #if the player clicked 
        if Draw.mousePressed():
            #find the x of the click
            newX = Draw.mouseX()
            #find the y of the click 
            newY = Draw.mouseY()
            #if the x and y of the click are in the Back to Home Screen button
            #invoke homeScreen()
            if newX >= 220 and newX <= 390 and newY >= 340 and newY <= 440:
                Draw.clear()
                homeScreen()

#this function plays the game 
def playGame():
    #initializes startTime
    startTime = time.time()
    #initializes score
    score = 0
    #initializes timeRemaining
    timeRemaining = int(SECONDS - (time.time() - startTime))
    #while score is less than 10 and timeRemaining is greater than 0
    while score < 10 and timeRemaining > 0:
        #invoke playRound
        score, timeRemaining = playRound(startTime, score)
    #when the score is equal to 10 or timeRemaining is equal to 0
    #invoke endGame 
    endGame(score)

#this function plays a round of the game 
def playRound(startTime, score):
    #chooses 2 random operands 
    operand1 = random.randint(10, 49)
    operand2 = random.randint(10, 49)
    #finds the answer 
    answer = operand1 + operand2
    #finds the operator 
    operator = "+" 
    #invokes makeChoiceList() 
    choiceList = makeChoiceList(answer)
    #initializes timeRemaining 
    timeRemaining = int(SECONDS - (time.time() - startTime)) 
    #while timeRemaining is greater than 0
    while timeRemaining > 0:
        #find timeRemaining 
        timeRemaining = int(SECONDS - (time.time() - startTime))
        #invokes drawScreen()
        drawScreen(operand1, operand2, operator, choiceList, score, timeRemaining)
        #if the player clicked 
        if Draw.mousePressed():
            #find the x of the click
            newX = Draw.mouseX()
            #find the y of the click
            newY = Draw.mouseY() 
            #invokes getBoxNumber 
            ans = getBoxNumber(newX, newY) 
            #if the player chose the correct answer
            if choiceList[ans] == answer and ans >= 0:
                #add one point to score 
                score += 1
                #return score and timeRemaining
                return score, timeRemaining
            #if the player did not choose the correct answer 
            elif ans >= 0:
                #if the score is greater than 0
                if score > 0:
                    #subtract one point from score 
                    score -= 1
                #return score and timeRemaining
                return score, timeRemaining 
    #return score and timeRemaining
    return score, timeRemaining 

#this function finds the box the player clicked on 
def getBoxNumber(newX, newY): 
    #if the player clicked outside the boxes
    #return -1 and nothing happens 
    if not(newX >= 50 and newX <= 550 and newY >= 200 and newY <= 350):
        return -1
    #if the player did click on a box
    else:
        #find the box number 
        return (newX - 50) // 100

#this function makes the list of possible answers 
def makeChoiceList(answer):
    #makes an empty list 
    choiceList = []
    #adds the correct answer to the list 
    choiceList += [answer]
    #while the list has less than 5 elements
    while len(choiceList) <= 4:
        #find a random answer 
        randomAnswer = random.randint(20, 99)
        #if the random answer is not in the list
        if not(randomAnswer in choiceList):
            #add the random answer to the list
            choiceList += [randomAnswer]
    #shuffle the list
    random.shuffle(choiceList)
    #return the list 
    return choiceList 

#this function draws the screen 
def drawScreen(operand1, operand2, operator, choiceList, score, timeRemaining):
    #clears the screen
    Draw.clear()
    #draws the question 
    Draw.setFontSize(40)
    Draw.string(str(operand1) + " " + operator + " " + str(operand2), 215, 100)
    #draws the boxes
    for i in range(5):
        Draw.rect(50 + 100 * i, 200, 100, 150)
    #draws the list of possible answers 
    for i in range(len(choiceList)):
        Draw.string(choiceList[i], 70 + 100 * i, 245) 
    #draws the score
    Draw.setFontSize(30)
    Draw.string("Score: " + str(score), 20, 400) 
    #draws the time remaining 
    Draw.string("Time Remaining: " + str(timeRemaining), 220, 400)  
    #shows everything
    Draw.show()

#this function tells the player if they won or lost
def endGame(score):
    #clears the screen 
    Draw.clear()
    #if score is 10
    if score == 10:
        #invokes homeScreenButtons()
        homeScreenButtons()
        #player won the game
        Draw.setFontSize(50)
        Draw.string("You won!", 170, 80)  
    #if the score is less than 10
    else:
        #invokes homeScreenButtons()
        homeScreenButtons()
        #player lost the game 
        Draw.setFontSize(50)
        Draw.string("You lost", 170, 80)        

#invokes the main function     
main() 