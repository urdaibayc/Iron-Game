import pygame
from stratego import *
from .pieces impor Piece

class GameBoard():
    # TODO: calcular BOARD_SIDE_X, BOARD_SIDE_X & add to class variables
    def __init__(self, game):
        self.game = game
        self.board_color = GAME_GRID_BACKGROUND
        self.board_grid_color = GAME_GRID_COLOR

        ##########################
        #### board grid ##########
        ##########################
        self.reg = []

        ##########################
        #### cursor ##########
        ##########################
        self.cursor_rect = pygame.Rect(BLOCK_RECT)
        self.cursor_rectx = 0
        self.cursor_recty = 0

        ##########################
        #### Movement ############
        ##########################
        self.selected_piece = None

    ##########################
    #### functions ###########
    ##########################
    def draw_grid(self):
        pass

    def display_board(self):
        while self.game.playing == True:
            #####################
            #### basic setup ####
            #####################
            self.game.check_events()
            self.check_input()
            self.board.fill(self.board_color)

            #####################
            #### draw grid ####
            #####################
            self.draw_grid()
            # draw cursor
            self.blit_screen()

    def blit_board(self):
        self.game.blit_item(self, display, self.board, (0, 5))
        pass

     def create_board(self):
        for row in range(ROWS):
            self.reg.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def blit_screen(self):
        # TODO: should be a Game mtod
        self.game.window.blit(self.board, (0,0))
        pygame.display.update() # "send to monitor"
        self.game.reset_keys()

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            self.game.playing = False
        #     elif self.state == 'Options':
        #         self.game.curr_menu = self.game.options
        #     elif self.state == 'Credits':
        #         self.game.curr_menu = self.game.credits
        #     self.run_display = False
        pass

    def move_cursor(self):
        # if self.game.DOWN_KEY:
        #     if self.state == 'Start':
        #         self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
        #         self.state = 'Options'
        #     elif self.state == 'Options':
        #         self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
        #         self.state = 'Credits'
        #     elif self.state == 'Credits':
        #         self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        #         self.state = 'Start'
        # elif self.game.UP_KEY:
        #     if self.state == 'Start':
        #         self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
        #         self.state = 'Credits'
        #     elif self.state == 'Options':
        #         self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        #         self.state = 'Start'
        #     elif self.state == 'Credits':
        #         self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
        #         self.state = 'Options'
        pass
