from stratego.game import Game

g = Game()
while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
while g.playing:
    g.game_board.display_board()
    g.game_loop()
