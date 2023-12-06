import unittest
from game import Game

class TestGame(unittest.TestCase):
    def test_spawn_enemy(self):
        # Create a new Game instance
        game = Game()
        
        # Call the new() method to initialize all_sprites
        game.new()

        # Initial count of enemies
        initial_enemy_count = len(game.enemies)

        # Spawn a new enemy
        game.spawn_enemy()

        # Get the count of enemies
        new_enemy_count = len(game.enemies)
        
        # Check if number of enemies increased after
        self.assertEqual(new_enemy_count, initial_enemy_count + 1)

if __name__ == '__main__':
    unittest.main()
