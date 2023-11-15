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

1) TestIsCollision:Validates the isCollision function, checking if it accurately detects a collision between an enemy and a bullet based on their coordinates.
2) TestShowScore:Tests the show_score function, specifically verifying that the score value is correctly rendered on the game screen at the specified coordinates.
3) TestGameOverText:Utilizes mocking to test the game_over_text function. Ensures that the "GAME OVER" text is rendered with the expected parameters, including color and
rendering mode, and is placed at the specified coordinates.
4) TestPlayerFunction:Focuses on the player function, mocking the Pygame display functions. Verifies that the player's image (playerImg) is correctly blitted onto
the game screen at the provided coordinates.
5) TestEnemy:Sets up an instance of the game (Game class) and tests the enemy function within this context. It checks if an enemy is created at the specified coordinates
    on the game screen.
6) TestFireBullet:Ensures the fire_bullet function behaves as expected. It checks the state change (bullet_state), tests if the bullet image is
    correctly rendered at the specified coordinates, and verifies the pixel color at the rendered bullet's location.
