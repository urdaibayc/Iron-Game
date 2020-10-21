import pygame
from stratego import *

class GameBoard():
    def __init__(self, game):
        self.game = game
        self.titlex, self.titley = self.game.DISPLAY_W/2, self.game.DISPLAY_H/11
        self.cursor_rect = pygame.Rect(0, 0, BOARD_CURSOR_W, BOARD_CURSOR_H)

    def display_board(self):
        while self.game.playing == True:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Stratego-Hack', GAME_FONT_SIZE, self.titlex, self.titley)
            # draw grid
            # draw cursor
            self.blit_screen()

    def draw_board_cursor(self):
        pygame.draw_rect()
        self.game.draw_item(B,self.cursor_rect,x , y)
        # self.game.draw_text('->', 50,self.cursor_rect.x, self.cursor_rect.y)
        pass

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update() # "send to monitor"
        self.game.reset_keys()

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
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
