# File:         terminal_sudoku.py
# Author:       Sadia Rahman
# Date:         12/11/2018
# Section:      9
# Email:        rasadia1@umbc.edu
# Description:  A simple program that loads up a game of sudoku and allows the player to solve it

###CONSTANTS###

MAX_NUMBER = 9
MIN_NUMBER = 1
PLAY = "p"
SOLVE = "s"
PLAY_NUMBER = "p"
SAVE = "s"
UNDO = "u"
QUIT = "q"
YES = "y"
NO = "n"

###CONSTANNTS###


# load()     this function loads a text file and converts the contents of the file to
#            a board that would be worked on
# Input      game_name; string
# Output     board

def load(game_name):
    
    load_game = open(game_name, "r")
    board = []
    
    for line in load_game.readlines():
        #Removes any and all white spaces
        clean_line = line.strip()
        #converts them into lists
        items = clean_line.split(",")
        row = []
        
        for i in items:
            #appends each item, as a number, into one row list...
            row.append(int(i))
            
        #Then each row list is added to the board
        board.append(row)
        
    load_game.close()
    return board

# savePuzzle() writes the contents a sudoku puzzle out
#              to a file in comma separated format
# Input:       board;    the square 2d puzzle (of integers) to write to a file
#              fileName; the name of the file to use for writing to

def savePuzzle(board, fileName):
    ofp = open(fileName, "w")
    for i in range(len(board)):
        rowStr = ""
        for j in range(len(board[i])):
            rowStr += str(board[i][j]) + ","
        # don't write the last comma to the file
        ofp.write(rowStr[ : len(rowStr)-1] + "\n")
    ofp.close()
    
# prettyPrint() prints the board with row and column labels,
#               and spaces the board out so that it looks nice
# Input:        board;  2D list; the square 2d game board (of integers) to print
# Output:       None;    prints the board in a pretty way

def prettyPrint(board):
    # print column headings and top border
    print("\n    1 2 3 | 4 5 6 | 7 8 9 ")
    print("  +-------+-------+-------+")

    for i in range(len(board)):
        # convert "0" cells to underscores  (DEEP COPY!!!)
        boardRow = list(board[i])
        for j in range(len(boardRow)):
            if boardRow[j] == 0:
                boardRow[j] = "_"

        # fill in the row with the numbers from the board
        print( "{} | {} {} {} | {} {} {} | {} {} {} |".format(i + 1,
                boardRow[0], boardRow[1], boardRow[2],
                boardRow[3], boardRow[4], boardRow[5],
                boardRow[6], boardRow[7], boardRow[8]) )

        # the middle and last borders of the board
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")
            
# solved()      solves the puzzle using recursion, used as the reference when
#               player decides to play with correctness
# Input         board; 2D list; the initial puzzle
#               row; integer
#               column; integer
# Output        solved_board; 2D list; solved puzzled
            
def solved(row, column, board):
    
    if row > 8 or column > 8:
        return True
    
    # find the next valid item of the board
    while board[row][column] != 0:
        
        column += 1
        
        #When the first row of items are all checked out, it resets "columns"...
        if column == MAX_NUMBER:
            column = 0
            #...and moves to the row of items
            row +=1
            
            #When the last row is checked out, then...
            if row == MAX_NUMBER:
                # ...base case is reached, without any missing items
                return True
        
    for i in range(1, 10):
        
        board[row][column] = i
        
        if willItDo(row, column, board, i, False) and solved(row, column, board):
            #checking if the current item is correct, plus if the rest of the board is solvable 
            return True
    
    # Otherwise, it resets the item back to zero and backtracks
    board[row][column] = 0
    return False

# willItDo    Checks to see if the number in question would be valid in the board
# Input       row; integer
#             column; integer
#             board; 2D list
#             number; integer; the number in question
#             printIfWrong; this is only for when the user opts out of correctness and
#             needs to be told if the number is unique. For solving the solution this will 
#             be set as False

def willItDo(row, column, board, number, printIfWrong):
    
    #Checks if the number is unique to the column.
    for i in range(len(board) - 1):
        
        if board[i][column] == number and i != row:
            
            #This is for when the user opts out of correctness and is prompted if the number is unique
            if printIfWrong:
                print("The number, "+ str(number)+" already exists in this column.")
            return False
    
    #Checks if the number is unique to the row
    for j in range(len(board) - 1):
        
        if board[row][j] == number and j != column:
            
            if printIfWrong:
                print("The number, "+ str(number)+" already exists in this row.")
            return False
    
    #Row and column wise, there are three base sets the number could be from, 0, 1 and 2
    #for example: if the row is in 0-2, then the row nonet set is 0, 
    #making the range 0 to (but not including) 3
    
    nonet_row = int(row/3)
    nonet_column = int(column/3)
    
    #checking if the number is unique to that specific nonet (square)
    for k in range(3 * nonet_row, 3* nonet_row + 3):
        
        for l in range(3 * nonet_column, 3 * nonet_column + 3):
            
            if board[k][l] == number and k != row and l != column:
                
                if printIfWrong:
                    print("The number, "+ str(number)+" already exists in this square")
                return False
            
    #If all checks out then the number is unique and the number will be placed into the board
    return True

# correctnessValidation ()      validation that'll exist when the player opts
#                               to play with correctness.
# Input                         solved_board; the solved puzzle
#                               row; integer
#                               column; integer
#                               number; integer

def correctnessValidation(solved_board, row, column, number):
    
    #If the number placed in is not the same as the number in the solved board
    #then the player is made aware
    print("OOPS! The number"+ str(number)+"does not belong in ("+ str(row)+","+ str(column)+")!") 
    print("Moving on...")
    
# solution()         Prints out the solution
# Input              solved_board; 2D list
        
