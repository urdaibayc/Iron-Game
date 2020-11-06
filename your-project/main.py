from stratego.game import Game
from stratego import FPS
import pygame

def main():
    # TODO:
    """
    the reference to file is made from main
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, 'stratego')
    image_path = os.path.join(resource_path, 'static')
    icon = pygame.image.load(os.path.join(image_path, 'strategy.png'))

    draw_text is repeated in board class & game class utrs used by piece class, menu class & board class has its own
    """
    # TODO: Save game
    # TODO: regulate FPS

    g = Game()
    while g.running:

        g.curr_menu.display_menu()
        g.game_loop()
        g.clock.tick(FPS)



if __name__ == '__main__':
    main()
