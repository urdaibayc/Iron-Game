import pygame
##########################
#### GAME SETTINGS ####
##########################
DISPLAY_H = 600
DISPLAY_W = 900
GAME_FONT_SIZE = 20

##########################
#### MENU SETINGS ####
##########################
MENU_CURSOR_W = 50
MENU_CURSOR_H = 50
MENU_FONT_SIZE = 20

##########################
#### SIDE BAR ####
##########################
SIDE_BAR_W = 300
SIDE_BAR_H = DISPLAY_H
SIDE_BAR_COLOR = (65, 123, 90)

##########################
#### GAME BOARD #####
##########################
GAME_BOARD_W = 500
GAME_BOARD_H = 500
GAME_BOARD_BACKGROUND = (254, 225, 130)
GAME_GRID_COLOR = (254, 225, 130)
ROWS = COLS = 10
GRAY = (28, 128, 128)

##########################
#### CURSOR ##############
##########################
BLOCK_H = GAME_BOARD_H/ROWS
BLOCK_W = GAME_BOARD_W/COLS
BOARD_CURSOR_COLOR = (221, 96, 49)
BOARD_CURSOR_EDGE = 3

##########################
#### PIECES ##############
##########################
BLUE = (0, 0, 255)
RED = (255, 0, 0)
# TODO: figure out how to load images =/
#ICON = pygame.image.load('./static/strategy.png')
##########################
#### ATTRIBUTIONS ########
##########################
"""
Made by Cosme Urdaibay
urdaibayc@gmail.com

Stratego is trademark, this project is ment to be a scolar exercise.

Icons made by <a href="https://www.flaticon.com/authors/nikita-golubev" title="Nikita Golubev">Nikita Golubev</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
"""