def solution(solved_board):
    
    #Prints the solution 
    print("Here is the solution")
    prettyPrint(solved_board)
    
# quitGame()            quits the game after displaying the final updated
#                       puzzle
# Input                 board; current puzzle

def quitGame(board):
    
    #Prints the goodbye message and the final board
    print("Goodbye! Here is the final board!")
    prettyPrint(board)

# undo()                this function undos moves however many times the player
#                       decides to.
# Input                 board; current board
#                       move_position; 2d list; this is a list, containing the positions the
#                       player's moves exists
    
def undoMove(board, move_position):
    
    #User is prompted if they want to undo
    undo = input("Are you sure? ('y' for yes or 'n' for no): ")
    
    #until the user says no, the user can undo as many times as they want
    while undo == YES:

        if len(move_position) < 1:

            print("You have no more moves to undo")
            return

        else:
            #pinpoints the last move's co ordinates 
            last_move = move_position[len(move_position) - 1]
        
            #removes it from the list
            move_position.remove(last_move)
        
            #and turns whatever move they made to a 0
            board[last_move[0]][last_move[1]] = 0
        
            prettyPrint(board)
            undo = input("Would you like to undo again? ('y' for yes or 'n' for no): ")

# makeAMove()           makes and stores each move the player decides to make
# Input                 board; current board
#                       solved_board; solved puzzled used as reference
#                       move_position; 2D list
#                       correctness; string
# Output                board; current board but with updates
    
def makeAMove(solved_board, board, move_position, correctness):
    
    #Asks for the row
    row = int(input("Enter a row number (1-9): "))
    
    #Validates the row put in
    while row > MAX_NUMBER or row < MIN_NUMBER:
        row = int(input("Must be a number between 1-9, Please try again: "))
        
    #Asks for the column
    column = int(input("Enter a column number (1-9): "))
    
    #Validates the column put in
    while column > MAX_NUMBER or column < MIN_NUMBER:
        column = int(input("Must be a number between 1-9. Please try again: "))
        
    #Asks for the number
    number = int(input("Enter a number to put in cell ("+ str(row)+","+ str(column)+"): "))
    
    #Validates the number
    while number > MAX_NUMBER or number < MIN_NUMBER:
        number = int(input("Must be a number between 1-9. Please try again  "))

        #Setting the index correctly
    row -= 1
    column -= 1
        
    #When the user enabled correctness, the user will be let know if the answer is wrong or not
    if correctness == YES:

        #Checks if it is a zero
        if board[row][column] == 0:

            if solved[row][board] != number:
                correctnessValidation(solved_board, row, column, number)
        
            #Each move is added to a list, as a list
            #Thus removing the possibility of removing the first similar item
            move_position.append([row, column])

            board[row][column] = number
            prettyPrint(board)

        #Otherwise it doesnt do anything
        else:
            
            print("That position has a number already")
            
    #If the user opts out of correctness, the user will simple be told if the number is valid
    elif correctness == NO:

        #Checks if the number is 0
        if board[row][column] == 0:

            
            can_do = willItDo(row, column, board, number, True)
            if can_do:
                move_position.append([row, column])

                board[row][column] = number
                prettyPrint(board)

        else:

            print("That position already has a number")
            

    return board

# fullBoard()           checks if the board is full or not
# Input                 board; current board

def full(board):
    
    #Checks each item in the row
    for i in range(len(board)):
        
        #Checks each item within each row
        for j in range(len(board[i])):
            
            #checks if the number is 0
            if board[i][j] == 0:
                return False
    return True

# winOrLose()           checks if the full box is is the true solution
#                       or not
# Input                 board

def winOrLose(board, solved_board):
    
    for i in range(len(board)):
        
        for j in range(len(board[0])):
            #Similar to the full function except that it checks if it the same as the solved board
            if board[i][j] != solved_board[i][j]:
                return False
    return True
    
# deepCopy()        creates a deep copy of board, so that the copy can be
#                   used to create a solved board
# Input             board; 2D list
# Ouput             new_board; 2D list
    
def deepCopy(board):
    
    new_board = []
    
    for row in board:
        new_board.append(row[:])
    return new_board

def main():
    
    print("Welcome to Sudoku!")
    
    print()
    game_name = input("Please enter the name of the file:  ")
    
    #Load the file
    board = load(game_name)

    prettyPrint(board)
    
    #makes a seperate copy, a deep copy
    solved_board = deepCopy(board)
    
    #Solve the board
    solved(0, 0, solved_board)
    
    solve_play =input("solve(s) or play(p)? ")
    
    if solve_play == SOLVE:
        
        #prints the solution
        solution(solved_board)
        
    elif solve_play == PLAY:

        correctness = input("Enable correctness (y/n)? ")
        move_position = []
        is_it_full = full(board)
        
        while is_it_full == False:

            prettyPrint(board)
            
            play_undo_save_quit = input("play (p), undo (u), save (s), quit (q): ")
            
            if play_undo_save_quit == PLAY_NUMBER:
                
                board = makeAMove(solved_board, board, move_position, correctness)
                
            elif play_undo_save_quit == UNDO:
                
                undoMove(board, move_position)
            
            elif play_undo_save_quit == SAVE:
                
                savePuzzle(board, game_name)
                
            elif play_undo_save_quit == QUIT:
                
                quitGame(board)
                return

            else:

                play_undo_save_quit = input("Not a valid option! Try again: ")
            is_it_full = full(board)
            
        outcome = winOrLose(board, solved_board)
        
        if outcome:
            
            print("You won! \(^-^)/")
        else:
            print("You lost...try again next time!")

    else:

        play_solve = input("That is not valid please enter (p) or (s): ")
main()
