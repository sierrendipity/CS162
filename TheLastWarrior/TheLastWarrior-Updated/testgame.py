import sys
import pygame
from pygame.locals import *
from unittest.mock import Mock
from game import*

def test_game():

    # Mock essential functions and methods to control their behavior
    pygame.display.init = Mock()
    pygame.mixer.music.load = Mock()
    pygame.mixer.music.play = Mock()
    pygame.event.get = Mock(return_value=[pygame.event.Event(QUIT)])

    # Create an instance of the Game class
    game = Game()

    # Mock the methods of the Game class
    game.intro_screen = Mock()
    game.char_select = Mock()
    game.new = Mock()
    game.main = Mock()
    game.game_over = Mock()

    try:
        # Attempt to run the game
        run_game()
    except SystemExit:
        pass 

    # Verify that the necessary methods are called at least once during the game execution
    game.intro_screen.assert_called_once_with('START GAME')
    game.new.assert_called_once()
    game.main.assert_called_once()
    game.game_over.assert_called_once()

# Run if this script is executed
if __name__ == '__main__':
    test_game()