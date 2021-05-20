from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.score = 0

    def set_name(self):
        self.name = input("What's your name?")
        print(self.name)

    def choosing_gesture(self):
        print("Choose a gesture:")
        gesture_index = 0
        for gesture in self.list_of_gestures :
            print(f'Press {gesture_index} for {gesture}' )
            gesture_index += 1
        user_input = int(input("Enter here:"))
        self.gesture_chosen = self.list_of_gestures[user_input]
        print(self.gesture_chosen)



