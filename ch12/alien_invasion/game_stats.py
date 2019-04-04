highscorefile = 'highscore.txt'

class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start Alien Invasion in inactive mode.
        self.game_active = False
        #Look for highscore.txt.  if it exists, load it as high score,
        #   otherwise set it to 0
        try:
            with open(highscorefile) as f_obj:
                self.high_score = int(f_obj.read())
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """Iniitialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
