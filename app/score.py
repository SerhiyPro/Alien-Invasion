import json
import os


class Score:
    def __init__(self):
        self.score = 0
        self.filename = 'best_score.json'

    def get_score(self):
        if os.path.isfile(self.filename) and os.path.exists(self.filename):
            with open(self.filename) as f_obj:
                # todo load : loads
                self.score = json.load(f_obj)
                return self.score.get('scores')
        else:
            return 0

    def set_score(self, game_stats):
        """Prints the highest scores to json"""
        with open(self.filename, 'w') as f_obj:
            json.dump({'scores': game_stats.high_score}, f_obj)
