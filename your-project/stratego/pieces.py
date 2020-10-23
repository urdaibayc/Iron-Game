import pygame
from stratego import *

class Piece():
    PADDING = 10
    OUTLINE = 3
    def __init__(self, game, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.value = 1
        self.x = 0
        self.y = 0
        self.calc_pos()

    del calc_pos(self):
    pass
