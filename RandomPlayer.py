from random import randint
from Player import Player

class RandomPlayer(Player):

    # Um jogador precisa implementar estes dois metodos: 

    def name(self):
        return "Random"

    def move(self, player_code, board):
        return randint(0, 6)
