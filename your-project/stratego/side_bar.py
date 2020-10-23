import pygame
from stratego import *

class SideBar():
    def __init__(self, game):
        
        self.background_color = SIDE_BAR_COLOR
        self.titlex = SIDE_BAR_W/2
        self.titley = 50

    def draw_side_bar(self):
        pass


    def display_side_bar(self):
        while self.game.playing == True:
            self.side_bar.fill(self.background_color)
            self.draw_side_bar()
            self.blit_screen()
