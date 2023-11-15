import unittest
import math

class TestIsCollision(unittest.TestCase):
    def test_isCollision(self):
        enemyX = 5
        enemyY = 5
        bulletX = 5
        bulletY = 5
        expected = True
        distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
        result = True if distance < 27 else False
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
