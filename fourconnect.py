
#The player class and their attributes and methods
class Player:
    #Initialising the attributes of a the 'Player'-class
    def __init__(self, name, color, winner=False):
        self.name = name 
        self.color = color
        self.winner = winner

    #Creating the logic for a player turn
    def turn():
        pass



class Board:
    
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [['0' for _ in range(columns)] for _ in range(rows)]
    
    def print_board(self):
        for row in self.board:
            print(' '.join(row))


board = Board(6, 7)

board.print_board()