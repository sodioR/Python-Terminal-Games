# File:         connect_four.py
# Author:       Sadia Rahman
# Date:         11/9/2018
# Section:      9
# E-mail:       rasadia1@umbc.edu
# Description:  This is a simple program depicting Connect Four game

############################
                           #
from random import randint #
                           #
############################

#CONSTANTS

ONE_PLAYER = "y"
TWO_PLAYERS = "n"
FIRST_CHARACTER = "X"
SECOND_CHARACTER = "O"
EMPTY_CELL = "_"

#FUNCTIONS

# def printGrid(gridList): This functiion prints out the
#                          grid whenever called.
# input                    gridList
# output                   no returns

def printGrid(gridList):

    #This allows the grid to be printed backwards
    for x in range(len(gridList) - 1, -1, -1):
        for y in gridList[x]:
            print(y, end = " ")
        print()

# def playersMove(height, gridList, moveOne, FIRST_CHARACTER): This function executes the
#                                                              changes the grid will go
#                                                              through when the player decides
#                                                              a move.
# input                                                        gridList, height, moveOne, FIRST_CHARACTER
# output                                                       gridList

def playerMove(height, gridList, moveOne, FIRST_CHARACTER):

    a = 0
    #It's necessary to substract one since indexing will consider a 5 by 5 grid to
    #start from 0-4 not 1-5.
    column = moveOne - 1

    while a < height:
        if gridList[a][column] == EMPTY_CELL:
            gridList[a][column] = FIRST_CHARACTER
            return True
        a += 1
        #if the loop encounter an empty cell, the function will stop
    return False

# def calculatePosition(gridList, character, xPos, yPos, direction): This function calculates
#                                                                    whether the current player's
#                                                                    move is the fourth
# input                                                              gridList, character, xPos, yPos,
#                                                                    direction
# output                                                             0 or 1 depending on conditions
    
def calculatePosition(gridList, character, xPos, yPos, direction):

    #if the current position is outside of range of the grid, it'll return 0
    if xPos < 0 or yPos < 0 or xPos >= len(gridList[0]) or yPos >= len(gridList):
        return 0

    #if the character at given position is not specified piece
    if gridList[yPos][xPos] != character:
        return 0

    #1 will be added for each time an assigned character is found for each direction

    #left up diagonal
    if direction == 0:
        return 1 + calculatePosition(gridList, character, xPos - 1, yPos + 1, direction)

    #to the left side
    if direction == 1:
        return 1 + calculatePosition(gridList, character, xPos - 1, yPos, direction)

    #left down diagonal
    if direction == 2:
        return 1 + calculatePosition(gridList, character, xPos - 1, yPos - 1, direction)

    #downwards
    if direction == 3:
        return 1 + calculatePosition(gridList, character, xPos, yPos - 1, direction)

    #right down diagonal
    if direction == 4:
        return 1 + calculatePosition(gridList, character, xPos + 1, yPos - 1, direction)

    #to the right
    if direction == 5:
        return 1 + calculatePosition(gridList, character, xPos + 1, yPos, direction) 

    #right up diagonal
    if direction == 6:
        return 1 + calculatePosition(gridList, character, xPos + 1, yPos + 1, direction)

# def bazinga(gridList, height, moveColumn, character): this function determines whether current player
#                                                       won the game with their latest move
# input                                                 gridList, height, moveColumn, character
# output                                                True or False; True if the player won, False if
#                                                       the player does not win

def bazinga(gridList, height, moveColumn, character):

    #we know which column the player's last move was, the following will determine the row
    moveRow = -1
    moveColumn -= 1
    a = 0

    while a < height:
        if gridList[a][moveColumn] != EMPTY_CELL:
            moveRow += 1
        a += 1

    #calculates the number of characters sideways
    side = calculatePosition(gridList, character, moveColumn, moveRow, 1) + calculatePosition(gridList, character, moveColumn, moveRow, 5) - 1

    #calculates the number of characters downwards
    down = calculatePosition(gridList, character, moveColumn, moveRow, 3)

    #
    forwardDiagonal = calculatePosition(gridList, character, moveColumn, moveRow, 2) + calculatePosition(gridList, character, moveColumn, moveRow, 6) - 1

    #
    backwardDiagonal = calculatePosition(gridList, character, moveColumn, moveRow, 0) + calculatePosition(gridList, character, moveColumn, moveRow, 4) - 1

    if side >= 4 or down >= 4  or forwardDiagonal >= 4 or backwardDiagonal >= 4:
        
        #the current player won!!!
        return True
    
    #the current player has not won
    return False

