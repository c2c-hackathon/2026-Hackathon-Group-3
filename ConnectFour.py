import typing
import time

from NeoTrellisGame import NeoTrellisGame, AbstractNeoTrellisGame, Action
from adafruit_neotrellis.multitrellis import MultiTrellis
from adafruit_neotrellis.neotrellis import NeoTrellis
from Colors import *

class ConnectFour:
    def __init__(self, board: typing.Optional[AbstractNeoTrellisGame] = None):
        self.board = board if board is not None else NeoTrellisGame()
        super().__init__()

        self.choose_color = True
        self.game = False
        self.p1 = None
        self.p2 = None
        self.current_player = self.p1

        self.register_callbacks()

        self.choose_list = [OFF, RED, GREEN,PINK, BLUE, ORANGE, PURPLE, OFF]
        for i in range(8):
            self.board.set_cell_color(i, 0, self.choose_list[i])
        self.board.update_display()


        self.game_state = [
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE]
        ] #TODO: Choose a structure to represent what pieces are currently in the game board
        # self.update_board_colors()

    def reset_game(self):
        #TODO reset the game state to its original empty state
         self.game_state = [
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE]
        ]

    def register_callbacks(self):
        #TODO: Register callbacks that will be run when buttons are pressed and released
        self.board.set_callback(0, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
        self.board.activate_key(0, 0, Action.BUTTON_PRESSED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable

        self.board.set_callback(1, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
        self.board.activate_key(1, 0, Action.BUTTON_PRESSED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable

        self.board.set_callback(2, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
        self.board.activate_key(2, 0, Action.BUTTON_PRESSED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable

        self.board.set_callback(3, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
        self.board.activate_key(3, 0, Action.BUTTON_PRESSED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable

        self.board.set_callback(4, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
        self.board.activate_key(4, 0, Action.BUTTON_PRESSED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable
        
        self.board.set_callback(5, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
        self.board.activate_key(5, 0, Action.BUTTON_PRESSED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable

        self.board.set_callback(6, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
        self.board.activate_key(6, 0, Action.BUTTON_PRESSED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable

        self.board.set_callback(7, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
        self.board.activate_key(7, 0, Action.BUTTON_PRESSED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable

        pass
  
    def handle_button_event(self, x:int, y: int, action: Action):
        """
        This is an example of how a callback function will look. It takes an x value, y value, and action, which will indicate what button activated the callback and what action the user did to run it.
        See NeoTrellisGame.set_callback() for info about callbacks.
        """
        #TODO: Implement what will happen when the button at position x,y is pressed or released
        if self.choose_color:
            if self.current_player == self.p1:
                self.p1 = self.choose_list[x]
                self.board.set_cell_color(x,y,OFF)
                self.board.update_display()
                self.current_player = self.p2
            elif self.current_player == self.p2:
                self.p2 = self.choose_list[x]
                self.current_player = self.p1
                self.update_board_colors()
                self.choose_color = False
                self.game = True
                self.current_player = self.p1

        
        print(str(self.p1) + "   " + str(self.p2))

        if self.game:
            self.show_current_player()
            
            # yc = 2
            # while yc < 8:
            #     self.board.set_cell_color(x,yc, self.current_player)
            #     yc = yc + 1

            #     time.sleep(0.1)
            #     self.board.update_display()
            #     self.board.set_cell_color(x,yc-1, WHITE)
            #     time.sleep(0.1)
            #     self.board.update_display()
            #     self.game_state[self.find_lowest_empty_row(x)][x] = self.current_player
            #     self.update_board_colors()
            if self.find_lowest_empty_row(x) == -1: pass
            self.game_state[self.find_lowest_empty_row(x)][x] = self.current_player
            self.update_board_colors()
            self.board.play_sound("clack.mp3")

            if self.check_win():
                print("adhfjklashfkjuerhfkhelksifrhlkjasdhfljasdhflkhjdasfd")
                self.show_winner()
                self.board.play_sound("cheer.mp3")
                time.sleep(3)
                self.game = False
                self.choose = True
                self.reset_game()
                self.update_board_colors()
                self.choose_list = [OFF, RED, GREEN,PINK, BLUE, ORANGE, PURPLE, OFF]
                for i in range(8):
                    self.board.set_cell_color(i, 0, self.choose_list[i])
                self.board.update_display()
                self.game = True

            if self.current_player == self.p1:
                self.current_player = self.p2
            elif self.current_player == self.p2:            
                self.current_player = self.p1 
             

    def find_lowest_empty_row(self, col: int):
        c = []
        for i in self.game_state:
            c.append(i[col])
        print(f"CCCCCCC {c}")
        
        c = c[::-1]
        a = 0
        for b in c:
            print(b)
            if b == WHITE:
                return 5 - a
            a += 1
            print(a)
            if a >= 6:
                self.board.play_sound("ding.mp3")
                return -1
        """
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
            [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE]
        """

    def place_piece(self, col: int):
        #TODO: Finds the legal move in the column, and updates the game state to reflect the new piece, checking to see if a player has won with that new piece. Don't forget to play a sound!
        pass

    def update_board_colors(self):
        #TODO: Taie the current game state and update the board colors accordingly. Hint: look at NeoTrellisGame.py for functions to update the colors and display the colors
        for a in range(6):
            for b in range(8):
                self.board.set_cell_color(b, a+2, self.game_state[a][b])
            
        self.board.update_display()
        

    def switch_player(self):
        #TODO: Change which player is curently placing a piece. Keep track of this in some sort of variable
        pass

    def show_current_player(self):
        for i in range(8):
            if self.current_player == self.p1:
                self.board.set_cell_color(i, 0, self.p2)
            elif self.current_player == self.p2:
                self.board.set_cell_color(i, 0, self.p1)
            self.board.update_display()
        pass

    def check_win(self):

        inarow = 1
        prevr = 0

        for r in self.game_state:
            for i in r:
                if i == prevr and i != WHITE:
                    inarow += 1
                    # prevr = self.find_lowest_empty_row(x)
                    prevr = i
                else:
                    inarow = 1
                    prevr = i
                if inarow == 4:
                    return True
        
        inarow = 1
        
        for col in range(8):
            c = []
            for i in self.game_state:
                c.append(i[col])

            prevc = 0
            for i in c:
                if i == prevr and i != WHITE:
                    inarow += 1
                    prevr = i
                else:
                    inarow = 1
                    prevr = i
                if inarow == 4:
                    return True

        inarow = 1
        prevd = 0

        for a in range(6):
            for b in range(8):
                if self.game_state[a][b] != WHITE:
                    try:
                        if self.game_state[a][b] == self.game_state[a+1][b+1] == self.game_state[a+2][b+2] == self.game_state[a+3][b+4]:
                            return True
                    except:
                        pass
        
        for a in range(6):
            for b in range(8):
                if self.game_state[a][b] != WHITE:
                    try:
                        if self.game_state[a][b] == self.game_state[a-1][b+1] == self.game_state[a-2][b+2] == self.game_state[a-3][b+4]:
                            return True
                    except:
                        pass

        # for a in range(6):
        #     for b in range(8):
        #         if self.game_state[a][b] != WHITE and self.game_state[a][b] == prevd:
        #             inarow += 1
        #             prevd = self.game_state[a][b]
        #         else:
        #             inarow = 1
        #             if (a+1 < 6 and a+1 > 0) and (b+1 < 8 and b+1 > 0):
        #                 prevd = self.game_state[a+1][b+1]
        #             else:
        #                 prevd = 0
        #         if inarow == 4:
        #             return True
        
        # inarow = 1
        # prevd = 0
        # for a in range(6):
        #     for b in range(8):
        #         if self.game_state[a][b] != WHITE and self.game_state[a][b] == prevd:
        #             inarow += 1
        #             prevd = self.game_state[a][b]
        #         else:
        #             inarow = 1
        #             if (a+1 < 6 and a+1 > 0) and (b-1 < 8 and b-1 > 0):
        #                 prevd = self.game_state[a+1][b-1]
        #             else:
        #                 prevd = 0
        #         if inarow == 4:
        #             return True
        


        

    def show_winner(self):
        current_player = self.current_player
        self.game_state = [
            [current_player, current_player, current_player, current_player, current_player, current_player, current_player, current_player],
            [current_player, current_player, current_player, current_player, current_player, current_player, current_player, current_player],
            [current_player, current_player, current_player, current_player, current_player, current_player, current_player, current_player],
            [current_player, current_player, current_player, current_player, current_player, current_player, current_player, current_player],
            [current_player, current_player, current_player, current_player, current_player, current_player, current_player, current_player],
            [current_player, current_player, current_player, current_player, current_player, current_player, current_player, current_player],
        ]
        self.update_board_colors()

    def show_tie_game(self):
        #TODO: Display on the board that there was a draw
        pass


    def is_board_full(self):
        #TODO: Return whether or not the game state has no more legal moves
        pass  

    def get_player_color(self, player) -> tuple[int, int, int]:
        #TODO: Return the color for the given player 
        pass

    def is_column_full(self, col: int):
        #TODO: Return if the given column is currently full
        pass