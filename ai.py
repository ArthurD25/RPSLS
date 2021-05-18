import random
from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = "Computer"
        print(self.name)

    def choosing_gesture(self):
        gestures_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        x = random.choice(gestures_list)
        print(x)


