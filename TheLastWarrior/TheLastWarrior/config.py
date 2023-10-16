"""
File: Final
Author: Sierra Brightly
Student ID: X00465282
Date:November 29, 2022

Description:
Welcome to The Last Warrior! 
This is a mini RPG. In this game, you can choose between four characters. 
Once you've made your choice it's your job to kill all the enemies with the three lives you are given. 

This file is for configurations
"""

WIN_WIDTH = 640
WIN_HEIGHT = 480
TILESIZE = 32
FPS = 60

PLAYER_LAYER = 4
ENEMY_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

ENEMY_COUNT = 10
LIVES = 3
ENEMY_SPAWN_INTERVAL = 45

PLAYER_SPEED = 3
ENEMY_SPEED = 1
KNOCK_DISTANCE = 15


RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW =(255, 255, 0)
WHITE = (255,255,255)


#B = Blocked, P = Player, T = Tree, E = Enemy
tilemap = [
    
    'TTTTTTTTTTTTTTTTTTTT',
    'T.......E..........T',
    'T..E...........E...T',
    'T...B......E...TTT.T',
    'T...BBB...........TT', 
    'T...TT.........E...T',
    'T........P......B..T',
    'T....E.....BBB.....T',
    'T......T.....B..E..T',
    'TBB..B.......B.....T', 
    'T........E.........T',
    'T....BT.......E....T',
    'T....E.............T',
    'T........B.........T',
    'TTTTTTTTTTTTTTTTTTTT', 
]

