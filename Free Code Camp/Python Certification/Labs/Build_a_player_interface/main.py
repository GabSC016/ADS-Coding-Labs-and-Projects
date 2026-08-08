from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]


    def make_move(self):
        new_move = random.choice(self.moves)

        updated_position = (new_move[0] + self.position[0],new_move[1] + self.position[1])

        self.position = updated_position
        self.path.append(updated_position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

# Classe filha
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0,1),(0,-1), (-1,0),(1,0)]

    def level_up(self):
        diagonal_moves = [(1,1), (-1,-1),(-1,1), (1,-1)]
        for move in diagonal_moves:
            self.moves.append(move)