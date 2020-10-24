import pygame
from stratego import *

class Piece:
    def __init__(self, game, row, col, color):
        self.game = game
        self.row = row
        self.col = col
        self.color = color
        self.value = 1
        self.selected = False
        self.last_poss = ()
        self.turn = True
        self.x = 0
        self.y = 0
        self.calculate_pos()

    def calculate_pos(self):
        self.x = BLOCK_W*self.col+55
        self.y = BLOCK_H*self.row+55

    def draw_piece(self):
        pygame.draw.rect(self.game.display, self.game.BLACK,(self.x, self.y,BLOCK_W-10, BLOCK_H-10))
        pygame.draw.rect(self.game.display, self.color,(self.x, self.y,BLOCK_W-12, BLOCK_H-12))
        #self.game.draw_text(str(self.value), 20, x, y)

    def __repr__(self):
        return str(self.color)
