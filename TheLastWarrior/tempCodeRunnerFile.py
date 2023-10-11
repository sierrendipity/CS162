    def game_over(self):
        """Game over menu"""

        game_over = True
        entering_name = False
        player_name = ""
        score_saved = False
        
        title = self.largefont.render('Game Over', True, BLACK)
        title_rect = title.get_rect(x=150, y=20)

        # Clear the screen at the beginning of each frame
        self.screen.blit(self.game_over_background, (0, 0))

        # Display the game over title
        self.screen.blit(title, title_rect)

        # Display the player's score in the middle of the screen
        score_text = self.font.render(f'Score: {self.player.score}', True, WHITE)
        score_rect = score_text.get_rect(x=230, y=160)
        self.screen.blit(score_text, score_rect)

        menu_button = Button(80, 380, 140, 30, WHITE, BLACK, 'Return To Menu', 32)

        restart_button = Button(260, 380, 120, 30, WHITE, BLACK, 'Restart Game', 32)

        exit_button = Button(440, 380, 100, 40, WHITE, BLACK, 'Exit Game', 32)

        save_button = Button(400, 280, 100, 40, WHITE, BLACK, 'Save Score', 32)
        
        while self.running and game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Check if the player's score is a high score
                if self.highscore_manager.is_highscore(self.player.score):
                    entering_name = True

                    # Display the high score message
                    highscore_text = self.smediumfont.render('HIGH SCORE!', True, YELLOW)
                    highscore_rect = highscore_text.get_rect(x=50, y=185)
                    self.screen.blit(highscore_text, highscore_rect)

                    # Display the instruction to enter a name
                    enter_name_text = self.smallfont.render('ENTER NAME:', True, WHITE)
                    enter_name_rect = enter_name_text.get_rect(x=175, y=310)
                    self.screen.blit(enter_name_text, enter_name_rect)

                    # Display 3 lines for name
                    name_place_text = self.smallfont.render('_    _    _', True, WHITE)
                    name_place_rect = name_place_text.get_rect(x=285, y=315)
                    self.screen.blit(name_place_text, name_place_rect)

                if entering_name and len(player_name) < 3:
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            player_name += event.unicode
                        #FIX THIS!!!!!
                        # elif event.key == pygame.K_BACKSPACE:
                        #     print("Backspace key pressed")
                        #     player_name = player_name[:-1]

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            # If the menu button is pressed, go to the menu
            if menu_button.is_pressed(mouse_pos, mouse_pressed):
                game_over = False
                self.intro_screen('Start Game')

            # If the restart button is pressed, restart the game
            elif restart_button.is_pressed(mouse_pos, mouse_pressed):
                game_over = False
                self.main()
                game.new()

            # If the exit button is pressed, exit the game
            elif exit_button.is_pressed(mouse_pos, mouse_pressed):
                if entering_name:
                    self.highscore_manager.add_highscore(player_name, self.player.score)
                    self.highscore_manager.save_highscores()
                self.running = False

            elif save_button.is_pressed(mouse_pos, mouse_pressed) and not score_saved:
                if entering_name and len(player_name) == 3:  # Check the length of the player's name
                    self.highscore_manager.add_highscore(player_name, self.player.score)
                    self.highscore_manager.save_highscores()
                    score_saved = True  # Set the flag to True to indicate that the score has been saved
                    print("name saved")
                else:
                    # Display 3 lines for name
                    name_place_text = self.smallfont.render('ENTER 3 LETTERS', True, WHITE)
                    name_place_rect = name_place_text.get_rect(x=380, y=330)
                    self.screen.blit(name_place_text, name_place_rect)   
                    print("enter 3 letters")                 
            
            # # Handle backspace key outside the nested event loop
            # keys = pygame.key.get_pressed()
            # if entering_name and len(player_name) > 0 and keys[pygame.K_BACKSPACE]:
            #     player_name = player_name[:-1]
  
            # Display the entered name
            if entering_name:
                name_text = self.font.render(player_name, True, WHITE)
                name_rect = name_text.get_rect(x=275, y=240)
                self.screen.blit(name_text, name_rect)

            self.screen.blit(menu_button.image, menu_button.rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.screen.blit(save_button.image, save_button.rect)

            self.clock.tick(FPS)
            pygame.display.update()