# Alien--intruder
This game is chosen because it's easy to learn and teaches the basics of game development using Python and Pygame. Its classic Alien-intruder
style is familiar and enjoyable, making it a friendly starting point for beginners while allowing room for more features to be added later.

This Python code utilizes the Pygame library to create a basic 2D game titled "Alien Intruder." It establishes the game environment, including the screen,
background, and sound effects. The player, represented by a spaceship, can be moved horizontally using arrow keys and fires bullets with the spacebar.
Multiple enemies traverse the screen horizontally and descend upon reaching the edges. The game employs collision detection to identify interactions between bullets
and enemies, triggering explosion sounds and updating the player's score. A "Game Over" message is displayed if any enemy reaches the screen's bottom. 
The code features continuous updates through a game loop, ensuring dynamic gameplay. The visuals include images for the player, enemies, bullets, and icons,
enhancing the gaming experience. 

#Description on test unit code;
import unittest
import pygame
These lines import the necessary modules for unit testing (unittest) and Pygame. The unittest module provides a testing framework, and Pygame is a set of Python modules designed for writing video games.
class TestPygameInit(unittest.TestCase):
This line defines a test class named TestPygameInit, which inherits from unittest.TestCase. Test classes are used to group related test methods together.
 def test_pygame_init(self):
This line defines a test method named test_pygame_init within the TestPygameInit class. Test methods should start with the word "test" to be recognized by the testing framework.
     pygame.init()
     self.assertEqual(pygame.get_error(), '')
Within the test_pygame_init method, these lines initialize Pygame using pygame.init() and then use self.assertEqual to check if there are no errors by verifying that pygame.get_error() returns an empty string.
class TestPygameDisplay(unittest.TestCase):
This line defines another test class named TestPygameDisplay.
 def test_set_caption(self):
This line defines a test method named test_set_caption within the TestPygameDisplay class.
     pygame.display.set_caption("Alien intruder")
     title, _ = pygame.display.get_caption()
     self.assertEqual(title, "Alien intruder")
Within the test_set_caption method, these lines set the caption of the Pygame display to "Alien intruder" and then use self.assertEqual to check if the caption is set correctly by comparing it to the expected value.
     import random
This line imports the random module, which is used later in the code.
class TestPygameImage(unittest.TestCase):
This line defines a test class named TestPygameImage.
 def test_image_load(self):
This line defines a test method named test_image_load within the TestPygameImage class.
    enemyImg = pygame.image.load('enemy.png')
    self.assertIsNotNone(enemyImg)
Within the test_image_load method, these lines attempt to load an image named 'enemy.png' using pygame.image.load() and then use self.assertIsNotNone to check if the image is successfully loaded.
def test_random_enemy_position(self):
This line defines another test method named test_random_enemy_position within the TestPygameImage class.
   enemyX = random.randint(0, 736)
   enemyY = random.randint(50, 150)
Within the test_random_enemy_position method, these lines generate random X and Y coordinates for an enemy within specified ranges.
   self.assertGreaterEqual(enemyX, 0)
   self.assertLessEqual(enemyX, 736)
   self.assertGreaterEqual(enemyY, 50)
   self.assertLessEqual(enemyY, 150)
These lines use assertion methods to check that the generated enemy position coordinates are within the expected ranges.
The following part of the code defines more test classes (TestGameFunctions) and test methods (test_show_score and test_game_over_text) with similar structures. These test methods check various aspects of game functions related to displaying scores and game over text.
if __name__ == '__main__':
 unittest.main()
This line runs the tests when the script is executed directly (not imported as a module). The unittest.main() function discovers and runs the tests defined in the script.
