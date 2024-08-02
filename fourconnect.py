import numpy as np

#The player class and their attributes and methods
class Player:
    def __init__(self, name, player_tag, winner=False):
        self.name = name 
        self.player_tag = player_tag
        self.winner = winner

    #Make the player choose a column for the turn 
    def choose_column(self):
        while True:
            try:
                chosen_column = int(input(f'{self.name}, where do you want to put your token? (Choose column from 1 to 7): '))
                #Uses the input minus 1 to match the index numbers 0-6
                if chosen_column in range(1, 8):
                    return chosen_column - 1
                else:
                    print("Invalid input. Please choose a valid column between 1 and 7!")

            except ValueError:
                print("Invalid input. Please enter a column between 1 and 7")

    #Creating the logic for a player turn using the methods of both classes
    def player_turn(self, board):
        column = self.choose_column()
        #get_available_row method from the board class
        row = board.get_available_row(column)
        if row != None:
            board.fill_slot(row, column, self.player_tag)
            return True
        else:
            print("Column is full! Please choose another column.")
            return False

         
    



#The board class and their attributes and their methods for game logic
class Board:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        #Making the board a 2D array of zeros using the numpy module
        self.board = np.zeros((self.rows, self.columns)) 
    
    
    def print_board(self):
        # Flip the board for correct display, as top row should be displayed first & making the index [0][0] bottom left instead of top right
        print(np.flip(self.board, 0))

    #Switch out the 0 in the index with the player_tag
    def fill_slot(self, row, column, player_tag):
        self.board[row][column] = player_tag

    def get_available_row(self, column):
        for row in range(self.rows):
            if self.board[row][column] == 0:
                return row
        return None

    #Check the winner in the relevant locations (horizontal, vertical, diagonal)
    def check_winner(self, player_tag):
        # Check horizontal locations
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if np.all(self.board[row, col:col + 4] == player_tag):
                    return True

        # Check vertical locations
        for col in range(self.columns):
            for row in range(self.rows - 3):
                if np.all(self.board[row:row + 4, col] == player_tag):
                    return True

        # Check positively diagonal locations
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if all(self.board[row + i][col + i] == player_tag for i in range(4)):
                    return True

        # Check negatively diagonal locations
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if all(self.board[row - i][col + i] == player_tag for i in range(4)):
                    return True

        return False
              

#Implement the logic-loop of the game including variables etc. 
#Use the classes to built up the game loop
def __main__():
    beginning_board = Board()
    player1 = Player("Player 1", player_tag=1)
    player2 = Player("Player 2", player_tag=2)

    players = [player1, player2]

    #Sets a turn variable to keep track of which players turn it is on even numbers the remainder is giving the turn to player1
    turn = 0

    while True:
        current_player = players[turn % 2]
        beginning_board.print_board()

        if current_player.player_turn(beginning_board):
            if beginning_board.check_winner(current_player.player_tag):
                beginning_board.print_board()
                print(f"Congratulations {current_player.name}! You win!")
                break

        turn += 1
    

if __name__ == __main__():
    main()
