import pygame
from .menu import *
from stratego import *
from .piece import Piece

class GameBoard:
    # TODO: calcular BOARD_SIDE_X, BOARD_SIDE_X & add to class variables
    def __init__(self, game):
        self.game = game
        self.board_color = GAME_BOARD_BACKGROUND
        self.board_x = 50
        self.board_y = 50
        self.board_h = GAME_BOARD_H
        self.board_w = GAME_BOARD_W
        self.side_bar_x = self.board_w + 100
        self.side_bar_h = SIDE_BAR_H
        self.side_bar_w = SIDE_BAR_W
        self.side_bar_color = SIDE_BAR_COLOR
        self.square_h = BLOCK_H
        self.square_w = BLOCK_W
        self.reg = []
        self.populate_board()

    ##########################
    #### functions ###########
    ##########################
    def check_input(self):
        if self.game.START_KEY:
            self.game.playing = False

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update() # "send to monitor"
        self.game.reset_keys()

    def display_board(self):
        while self.game.playing == True:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            # board
            self.draw_squares()
            for row in range(ROWS):
                for col in range(COLS):
                    piece = self.reg[row][col]
                    if piece != 0:
                        piece.draw_piece()
            # side_bar
            self.draw_side_bar()
            # send to display
            self.blit_screen()

    def draw_squares(self):
        pygame.draw.rect(self.game.display, self.board_color, (self.board_x, self.board_y,self.board_w, self.board_h), 0)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(self.game.display, GRAY, ((row*self.square_h)+self.board_y, (col *self.square_w)+self.board_x,self.square_h,self.square_h),0)

    def draw_side_bar(self):
        pygame.draw.rect(self.game.display, self.side_bar_color, (self.side_bar_x, 0,self.side_bar_w, self.side_bar_h), 0)


    def populate_board(self):
        for row in range(ROWS):
            self.reg.append([])
            for col in range(COLS):
                if row < 2:
                    self.reg[row].append(Piece(self.game, row, col, BLUE))
                elif row > 7:
                    self.reg[row].append(Piece(self.game, row, col, RED))
                else:
                    self.reg[row].append(0)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        # Evaluate if fight, same team, etc.

    def get_piece(self, row, col):
        return self.reg[row][col]

    def get_row_col_from_mouse(self):
        x, y = self.game.MOUSE_POS
        row = y//self.square_h
        col = x//self.square_w
        return row, col
