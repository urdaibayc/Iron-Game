import os
import pygame
from stratego.menu import *
from stratego.game_board import *
from stratego import DISPLAY_H, DISPLAY_W

class Game():

    def __init__(self):
        # TODO: fix icon
        pygame.init()
        pygame.display.set_caption("StrategoHackPy")
        # pygame.display.set_icon(icon)
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY,  self.RIGHT_KEY,  self.LEFT_KEY, self.START_KEY, self.BACK_KEY, self.ESC_KEY = False, False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = DISPLAY_W, DISPLAY_H
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H))) # Create a canvas on which to display everything
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H)) # Create a surface
        #self.font_name = 'font.TTF'
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.game_board = GameBoard(self)


    def game_loop(self):
        """Controls the game states, resets key flags to False"""
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.game_board.display_board()
            pygame.display.update()
            self.reset_keys()


    def check_events(self):
        # TODO: set esc key
        """sets key flags to True if triggered by the user"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running, self.playing = False, False
                    self.curr_menu.run_display = False
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_UP:
                    self.LEFT_KEY = True

    def reset_keys(self):
        """sets key flags to false"""
        self.UP_KEY, self.DOWN_KEY, self.RIGHT_KEY, self.LEFT_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False, False, False

    def draw_text(self, text, size, x,y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE) # font.render(text, antialiasing, color)
        text_rect = text_surface.get_rect() # rect obj(x,y, heigth, width)
        text_rect.center = (x,y) # coordinates
        self.display.blit(text_surface,text_rect)

    def draw_item(self, item_rect, x, y):
        self.display.blit(item_rect,t_rect)
