class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Use a single list to rep 3x3 board
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range (3)]:
            print('| ' + '| '.join(row) + ' |')
    
    @staticmethod
    def print_board_num():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [ [str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + '| '.join(row) + ' |')
    
    def available_moves(self):
        #return the the list of index of space spot in board
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board #return boolean
    
    def num_empty_squares(self):
        #return len(self.available_moves())
        return self.board.count(' ')

    def make_move (self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return ture. If invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winer if 3 in a row.....
        # First Check the row
        row_index = square // 3 #Floor division
        row = self.board[row_index*3 : (row_index + 1)*3]
        if all([spot == letter for spot in row]): #all function return true if all items are true
            return True

        #check column
        col_index = square % 3
        col = self.board[]

def play (game, x_player, o_player, print_game = True):
    # return the winner of the game! or None for a tie
    if print_game:
        game.print_board_num()

    letter = 'X' #Starting letter
    # iterate while the game still has empty squares (dont worry about winner bc return that which breaks the loop)
    while game.empty_squares():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # Define the function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()
                print('') #Print new lines

            if game.current_winner:
                if print_game:
                    print(letter + " Win! ")
                return letter
        
        #After we made a move, alternate letters
        letter = 'O' if letter == 'X' else 'X'
            
    if print_game:
        print ("Tie!")