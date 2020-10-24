import pygame
from stratego import *

class Piece:
    def __init__(self, game, row, col, color):
        self.game = game
        self.row = row
        self.col = col
        self.color = color
        self.value = '1'
        self.selected = False
        self.last_poss = ()
        self.turn = True
        self.out_w = BLOCK_W-10
        self.in_w = BLOCK_W-12
        self.out_h = BLOCK_H-10
        self.in_h = BLOCK_H-12
        self.x = 0
        self.y = 0
        self.calculate_pos()
        self.text_x = int(self.x + self.in_w//2)
        self.text_y = int(self.y + self.in_h//2)

    def calculate_pos(self):
        self.x = BLOCK_W*self.col+55
        self.y = BLOCK_H*self.row+55

    def draw_piece(self):
        pygame.draw.rect(self.game.display, self.game.BLACK,(self.x, self.y, self.out_w, self.out_h))
        pygame.draw.rect(self.game.display, self.color,(self.x, self.y, self.in_w, self.in_h))
        self.game.draw_text(self.value, 20, self.text_x, self.text_y)

    def move(self, row, col):
        self.last_poss = (self.x, self.y)
        self.row = row
        self.col = col
        self.calculate_pos()


    def __repr__(self):
        return str(self.color)