#MAIN FUNCTION

def main():
    
    print("Welcome to CONNECT FOUR")

    height = int(input("Enter a height for the grid (5 or bigger): "))
    #Validating the height
    while height < 5:
        height = int(input("Height cannot be less than 5. Please enter a larger number: "))
        
    width = int(input("Enter a width for the grid (5 or bigger): "))
    #Validating the width
    while width < 5:
        width = int(input("Width cannot be less than 5. Please enter a larger number: "))
        
    #The user decided playing against the computer or two players.
    onePlayerTwoPlayer = input("Do you want to play against a computer or another player? (y = computer/n = another player): ")
    while onePlayerTwoPlayer != ONE_PLAYER or onePlayerTwoPlayer != TWO_PLAYERS:
        onePlayerTwoPlayer = input("Please enter either 'y' or 'n': ")
        
    gridList = []
    widthList = []

    #Make on list that depicts each row
    i = 0
    while i < width:
        widthList.append("_")
        i += 1

    #Add the width to the gridList to create a mock grid
    j = 0
    while j < height:
        gridList.append(list(widthList))
        j += 1

    #The inital, totally empty grid
    printGrid(gridList)

    while True:

        #If the user chose to play against a computer
        if onePlayerTwoPlayer == ONE_PLAYER:

            #The player one's moves
            moveOne = int(input("PLAYER ONE: Please enter a column to place your piece (1 - "+ str(width)+"): "))
            #Validating player one's moves
            while moveOne < 1 or moveOne > width:
                moveOne = int(input("Not valid. Please choose one within the given range: "))
            playerMove(height, gridList, moveOne, FIRST_CHARACTER)
            printGrid(gridList)

            #Checking if player one won
            won = bazinga(gridList, height, moveOne, FIRST_CHARACTER)
            if won == True:
                print("The game is over. WINNER : PLAYER ONE \(^-^)/")
                #using return, ends the loop
                return
            
            print()

            #The computer's moves
            print("Now the computer's turn...")
            computerMove = randint(1, width)
            print("The computer chose column:", computerMove)
            playerMove(height, gridList, computerMove, SECOND_CHARACTER)
            printGrid(gridList)

            #checking if the computer won
            won = bazinga(gridList, height, computerMove, SECOND_CHARACTER)
            if won == True:
                print("The game is over. WINNER: COMPUTER \(^-^)/")
                return

        #If the user chose to play against another player
        if onePlayerTwoPlayer == TWO_PLAYERS:

            #The player one's moves
            moveOne = int(input("PLAYER ONE: Please enter a column to place your piece (1 - "+ str(width)+"): "))
            #Validating player one's moves
            while moveOne < 1 or moveOne > width:
                moveOne = int(input("Not valid. Please choose one within the given range: "))
            playerMove(height, gridList, moveOne, FIRST_CHARACTER)
            printGrid(gridList)

            #Checking if player one won
            won = bazinga(gridList, height, moveOne, FIRST_CHARACTER)
            if won == True:
                print("The game is over. WINNER: PLAYER ONE \(^-^)/")
                return

            print()

            #The second player's moves
            moveTwo = int(input("PLAYER TWO: Please enter a column to place your piece (1 - "+ str(width)+"): "))
            #Validating player two's move
            while moveTwo < 1 or moveTwo > width:
                moveTwo = int(input("Not valid. Please choose one within the range: "))
            playerMove(height, gridList, moveTwo, SECOND_CHARACTER)
            printGrid(gridList)

            #Checking if the second player won
            won = bazinga(gridList, height, moveTwo, SECOND_CHARACTER)
            if won == True:
                print("The game is over. WINNER: PLAYER TWO \(^-^)/")
                return

main()
            

        
