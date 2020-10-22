import pygame
from stratego import *

class GameBoard():
    def __init__(self, game):
        self.game = game
        self.titlex, self.titley = self.game.DISPLAY_W/2, self.game.DISPLAY_H/11
        self.cursor_rect = pygame.Surface((100,100))
        self.cursor_rectx = 0
        self.cursor_recty = 0


    def display_board(self):
        while self.game.playing == True:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Stratego-Hack', GAME_FONT_SIZE, self.titlex, self.titley)
            self.draw_board_cursor()
            # draw grid
            # draw cursor
            self.blit_screen()

    def draw_board_cursor(self):
        pygame.draw.rect(self.cursor_rect,BOARD_CURSOR_COLOR,(0,0,50,50),0)
        self.game.draw_item(self.cursor_rect,(self.cursor_rectx, self.cursor_recty))

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
