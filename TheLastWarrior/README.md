File: Project 3 (but also Final Project Possibly???)
Author: Sierra Brightly
Student ID: X00465282
Date: October 15, 2023 (Continuous upgrades still happening)


Team:

Sierra Brightly

Bob

Penny

Shiro

June


Team Contributions:

Sierra: 

    Player Class:
    
    - Created player movement that allows for the "camera" to follow the character around in the game.
    
    - Collisions:
    
        -When colliding with an enemy players are kicked back and the player loses a life
        
        -When colliding with environmental objects (trees/blocks) the enemy is stopped and the camera is as well. 
        
    - Player controls (Using ASWD to move)

    
Bob: 

    Sprites and Animations:
    
    -Sourced and edited spritesheets to ensure that they will work for the game
    
    -Created the animation setting for the sprites inclduing for the Player, Enemy, and Attacks. 


Penny:

    Environmental Classes (trees, blocks, and ground):
    
    - Created Block, Tree, and Ground classes that randomize between different selections for more variety in the game
    
    - Create the tilemap, which configure which of the object can be placed where
    
    
Shiro:

    Enemy Class and Enemy Spawing:
    
    - Handled how and where the enemy spawns
    
    - Enemy Movement that allows enemies to "seek" players
    
    
June:

    Attack Class:
    
    - Handles when the player attacks the enemy, making enemies disappear and adding points to the player's score. 
    
    - Also worked on testing 
    
    

Features:

    -Menu

    -Character Selection

    -Unlimited enemies to kill that "seek" player

    -3 lives

    -Game over screen that flashes for a second after player dies

    -High score screen that pops up when a high score is achieved that allows players to input a name and save it. 

    -Score screen that shows player score after game over or high score that has buttons for back to menu, restart with that character, or exit

    -Camera follows character

    -Player is kicked back by enemy attack

    -Animations in movement and attack

    -Plays Music


Sources:

    ShawCode: https://www.youtube.com/watch?v=crUF36OkGDw
        Basic layout for game
        spritesheets

    EdZoft: https://www.youtube.com/watch?v=EI1tJkUu5ms
        character selection

    https://pipoya.itch.io/pipoya-free-rpg-character-sprites-32x32
        spritesheets

    https://lamorapedia.itch.io/grasslands-pixel-art-top-down
        spritesheets

    
    (Watching for better examples for enemy movement)



Current WIPs:


    1. Fix gameover menu(Some text not smooth and print test is failing for a single button press. Possible issue with loop/rendering/updating???) Maybe split it into different methods? (DONE)

        1.1 Totally redid the game over section and this created a new problem that makes the Game over screen not dissapear until a mouse is moved to go on to the next screen and for some reason takes you back to the highscore screen not the menu (Rendering issues?)

    2. Fix enemy movement and spawning. Not happy with it.

    3. Fix the back button highscore entry section of the gameover screen. (Possible path forward is known) (DONE)

    4. Fix it so that the mouse doesn't change anything during the game. (DONE)

    5. Clean up code so it's more standard. 

    6. Create more tests.



Future Future Upgrades:

    1. Have each character have their own style of attack

    2. Have settings (difficulty level, sounds, etc.)

    3. Have a pause game option which allows you to change settings or return to the menu. 

    4. have music switch between home, game play, and game over screens. 

    5. Make lives into a heart system and possible have a heart drop for every n number of enemies killed. 


    




    


