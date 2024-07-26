
#The player class and their attributes and methods
class Player:
    #Initialising the attributes of a the 'Player'-class
    def __init__(self, name, token_color, winner=False):
        self.name = name 
        self.color = token_color
        self.winner = winner

    #Creating the logic for a player turn
    def turn():
        pass


#The board class including the attributes of the board and it's methods for game logic
class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [['0' for slot in range(columns)] for slot in range(rows)]
    
    #Printing out a board of zeros inside the terminal
    def print_board(self):
        for row in self.board:
            print(' '.join(row))
    
    def fill_slot(self):
        input('Where do you want to put your token?')

#Implement the logic-loop of the game including variables etc. 
def __main__():
    board = Board(6, 7)#Using 6 and 7 to let the game know how long a 
    board.print_board()
    board.fill_slot()

if __name__ == __main__():
    main()
