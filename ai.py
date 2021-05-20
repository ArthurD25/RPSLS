import random
from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()
        self.score = 0

    def set_name(self):
        self.name = "Computer"
        print(self.name)

    def choosing_gesture(self):
        gestures_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.gesture_chosen = random.choice(gestures_list)
        print(self.gesture_chosen)


