import pygame

class HighscoreManager:
    """Highscore file i/o"""

    def __init__(self):
        self.highscore_file = 'highscores.txt'
        self.highscores = []
        self.load_highscores()

    def load_highscores(self):
        try:
            with open(self.highscore_file, 'r') as file:
                lines = file.readlines()
                self.highscores = [line.strip() for line in lines]
        except FileNotFoundError:
            self.highscores = []

    def save_highscores(self):
        with open(self.highscore_file, 'w') as file:
            for score in self.highscores:
                file.write(score + '\n')

    def add_highscore(self, name, score):
        name = name.upper()
        self.highscores.append(f'{name}: {score}')
        self.highscores.sort(reverse=True, key=lambda x: int(x.split(': ')[1]))
        self.highscores = self.highscores[:10]

    def get_highscores(self):
        return self.highscores

    def is_highscore(self, score):
        """Check if a given score is within the top 10 high scores."""

        if len(self.highscores) < 10:
            return True  # If there are less than 10 scores, any score is a high score
        else:
            # Compare the score with the 10th highest score (index 9)
            tenth_highscore = int(self.highscores[9].split(': ')[1])
            return score > tenth_highscore
