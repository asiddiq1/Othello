#Aisha Siddiq 81047072 Project 4 

import OthelloGame


def ROW_NUM():
    '''Prompts the user for the row number
    '''
    while True: 
        try:
            row = int(input())
            if (row >= 4 and row <=16) and row % 2 == 0:
                return row
            else:
                print('Please enter an even integer from 4-16')
                
        except ValueError:
            print('Please print an integer to specify the row number')

        

def COLUMN_NUM():
    '''Prompts the user for the column number
    '''

    while True:
        try:
            column = int(input())
            if (column >= 4 and column <=16) and column % 2 == 0:
                return column
            else:
                print('Please enter an even integer from 4-16')
                
        except ValueError:
            print('Please print an integer to specify the column number')


def first_move():
    '''Asks the user to specify who should be the first player
    '''
    while True: 
        move_first = input()
        if move_first.upper() == 'B' or move_first.upper() == 'W':
            return move_first.upper()
        else:
            print('Please enter "B" or "W" for the beginning player') 


def start_piece_position():
    '''Asks the player who will be the top left player and the bottom left player
    '''
    while True:
        
        corner_position = input()
        if corner_position.upper() == 'B':
            top_piece = corner_position
            bottom_piece = 'W'
        elif corner_position.upper() == 'W':
            top_piece = corner_position
            bottom_piece = 'B'

        else:
            print('Please enter "B" or "W" to specify to top left player')
            continue

        return (top_piece.upper(), bottom_piece.upper())


def row_column_prompt():
    '''Prompts the user for the row and column (specifies that the first 2
    values should be integers)'''
    while True: 
        try: 
            row_column = input()
            split_row_column = row_column.split()
            first_number = int(split_row_column[0])-1
            second_number = int(split_row_column[1])-1
            return (first_number, second_number)
        except:
            print('INVALID')
            

def insert_row_column(row, column):
    '''Prompts the user to input a row and column number
    '''
    while True:
        first_number, second_number = row_column_prompt()
        if (0 <= first_number < row) and (0 <= second_number < column):
            return (first_number, second_number)
        else:
            print('INVALID')


def print_board(game_state):
    '''Prints the board of the game
    '''

    for table in game_state.game_board:
        for board in table:
            print(board, end = ' ')
        print()


def print_turn(game_state):
    '''Prints whose turn it is
    '''
    print('TURN:', game_state._turn)
    

def print_score(game_state):
    '''Prints the current score of the game
    '''
    print('{}: {} {}: {}'.format(game_state.Black, game_state.total_black,
                                 game_state.White, game_state.total_white))



        
def play_Othello():
    '''Implements the game in a single function
    '''
    row = ROW_NUM()
    column = COLUMN_NUM()
    who_plays_first = first_move()
    top_piece, bottom_piece = start_piece_position()
    game_state = OthelloGame.OthelloGame(row, column, who_plays_first, top_piece, bottom_piece)
    game_state.create_board()

    while True: 
        winning_player = input()
        if winning_player != '>' and winning_player != '<':
            print('Please enter ">" or "<" to specify the winning method')
            continue
        break
               
    game_state.player_score()

    print_score(game_state)
    print_board(game_state)
    print_turn(game_state)


    
    while True:
        
        (row_number, column_number) = insert_row_column(row, column)
        
        
        try:

            game_state.make_move(row_number, column_number)
            
            if game_state.winning_player():
               break
            print('VALID') 
            print_score(game_state) 
            print_board(game_state)
            print_turn(game_state) 
       
        except:
            print('INVALID')

        
        
    if winning_player == '>':
        winner = game_state.winner_most_points()
        
    elif winning_player == '<':
        winner = game_state.winner_least_points()
    
    print_score(game_state) 
    print_board(game_state)        
    print('WINNER:', winner) 


if __name__ == '__main__':
    play_Othello()






 
    

    

