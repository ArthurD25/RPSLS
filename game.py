from player import Player
from human import Human
from ai import AI
class Game:
    def __init__(self):
        Human()
        AI()

    def run_game(self):
        self.display_welcome()
        self.choose_player_two()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to RPSLS! The best one on one game ever!")

    def choose_player_two(self):
        player_two =input("Would you like to play single player or multiplayer?")
        if player_two == 'single player':
            return AI()
        elif player_two == "multiplayer":
            return Human()
        else:
            print("That's not a valid response please try again")

    def player_one_choose(self):
        Human.choosing_gesture()

    def player_two_choose(self):
        if 

