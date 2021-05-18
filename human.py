from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = input("What's your name?")
        print(self.name)

    def choosing_gesture(self):
        print("Choose a gesture:")
        gesture_index = 0
        for gesture in self.list_of_gestures :
            input(f'Press {gesture_index} for {gesture}' )
            gesture_index += 1



