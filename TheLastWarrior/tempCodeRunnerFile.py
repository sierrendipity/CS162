    def stats(self,score,lives):
        """stats for the game. keyword arguments: score, lives"""

        score1 = self.smallfont.render("SCORE:" + str(score), True, WHITE)
        score_rect = score1.get_rect(x=80, y=0)
        lives1 = self.smallfont.render('LIVES:' + str(lives), True, WHITE)
        lives_rect = lives1.get_rect(x=0, y=0)

        self.screen.blit(score1, score_rect)
        self.screen.blit(lives1, lives_rect)
        # self.clock.tick(FPS)
        pygame.display.update()