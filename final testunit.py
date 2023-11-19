import unittest
import pygame

class TestPygameInit(unittest.TestCase):
 def test_pygame_init(self):
     # Call the function and check the result
     pygame.init()
     self.assertEqual(pygame.get_error(), '')
class TestPygameDisplay(unittest.TestCase):
 def test_set_caption(self):
     # Call the function and check the result
     pygame.display.set_caption("Alien intruder")
     title, _ = pygame.display.get_caption()
     self.assertEqual(title, "Alien intruder")
     import random

class TestPygameImage(unittest.TestCase):
 def test_image_load(self):
    # Call the function and check the result
    enemyImg = pygame.image.load('enemy.png')
    self.assertIsNotNone(enemyImg)

def test_random_enemy_position(self):
   # Generate a random enemy position
   enemyX = random.randint(0, 736)
   enemyY = random.randint(50, 150)
   # Check that the position is within the expected range
   self.assertGreaterEqual(enemyX, 0)
   self.assertLessEqual(enemyX, 736)
   self.assertGreaterEqual(enemyY, 50)
   self.assertLessEqual(enemyY, 150)
class TestGameFunctions(unittest.TestCase):
 def setUp(self):
    pygame.font.init()

 def test_show_score(self):
   # Call the function and check the result
   x = 10
   y = 10
   score_value = 100
   score = pygame.font.Font('freesansbold.ttf', 32).render("Score : " + str(score_value), True, (255, 255, 255))
   self.assertIsNotNone(score)

 def test_game_over_text(self):
  # Call the function and check the result
  over_text = pygame.font.Font('freesansbold.ttf', 64).render("GAME OVER", True, (255, 255, 255))
  self.assertIsNotNone(over_text)




if __name__ == '__main__':
 unittest.main()

