#Aisha Siddiq 81047072 Project 4 


class InvalidMoveError(Exception):
    '''Raises an error whenever an invalid move is made
    '''
    pass
    
class OthelloGame:

    #Public Functions 

    def __init__(self, row, column, turn, top_player_piece, bottom_player_piece):
        '''Initializes all objects inserted by the user
    '''
        self.Black = 'B'
        self.White = 'W'
        self.NONE = '.'
        self.Tie = 'NONE' 
        self._row =  row
        self._column = column
        self._turn = turn
        self._topcorner = top_player_piece
        self._bottomcorner = bottom_player_piece
        


    def create_board(self):
        '''Create the board with the four pieces in the middle
    '''
        self.game_board = []
         
        for row in range(self._row):
            self.game_board.append([self.NONE] * self._column)
        self.game_board[int(self._row/2) -1][int(self._column/2)-1] = self._topcorner
        self.game_board[int(self._row/2) -1][int(self._column/2)] = self._bottomcorner
        self.game_board[int(self._row/2)][int(self._column/2) -1] = self._bottomcorner
        self.game_board[int(self._row/2)][int(self._column/2)] = self._topcorner


    def make_move(self, row, col):
        '''The user inputs the row/col and if the move is valid, update the board
    if invalid then raise an error
    '''
        if self._valid_move(row,col):
            self._flip_pieces(row,col)
            self._turn = self._switch_color()
            self.player_score()
            
        else:
            raise InvalidMoveError()

       

    def player_score(self):
        '''Counts the score of each player
    '''
        self.total_white = 0
        self.total_black = 0
        for row in self.game_board:
            for col in row:
                if col == self.Black:
                    self.total_black += 1
                elif col == self.White:
                    self.total_white += 1            


    def winning_player(self)->bool:
        '''Returns false if there is a move on the board that is valid,  if there
    isn't then it checks if the other player has a valid move. If both players don't
    have a valid move available then there is a winning player(true)'''
        

        for row in range(self._row):
            for col in range(self._column):
                if self._valid_move(row, col):
                    return False
        self._turn = self._switch_color()
        for row in range(self._row):
            for col in range(self._column):
                if self._valid_move(row, col):
                    return False
        return True

                
    def winner_most_points(self):
        '''Winning option (player with the most points)
    '''

        
        if self.winning_player():
            if self.total_black > self.total_white:
                return self.Black
            elif self.total_white > self.total_black:
                return self.White
            else:
                return self.Tie
            

    def winner_least_points(self):
        '''Winning option (player with the least points)
    '''

        
        if self.winning_player():
            if self.total_black > self.total_white:
                return self.White
            elif self.total_white > self.total_black:
                return self.White
            else:
                return self.Tie
            
            

    #Private functions 

    def _switch_color(self):
        '''Switches the color of the players
    '''
        
        if self._turn == self.Black:
            return self.White
        elif self._turn == self.White:
            return self.Black



    def _check_valid(self, row, col, rowdelta, coldelta)->bool:
        '''Returns true if the row/col selected is a valid position on the board
    '''
        
        starting_point = self.game_board[row][col]
        seen_opposite_color = False
        
        if starting_point != self.NONE:
            return False
        else:
            for i in range(1, max(self._row, self._column)):
                if self._valid_column_number(col + coldelta * i) and self._valid_row_number(row + rowdelta * i):
                    current_point = self.game_board[row + rowdelta * i][col + coldelta * i]
                    if current_point == self._switch_color():
                        seen_opposite_color = True
                        continue
                    elif current_point == self._turn and seen_opposite_color:
                        return True
                    else:
                        return False
            return False


    def _valid_move(self, row, col)->bool:
        '''Returns true/false if there is a move on the board that is valid
    '''
        return self._check_valid(row, col, 0, 1)\
               or self._check_valid(row, col, 1, 1)\
               or self._check_valid(row, col, 1, 0)\
               or self._check_valid(row, col, 1, -1)\
               or self._check_valid(row, col, 0, -1)\
               or self._check_valid(row, col, -1, -1)\
               or self._check_valid(row, col, -1, 0)\
               or self._check_valid(row, col, -1, 1)

    def _flip_pieces(self, row, col):
        '''If the position selected is valid flip the pieces on the board
    '''
        delta = [(0,1), (1,1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for rowdelta, coldelta in delta:
            if self._check_valid(row, col, rowdelta, coldelta):
                for i in range(1, max(self._row, self._column)):
                    current_point = self.game_board[row + rowdelta * i][col + coldelta * i]
                    if current_point == self._switch_color():
                        self.game_board[row + rowdelta * i][col + coldelta * i] = self._turn
                        continue
                    else:
                        break
        self.game_board[row][col] = self._turn



    def _valid_column_number(self, valid_column)->bool:
        '''Checks to see if the piece is in a valid column
    '''
        return 0 <= valid_column < self._column
    

    def _valid_row_number(self, valid_row)->bool:
        '''Checks to see if the piece is in a valid row
    '''
        return 0 <= valid_row < self._row


    





    

    

    
    

    
        
            
            
                
                
         
