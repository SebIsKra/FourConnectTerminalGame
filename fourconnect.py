import numpy as np

#The player class and their attributes and methods
class Player:
    #Initialising the attributes of a the 'Player'-class
    def __init__(self, name, winner=False, turn=0):
        self.name = name 
        #self.color = token_color
        self.winner = winner
        self.turn = turn

    #Creating the logic for a player turn
    def turn():
        choose_row = input('Where do you want to put your token? (Choose row from 1 to 7): ')

        return 


#The board class including the attributes of the board and it's methods for game logic
class Board:
    def __init__(self, rows=6, columns=7, ):
        self.rows = rows
        self.columns = columns
        #Making the board a 2D array of zeros using the numpy module
        self.board = np.zeros((self.rows, self.columns)) 
    
    
    def print_board(self):
        board = print(self.board)
        return board
    #Changes the 0 which are  to either a one or a two depending on the player
    
    def check_slot(self):
        if slot == 0:
            return True

    def fill_slot(self):
        
        if choose_row in range(1, 8):
            pass
              

#Implement the logic-loop of the game including variables etc. 
#Use the classes to built up the game loop
def __main__():
    beginning_board = Board()
    player1 = Player("Me")
    player2 = Player("You")
    beginning_board.print_board()

    if player1.turn == 0:
        beginning_board.fill_slot()
    else:
        selection = int(input("Player 2 make your selection: 1 - 7"))
    
    player1.turn += 1
    player1.turn = player1.turn % 2

    #board.fill_slot()
    

if __name__ == __main__():
    main()
