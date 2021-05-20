class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.list_of_gestures =["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.gesture_chosen = ""

    def choosing_gesture(self):
        print("Choose a gesture!")
        print(f'{self.list_of_gestures}')






