#Aisha Siddiq 81047072 

import tkinter
import OthelloGame
import math



class OthelloGUI:

    def __init__(self, rows, columns, firstplayer, upperleftcorner, bottomcorner, winning_condition):



        self._dialog_window = tkinter.Toplevel()

        self.winning_condition = winning_condition 


        self._canvas = tkinter.Canvas(self._dialog_window, width = 600, height = 600,
            background = '#0B851D')
        
        
        self.game_state = OthelloGame.OthelloGame(rows, columns, firstplayer, upperleftcorner, bottomcorner)
        self.game_state.create_board()
        self.game_state.player_score()

        
        self._canvas.grid(
            row = 1, column = 0, padx = 20, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)


        self._canvas.bind('<Button-1>', self._on_button_down)
        self._canvas.bind('<Configure>', self._on_canvas_resized)


        self.black_score = tkinter.StringVar()
        self.black_score.set("Black: 0")
        self.label_black_score = tkinter.Label(self._dialog_window,
                                         textvariable = self.black_score, font = ('Helvetica', 22)).grid(
                                             row = 0, column = 0, padx = 20, pady = 0, sticky = tkinter.W)

        self.white_score = tkinter.StringVar()
        self.white_score.set("White: 0")
        self.label_white_score = tkinter.Label(self._dialog_window,
                                         textvariable = self.white_score, font = ('Helvetica', 22)).grid(
                                             row = 0, column = 0, padx = 20, pady = 0, sticky = tkinter.E)


        self.display_turn = tkinter.StringVar()
        self.display_turn.set("")

        self.label_turn = tkinter.Label(self._dialog_window,
                                         textvariable = self.display_turn, font = ('Helvetica', 22)).grid(
                                             row = 2, column = 0, padx = 20, pady = 0, sticky = tkinter.S)


        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)





    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()



    def exit_tkinter(self) -> None:
        '''Exits tkinter window once the game is done
    '''
        self._dialog_window.destroy()  



    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''Resizes the board
    '''
        self._canvas.delete(tkinter.ALL)
        self._draw_grid(self.game_state._row, self.game_state._column)
        self._draw_pieces()
        self._display_score()
        self._display_turn()

    def _display_score(self):
        '''Displays the score on the board
    '''
        self.black_score.set("Black: {}".format(self.game_state.total_black))
        self.white_score.set("White: {}".format(self.game_state.total_white))
        

    def _display_turn(self):
        '''Displays the current turn on the board
    '''
        if self.game_state._turn == 'W':
            turn = "White's Turn"
        else:
            turn = "Black's Turn"
        self.display_turn.set(turn) 

    

    def _draw_pieces(self) -> None:
        '''Draws the pieces on the board
    '''
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
                
        for row in range(self.game_state._row):
            for col in range(self.game_state._column):
                if self.game_state.game_board[row][col] == self.game_state.White:
                    self._canvas.create_oval(
                        canvas_width/self.game_state._column * col, canvas_height/self.game_state._row * row,
                        canvas_width/self.game_state._column * (col + 1), canvas_height/self.game_state._row * (row +1),
                        fill = 'white')
                elif self.game_state.game_board[row][col] == self.game_state.Black:
                    self._canvas.create_oval(
                        canvas_width/self.game_state._column * col, canvas_height/self.game_state._row * row,
                        canvas_width/self.game_state._column * (col + 1), canvas_height/self.game_state._row * (row +1),
                        fill = 'black')



    def _draw_grid(self, rows, col):
        '''Creates the grid of the board
    '''

        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()


        for horizontal in range(0, int(canvas_height), int(canvas_height/rows)):
            self._canvas.create_line(0, horizontal, canvas_width, horizontal)

        for vertical in range(0, int(canvas_width), int(canvas_width/col)):
            self._canvas.create_line(vertical, 0, vertical, canvas_height)



    def _on_button_down(self, event: tkinter.Event) -> None:
        '''
        Event handler that is called when the primary mouse button
        is down within the canvas.
        '''
        

        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()


        row = math.floor((event.y/height) * self.game_state._row) 
        col = math.floor((event.x/width) * self.game_state._column)

        if not self.game_state.winning_player():

            try:
                self.game_state.make_move(row, col)
                self._canvas.delete(tkinter.ALL)
                self._draw_grid(self.game_state._row, self.game_state._column)
                self._draw_pieces()
                self._display_score()
                self._display_turn()
        
            except:
                pass

        Winner = None
        win = None
        if self.game_state.winning_player() and self.winning_condition == True: 
            Winner = self.game_state.winner_most_points()
            if Winner == 'B':
                win = 'Black'
            elif Winner == 'W':
                win = 'White'
            self.display_turn.set("Winner: {}".format(win))
            
        if self.game_state.winning_player() and self.winning_condition == False:
            Winner = self.game_state.winner_least_points()
            if Winner == 'B':
                win = 'Black'
            elif Winner == 'W':
                win = 'White'
            self.display_turn.set("Winner: {}".format(win))

        if self.game_state.winning_player():
            tkinter.Button(master = self._dialog_window, text = 'Exit', font = ('Helvetica', 22),
                              command = self.exit_tkinter).grid(row = 2, column = 0, padx = 0, pady = 0,
                                                              sticky = tkinter.W)
            
            

        
               

class OthelloWindow:

    def __init__(self):
        '''Creates the window with the buttons
    '''

        self._root_window = tkinter.Tk()

        #Title label
        self.label_title = tkinter.Label(self._root_window, text = 'Welcome to Othello!',
                                         font = ('Helvetica', 22)).grid(
                                             row = 0, column = 0, padx = 10, pady = 0, sticky = tkinter.N)


        
        #Number of Rows

        self.select_row = tkinter.StringVar()
        self.select_row.set('Rows')
        

        self.row_numbers = tkinter.OptionMenu(self._root_window, self.select_row, 4, 6, 8, 10, 12, 14, 16).grid(row = 2, column = 0, padx = 0, pady = 0,
                                                                                sticky = tkinter.N)

        #Number of Columns


        self.select_column = tkinter.StringVar()
        self.select_column.set('Columns')

        self.col_numbers = tkinter.OptionMenu(self._root_window, self.select_column, 4, 6, 8, 10, 12, 14, 16).grid(row = 3, column = 0, padx = 0, pady = 0,
                                                                                sticky = tkinter.N)


        #First Player Pick

        self.select_first_player = tkinter.StringVar()
        self.select_first_player.set('First Player')

        self.first_player_choice = tkinter.OptionMenu(self._root_window, self.select_first_player, 'Black', 'White').grid(row = 4, column = 0, padx = 0, pady = 0,
                                                                                sticky = tkinter.N)


        #Piece Position


        self.select_top_piece = tkinter.StringVar()
        self.select_top_piece.set('Top Left Color')

        self.top_piece_choice = tkinter.OptionMenu(self._root_window, self.select_top_piece, 'Black', 'White').grid(row = 5, column = 0, padx = 0, pady = 0,
                                                                                sticky = tkinter.N)


        #Winning Player Choice
        
        self.select_winning_method = tkinter.StringVar()
        self.select_winning_method.set('Winning Method') 

        self.winning_player_choice = tkinter.OptionMenu(self._root_window, self.select_winning_method, 'Highest Points', 'Lowest Points').grid(row = 6, column = 0, padx = 0, pady = 0,
                                                                                sticky = tkinter.N)

        

        #Start Button


        start_button = tkinter.Button(master = self._root_window, text = 'Start Game', font = ('Helvetica', 16),
                                      command = self.start_game).grid(row = 7, column = 0, padx = 0, pady = 0,
                                                                      sticky = tkinter.N)
        
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def start_game(self):


        try:
            
            # Obtain row and column

            rows = int(self.select_row.get())
            columns = int(self.select_column.get())

            #Obtain first player pick

            first_player = self.select_first_player.get()
            if first_player == 'Black':
                first_player = 'B'
            elif first_player == 'White':
                first_player = 'W'


            #Obtain Piece Position
            top_left_piece = self.select_top_piece.get()
            

            bottom_player = None
            if top_left_piece == 'Black':
                top_left_piece = 'B'
                bottom_player = 'W'
            elif top_left_piece == 'White':
                top_left_piece = 'W'
                bottom_player = 'B'
            

            #Obtain Winning Player

            winning_player = self.select_winning_method.get()
            if winning_player == 'Highest Points':
                winning_player = True
            elif winning_player == 'Lowest Points':
                winning_player = False 

            assert(winning_player != 'Winning Method')
            assert(first_player != 'First Player')
            assert(top_left_piece != 'Top Left Color')

            game = OthelloGUI(rows, columns, first_player, top_left_piece, bottom_player, winning_player)
            game.show()
            

        except:

            #Label to make the user to select all options before continuing the game
            
            self.option_label = tkinter.Label(self._root_window, text = 'Please select all options',
                                              font = ('Helvetica', 15)).grid(
                                                  row = 1, column = 0, padx = 0, pady = 10, sticky = tkinter.N)
            
                      
        
    def start(self)->None:
        self._root_window.mainloop()
        

    
if __name__ == '__main__':
    OthelloWindow().start() 





        
