import pygame

class Tablero():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.cursor_rect = pygame.Rect(0,0,20,20) # Rect(x,y,w,h)

    def display_board(self):
        pass
        # self.run_display = True
        # while self.run_display:
        #     self.game.check_events()
        #     self.check_input()
        #     self.game.display.fill(self.game.BLACK)
        #     self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -20)
        #     self.game.draw_text('Start Game', 20, self.startx, self.starty)
        #     self.game.draw_text('Options', 20, self.optionsx, self.optionsy)
        #     self.game.draw_text('Credits', 20, self.creditsx, self.creditsy)
        #     self.draw_cursor()
        #     self.blit_screen()

    def draw_cursor(self):
            pass
            # self.game.draw_text('->', 50,self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        pass
        # self.game.window.blit(self.game.display, (0,0))
        # pygame.display.update() # "send to monitor"
        # self.game.reset_keys()
