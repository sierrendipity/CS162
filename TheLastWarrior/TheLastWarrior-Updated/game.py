import sys
import pygame
import sys
import pygame
from player import Player
from enemy import Enemy
from attack import Attack
from environment import*
from spritesheet import*
from settings import *
from button import Button
from highscoremanager import*

class Game:
    """class for game"""

    def __init__(self):
        """initializes the atrtibuts of game class """

        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.char_selection = 1
        self.font = pygame.font.Font('Amatic_Bold.ttf', 96)
        self.smediumfont = pygame.font.Font('Amatic_Bold.ttf', 60)
        self.smallfont = pygame.font.Font('Amatic_Bold.ttf', 32)
        self.largefont = pygame.font.Font('Amatic_Bold.ttf', 140)
        self.running = True
        self.highscore_manager = HighscoreManager()
        self.highscore_manager.load_highscores()
        self.enemy_spawn_timer = 0
        self.enemies = pygame.sprite.Group()
        self.char_select_spritesheet = Spritesheet('images/character_select.png')
        self.char_dictionary = {
            1: Spritesheet('images/valen.png'),
            2: Spritesheet('images/stella.png'),
            3: Spritesheet('images/basil.png'),
            4: Spritesheet('images/soren.png'),
        }
        self.character_spritesheet = self.char_dictionary[self.char_selection]
        self.terrain_spritesheet = Spritesheet('images/terrain.png')
        self.props_spritesheet = Spritesheet('images/props.png')
        self.attack_spritesheet = Spritesheet('images/attack.png')
        self.enemy_spritesheet = Spritesheet('images/enemy01.png')
        self.intro_background = pygame.image.load('./images/introbackground.png')
        self.intro2_background = pygame.image.load('./images/intro2background.png')
        self.choose_char_background = pygame.image.load('./images/char_select_background.png')
        self.game_over_background = pygame.image.load('./images/gameover.png')
        self.game_won_background = pygame.image.load('./images/gamewon.png')
        self.controls_background = pygame.image.load('./images/controls.png')

    def spawn_enemy(self):
        """Creates a new enemy in a valid spawn location"""
        
        valid_spawn_locations = self.get_valid_spawn_locations()
        
        if valid_spawn_locations:
            x, y = random.choice(valid_spawn_locations)
            new_enemy = Enemy(self, x, y)
            self.enemies.add(new_enemy)

    def create_tilemap(self):
        """creates the tilemap for the game, from the info in config"""

        #itterates through tilemap
        for i, row, in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column =='B':
                    Block(self, j, i)
                if column == 'P':
                    self.player = Player(self, j, i)
                if column == 'E':
                    Enemy(self, j, i)
                if column == 'T':
                    Tree(self, j, i)

    def get_valid_spawn_locations(self):
        """Sets valid spawn areas for the enemies."""
        
        # Initialize an empty list to store valid spawn locations
        valid_spawn_locations = []

        # Iterate through the tilemap to find grass locations and determine the boundaries
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == '.':
                    valid_spawn_locations.append((j, i))

        return valid_spawn_locations

    def new(self):
        """a new game starts"""

        self.playing = True
        
        #a group of sprites we can control easily
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.trees = pygame.sprite.LayeredUpdates()
        self.key = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.create_tilemap()

    def events(self):
        """game loop events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y)

    def update(self):
        """Game loop updates"""

        try:
            self.all_sprites.update()

            # Decrement the enemy spawn timer
            self.enemy_spawn_timer -= 1
            if self.enemy_spawn_timer <= 0:
                # Reset the timer to the spawn interval
                self.enemy_spawn_timer = ENEMY_SPAWN_INTERVAL
                # Get a list of valid spawn locations based on the positions of trees
                valid_spawn_locations = self.get_valid_spawn_locations()
                if valid_spawn_locations:
                    # Randomly choose a location from the list and spawn an enemy there
                    self.spawn_enemy()
        except pygame.error:
            raise SystemExit("Error")

    def draw(self):
        """draw them here"""


        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        #framerate
        self.clock.tick(FPS)

        pygame.display.update()

    def char_update(self):
        self.char_dictionary = {
            1: Spritesheet('images/valen.png'),
            2: Spritesheet('images/stella.png'),
            3: Spritesheet('images/basil.png'),
            4: Spritesheet('images/soren.png'),
        }
        self.character_spritesheet = self.char_dictionary[self.char_selection]
        self.new()

    def main(self):
        """game loop"""

        try:
            while self.playing:
                self.update()
                self.events()
                self.stats(self.player.score,self.player.lives)
                self.draw()
        except pygame.error:
            raise SystemExit("Error")
            
    def stats(self, score, lives):
        # Render the player's score, lives, and time
        score_text = self.smallfont.render("SCORE: " + str(score), True, WHITE)
        score_rect = score_text.get_rect(x=80, y=0)

        lives_text = self.smallfont.render('LIVES: ' + str(lives), True, WHITE)
        lives_rect = lives_text.get_rect(x=0, y=0)

        # Get the current time in milliseconds and convert it to seconds
        current_time = pygame.time.get_ticks() // 1000
        time_text = self.smallfont.render('TIME: ' + str(current_time), True, WHITE)
        time_rect = time_text.get_rect(x=160, y=0)

        # Blit the text onto the screen
        self.screen.blit(score_text, score_rect)
        self.screen.blit(lives_text, lives_rect)
        self.screen.blit(time_text, time_rect)
        pygame.display.update()
        
    def countdown_game_over(self, remaining_time):
        """Recursive countdown function for game over screen."""

        if remaining_time > 0:
            pygame.time.delay(1000)  # Pause for 1 second
            self.countdown_game_over(remaining_time - 1)
        else:

            if self.highscore_manager.is_highscore(self.player.score):
                self.show_high_score()
            else:
                self.show_score()

    def game_over(self):
        """Game Over"""

        game_over = True

        title = self.largefont.render('Game Over', True, BLACK)
        title_rect = title.get_rect(x=150, y=100)

        # Record the time when the game over screen was initiated
        game_over_start_time = pygame.time.get_ticks()

        while self.running and game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Clear the screen at the beginning of each frame
            self.screen.blit(self.game_over_background, (0, 0))

            # Display the game over title
            self.screen.blit(title, title_rect)

            # Calculate the elapsed time since the game over screen was initiated
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - game_over_start_time

            # If right time has passed, transition to score screen
            if elapsed_time >= 1000:
                game_over = False
                # Start the countdown when the game over screen is displayed
                self.countdown_game_over(1)

            self.clock.tick(FPS)
            pygame.display.update()

        self.screen.fill(BLACK)

    def show_score(self):
        """Game over menu """
        show_score = True

        title_upper = self.smediumfont.render("THE LAST BRAVE", True, BLACK)
        title_upper_rect = title_upper.get_rect(x=300, y=30)

        title_lower = self.smediumfont.render("WARRIOR'S SACRIFICE", True, BLACK)
        title_lower_rect = title_lower.get_rect(x=250, y=90)

        # Clear the screen at the beginning of each frame
        self.screen.blit(self.intro2_background, (0, 0))

        # Display the game over title
        self.screen.blit(title_upper, title_upper_rect)
        self.screen.blit(title_lower, title_lower_rect)

        # Display the player's score in the middle of the screen
        score_text = self.largefont.render(f'Score: {self.player.score}', True, BLACK)
        score_rect = score_text.get_rect(x=225, y=170)
        self.screen.blit(score_text, score_rect)

        menu_button = Button(80, 380, 140, 35, WHITE, BLACK, 'Return To Menu', 32)

        restart_button = Button(260, 380, 120, 35, WHITE, BLACK, 'Restart Game', 32)

        exit_button = Button(440, 380, 100, 35, WHITE, BLACK, 'Exit Game', 32)

        
        while self.running and show_score:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            # If the menu button is pressed, go to the menu
            if menu_button.is_pressed(mouse_pos, mouse_pressed):
                show_score = False
                self.new()
                self.intro_screen('Start Game')

            # If the restart button is pressed, restart the game
            elif restart_button.is_pressed(mouse_pos, mouse_pressed):
                show_score = False
                self.main()
                self.new()

            # If the exit button is pressed, exit the game
            elif exit_button.is_pressed(mouse_pos, mouse_pressed):
                show_score = False
                self.running = False

            self.screen.blit(menu_button.image, menu_button.rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)

            self.clock.tick(FPS)
            pygame.display.update()
 
    def show_high_score(self):
        """Enter High Score """
        show_high_score= True
        entering_name = False
        player_name = ""
        score_saved = False

        title = self.font.render("YOU HAVE A HIGH SCORE", True, YELLOW)
        title_rect = title.get_rect(x=55, y=50)

        save_button = Button(400, 280, 100, 40, WHITE, BLACK, 'SAVE SCORE', 32)
        
        while self.running and show_high_score:
            for event in pygame.event.get():

                # Clear the screen at the beginning of each frame
                self.screen.blit(self.game_won_background, (0, 0))

                # Display the high score title
                self.screen.blit(title, title_rect)

                if event.type == pygame.QUIT:
                    self.running = False

                entering_name = True

                # Display the instruction to enter a name
                enter_name_text = self.font.render('ENTER NAME', True, BLACK)
                enter_name_rect = enter_name_text.get_rect(x=200, y=150)
                self.screen.blit(enter_name_text, enter_name_rect)

                # Display 3 lines for name
                name_place_text = self.smallfont.render('_    _    _', True, WHITE)
                name_place_rect = name_place_text.get_rect(x=285, y=315)
                self.screen.blit(name_place_text, name_place_rect)

                if entering_name:
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha() and len(player_name) < 3:
                            player_name += event.unicode
                        
                        elif event.key == pygame.K_BACKSPACE:
                            print("Backspace key pressed")
                            player_name = player_name[:-1]

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            #if the player name has 3 characters show the save button
            if len(player_name) == 3:
                self.screen.blit(save_button.image, save_button.rect)

            if save_button.is_pressed(mouse_pos, mouse_pressed) and not score_saved:
                self.highscore_manager.add_highscore(player_name, self.player.score)
                self.highscore_manager.save_highscores()
                score_saved = True  # Set the flag to True to indicate that the score has been saved
                show_high_score= False
                self.show_score()
                print("name saved")
            else:
                score_saved=False

            # Display the entered name
            if entering_name:
                name_text = self.font.render(player_name, True, WHITE)
                name_rect = name_text.get_rect(x=285, y=240)
                self.screen.blit(name_text, name_rect)

            self.clock.tick(FPS)
            pygame.display.update()  
              
        self.screen.fill(BLACK)    

    def highscore_screen(self):
        """Display high scores on a screen."""

        highscore = True

        highscores = self.highscore_manager.get_highscores()

        highscore_title = self.font.render('High Scores', True, WHITE)
        highscore_title_rect = highscore_title.get_rect(center=(WIN_WIDTH // 2, 50))

        back_button = Button(276, 420, 85, 30, WHITE, BLACK, 'Back to Menu', 24)

        while highscore is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    highscore = False
                    pygame.quit()
                    sys.exit()

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if back_button.is_pressed(mouse_pos, mouse_pressed):
                highscore = False
                self.intro_screen('Start Game')  # Return to the intro screen

            # Clear the screen
            self.screen.fill(BLACK)

            # Display high scores
            column1_scores = highscores[:5]
            column2_scores = highscores[5:10]

            y_pos = 130
            for i, score in enumerate(column1_scores):
                score_text = self.smallfont.render(f"{i + 1}. {score}", True, WHITE)
                score_rect = score_text.get_rect(x=240, y=y_pos)
                self.screen.blit(score_text, score_rect)
                y_pos += 40

            y_pos = 130
            for i, score in enumerate(column2_scores):
                score_text = self.smallfont.render(f"{i + 6}. {score}", True, WHITE)
                score_rect = score_text.get_rect(x=360, y=y_pos)
                self.screen.blit(score_text, score_rect)
                y_pos += 40

            # Display back button
            self.screen.blit(back_button.image, back_button.rect)

            # Display the title
            self.screen.blit(highscore_title, highscore_title_rect)

            self.clock.tick(FPS)
            pygame.display.update()

    def intro_screen(self, startresume):
        """Intro screen menu parameters start/resume"""

        intro = True

        title1 = self.font.render('THE LAST WARRIOR', True, BLACK)
        title1_rect = title1.get_rect(x=120, y=14)

        play_button = Button(255, 140, 140, 50, WHITE, BLACK, f"{startresume}", 40)

        exit_button = Button(255, 320, 140, 50, WHITE, BLACK, 'EXIT GAME', 40)

        highscore_button = Button(255, 260, 140, 50, WHITE, BLACK, 'HIGH SCORES', 40)

        how_to_button = Button(255, 200, 140, 50, WHITE, BLACK, 'HOW TO PLAY', 40)

        while intro is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                if startresume == 'START GAME':
                    self.character_select()

            elif exit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False
                pygame.quit()
                sys.exit()

            elif highscore_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                self.highscore_screen()

            elif how_to_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                self.instructions()            

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title1, title1_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.screen.blit(highscore_button.image, highscore_button.rect)
            self.screen.blit(how_to_button.image, how_to_button.rect)

            self.clock.tick(FPS)
            pygame.display.update()

    def character_select(self):
        """Character selection screen"""

        char_sel = True
        title = self.font.render('Choose Your Character', True, BLACK)
        title_rect = title.get_rect(x=65, y=20)

        #dictionary of characters and their location on the screen
        object_dictionary = {
            "valen": [0,0],
            "stella": [32,0],
            "basil": [64,0],
            "soren": [96,0],
        }

        valen_pic = pygame.transform.scale2x(
            self.char_select_spritesheet.get_sprite(object_dictionary["valen"][0],object_dictionary["valen"][1], 
                                                    TILESIZE-9, TILESIZE-1))
        valen_rect = valen_pic.get_rect(x=60, y=200)

        stella_pic = pygame.transform.scale2x(
            self.char_select_spritesheet.get_sprite(object_dictionary["stella"][0],object_dictionary["stella"][1], 
                                                    TILESIZE-9, TILESIZE))
        stella_rect = stella_pic.get_rect(x=220, y=200)

        basil_pic = pygame.transform.scale2x(
            self.char_select_spritesheet.get_sprite(object_dictionary["basil"][0],object_dictionary["basil"][1], 
                                                    TILESIZE-6, TILESIZE))
        basil_rect = basil_pic.get_rect(x=380, y=200)

        soren_pic = pygame.transform.scale2x(
            self.char_select_spritesheet.get_sprite(object_dictionary["soren"][0],object_dictionary["soren"][1], 
                                                    TILESIZE-6, TILESIZE-1))
        soren_rect = soren_pic.get_rect(x=540, y=200)

        valen_button = Button(60, 270, 50, 30, WHITE, BLACK, 'Valen', 24)
        stella_button = Button(220, 270, 50, 30, WHITE, BLACK, 'Stella', 24)
        basil_button = Button(380, 270, 50, 30, WHITE, BLACK, 'Basil', 24)
        soren_button = Button(540, 270, 50, 30, WHITE, BLACK, 'Soren', 24)

        menu_button = Button(276, 350, 85, 30, WHITE, BLACK, 'Back to Menu', 24)

        while char_sel:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    char_sel = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if menu_button.is_pressed(mouse_pos, mouse_pressed):
                char_sel = True
                self.intro_screen('START GAME')

            elif valen_button.is_pressed(mouse_pos, mouse_pressed):
                char_sel = False
                self.char_selection = 1
                self.char_update()

            elif stella_button.is_pressed(mouse_pos, mouse_pressed):
                char_sel = False
                self.char_selection = 2
                self.char_update()

            elif basil_button.is_pressed(mouse_pos, mouse_pressed):
                char_sel = False
                self.char_selection = 3
                self.char_update()

            elif soren_button.is_pressed(mouse_pos, mouse_pressed):
                char_sel = False
                self.char_selection = 4
                self.char_update()

            self.screen.blit(self.choose_char_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(menu_button.image, menu_button.rect)
            self.screen.blit(valen_button.image, valen_button.rect)
            self.screen.blit(stella_button.image, stella_button.rect)
            self.screen.blit(basil_button.image, basil_button.rect)
            self.screen.blit(soren_button.image, soren_button.rect)
            self.screen.blit(valen_pic, valen_rect)
            self.screen.blit(stella_pic, stella_rect)
            self.screen.blit(basil_pic, basil_rect)
            self.screen.blit(soren_pic, soren_rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def instructions(self):

        instructions= True

        back_button = Button(280, 420, 85, 30, WHITE, BLACK, 'Back to Menu', 24)

        while instructions is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    instructions = False
                    pygame.quit()
                    sys.exit()

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            # Clear the screen
            self.screen.blit(self.controls_background, (0,0))

            # Display back button
            self.screen.blit(back_button.image, back_button.rect)

            if back_button.is_pressed(mouse_pos, mouse_pressed):
                  # Return to the intro screen
                  instructions = False
                  self.intro_screen('START GAME')

            self.clock.tick(FPS)
            pygame.display.update()

def run_game():
    game = Game()
    
    try:
        pygame.mixer.music.load('Hawkin - Woods.mp3')
        pygame.mixer.music.play(-1)
    except pygame.error:
        print('Cannot load sound')
    
    game.intro_screen('START GAME')
    game.new()

    # Game loop if the game is running, be in main, until playing is false, the game is over
    while game.running:
        game.main()
        game.game_over()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    run_game()