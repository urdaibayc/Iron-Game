from menu import blit_screen

class GameBoard():
    def __init__(self, game):
        self.game = game
        self.titlex, self.titley = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.cursor_rect = pygame.Rect(0, 0, BOARD_CURSOR_W, BOARD_CURSOR_H)

    def display_board(self):
        while self.game.playing = True
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)


        self.draw_text('Thanks for playing', GAME_FONT_SIZE, self.DISPLAY_W/2, self.DISPLAY_H/2)

    def check_input(self):
        pass

    def move_cursor(self):
        pass

blit_screen()
