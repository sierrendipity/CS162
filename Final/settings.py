WIDTH    = 1280
HEIGHT   = 720
FPS      = 60
TILESIZE = 64

#general colors
WATER_COLOR ='#71DDEE'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

#UI colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'


# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'media/graphics/font/Amatic_Bold.ttf'
UI_FONT_SIZE = 32

#weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic':'media/graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic':'media/graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic':'media/graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic':'media/graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic':'media/graphics/weapons/sai/full.png'}}

#magic
magic_data = {
    'flame': {'strength': 5, 'cost':20, 'graphic': 'media/graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost':10, 'graphic': 'media/graphics/particles/heal/heal.png'}}

#enemy
monster_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 
              'attack type': 'slash', 'attack_sound':'media/audio/attack/slash.wav',
              'speed': 3, 'resistance': 3, 'attack_radius': 8,'notice_radius': 360},
    'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 
              'attack type': 'claw', 'attack_sound':'media/audio/attack/claw.wav',
              'speed': 2, 'resistance': 3, 'attack_radius': 120,'notice_radius': 400},
    'spirit': {'health': 100, 'exp': 110, 'damage': 8, 
              'attack type': 'thunder', 'attack_sound':'media/audio/attack/fireball.wav',
              'speed': 4, 'resistance': 3, 'attack_radius': 60,'notice_radius': 3350},
    'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 
              'attack type': 'leaf_attack', 'attack_sound':'media/audio/attack/slash.wav',
              'speed': 3, 'resistance': 3, 'attack_radius': 50,'notice_radius': 300}}