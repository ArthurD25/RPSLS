from player import Player
from human import Human
from ai import AI
class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
        self.display_welcome()
        self.choose_player_two()
     #   self.player_one_choose()
     #   self.player_two_choose()
        self.battle()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to RPSLS! The best one on one game ever!")

    def choose_player_two(self):
        response = input("Would you like to play single player or multiplayer?")
        if response == "single player":
            self.player_two = AI()
        elif response == "multiplayer":
            self.player_two = Human()
        else:
            print("That's not a valid response please try again")

   # def player_one_choose(self):
     #   self.player_one.choosing_gesture()

   # def player_two_choose(self):
     #   self.player_two.choosing_gesture()

    def battle(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choosing_gesture()
            self.player_two.choosing_gesture()
            if self.player_one.gesture_chosen == "Rock":
                if self.player_two.gesture_chosen == "Rock":
                    print("its a tie")
                elif self.player_two.gesture_chosen == 'Paper':
                    self.player_two.score += 1
                elif self.player_two.gesture_chosen == "Scissors":
                    self.player_one.score += 1
                elif self.player_two.gesture_chosen == "Lizard":
                    self.player_one.score += 1
                elif self.player_two.gesture_chosen == "Spock":
                    self.player_two.score += 1
            if self.player_one.gesture_chosen == "Paper":
                if self.player_two.gesture_chosen == "Paper":
                    print("It's a tie!")
                elif self.player_two.gesture_chosen == "Rock":
                    self.player_one.score += 1
                elif self.player_two.gesture_chosen == "Scissors":
                    self.player_two.score += 1
                elif self.player_two.gesture_chosen == "Lizard":
                    self.player_two.score += 1
                elif self.player_two.gesture_chosen == "Spock":
                    self.player_one.score += 1
            if self.player_one.gesture_chosen == "Scissors":
                if self.player_two.gesture_chosen == "Scissors":
                    print("It's a tie")
                elif self.player_two.gesture_chosen == "Rock":
                    self.player_two.score += 1
                elif self.player_two.gesture_chosen == "Paper":
                    self.player_one.score += 1
                elif self.player_two.gesture_chosen == "Lizard":
                    self.player_one.score += 1
                elif self.player_two.gesture_chosen == "Spock":
                    self.player_two.score += 1
            if self.player_one.gesture_chosen == "Lizard":
                if self.player_two.gesture_chosen == "Lizard":
                    print("It's a tie!")
                elif self.player_two.gesture_chosen == "Rock":
                    self.player_one.score += 1
                elif self.player_two.gesture_chosen == "Paper":
                    self.player_one.score += 1
                elif self.player_two.gesture_chosen == "Scissors":
                    self.player_two.score += 1
                elif self.player_two.gesture_chosen == "Spock":
                    self.player_one.score += 1
            if self.player_one.gesture_chosen == "Spock":
                if self.player_two.gesture_chosen == "Spock":
                    print("It's a tie")
                elif self.player_two.gesture_chosen == "Rock":
                    self.player_one.score += 1
                elif self.player_two.gesture_chosen == "Paper":
                    self.player_two.score += 1
                elif self.player_two.gesture_chosen == "Scissors":
                    self.player_one.score += 1
                elif self.player_two.choosing_gesture == "Lizard":
                    self.player_two.score += 1

    def display_winner(self):
        if self.player_one.score == 2:
            print("Player one is the winner!")
        elif self.player_two.score == 2:
            print("Player 2 is the winner!")



