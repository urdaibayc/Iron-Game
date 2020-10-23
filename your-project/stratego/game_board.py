import pygame
from stratego import *

class GameBoard():
    # TODO: calcular BOARD_SIDE_X, BOARD_SIDE_X & add to class variables
    def __init__(self, game):
        self.game = game
        self.board_w = GAME_GRID_W
        self.board_h = GAME_GRID_H -10
        self.board = pygame.Surface((self.board_h, self.board_w))
        self.board_color = GAME_GRID_BACKGROUND
        self.board_grid_color = GAME_GRID_COLOR
        self.block_rect = (BOARD_CURSOR_H, BOARD_CURSOR_W)
        self.block = pygame.Surface(self.block_rect)
        self.cursor = pygame.Surface((BOARD_CURSOR_H,BOARD_CURSOR_W))
        self.cursor_rectx = 0
        self.cursor_recty = 0

    def draw_grid(self):

        grid_x = [x * BOARD_CURSOR_W for x in range(10)]
        grid_y = [y * BOARD_CURSOR_H for y in range(10)]
        for i in range(len(grid_y)):
            for j in range(len(grid_x)):
                pygame.draw.rect(self.block,self.board_grid_color,(0, 0, BOARD_CURSOR_H,BOARD_CURSOR_W),4)
                self.board.blit(self.block, (grid_x[j], grid_y[i]))

    def display_board(self):
        while self.game.playing == True:
            self.game.check_events()
            self.check_input()
            self.board.fill(self.board_color)
            # draw grid
            self.draw_grid()
            # draw cursor
            self.blit_screen()



    def blit_board(self):
        self.game.blit_item(self, display, self.board, (0, 5))
        pass

    def draw_board_cursor(self):
        # TODO: fix cursor draw settings
        pygame.draw.rect(self.cursor_rect,BOARD_CURSOR_COLOR,(0,0,100,300),BOARD_CURSOR_EDGE)
        self.game.draw_item(self.cursor_rect,(self.cursor_rectx, self.cursor_recty))

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
