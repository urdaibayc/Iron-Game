from stratego.game import Game

def main():
    # TODO:
    """
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, 'stratego')
    image_path = os.path.join(resource_path, 'static')
    icon = pygame.image.load(os.path.join(image_path, 'strategy.png'))
    """
    # TODO: Save game
    g = Game()
    while g.running:
        g.curr_menu.display_menu()
        g.game_loop()



if __name__ == '__main__':
    main()
