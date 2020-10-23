##########################
#### GAME SETTINGS ####
##########################
DISPLAY_H = 600
DISPLAY_W = 1000
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
SIDE_BAR_W = DISPLAY_W -400
SIDE_BAR_H = DISPLAY_H -100
SIDE_BAR_X = DISPLAY_W - SIDE_BAR_W
SIDE_BAR_Y = 0
SIDE_BAR_COLOR = (65, 123, 90)

##########################
#### GAME BOARD #####
##########################
GAME_BOARD_W = DISPLAY_W - SIDE_BAR_W
GAME_BOARD_H = DISPLAY_H - 100
GAME_GRID_BACKGROUND = (62, 105, 144)
GAME_GRID_COLOR = (254, 225, 130)
ROWS = COLS = 10

##########################
#### CURSOR ##############
##########################
BLOCK_RECT = (0,0, GAME_BOARD_H/ROWS, GAME_BOARD_W/COLS)
BOARD_CURSOR_COLOR = (221, 96, 49)
BOARD_CURSOR_EDGE = 3

##########################
#### PIECES ##############
##########################
BLUE = (0, 0, 255)
RED = (255, 0, 0)

##########################
#### ATTRIBUTIONS ########
##########################
"""
Made by Cosme Urdaibay
urdaibayc@gmail.com

Stratego is trademark, this project is ment to be a scolar exercise.

Icons made by <a href="https://www.flaticon.com/authors/nikita-golubev" title="Nikita Golubev">Nikita Golubev</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
"""
