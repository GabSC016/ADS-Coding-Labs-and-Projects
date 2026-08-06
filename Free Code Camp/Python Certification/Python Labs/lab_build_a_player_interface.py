# Lab: Build a Player Interface
# Implemented an abstract Player interface using ABC, with movement tracking, random move selection, and path history. Created a concrete Pawn class that defines cardinal movements and extends its capabilities through a level_up method by adding diagonal moves.

# Imports (abc e random)

from abc import ABC, abstractmethod
import random

# Define a classe abastrata

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    # Método para sortear movimentos    

    def make_move(self):
        new_move = random.choice(self.moves)

        updated_position = (new_move[0] + self.position[0],new_move[1] + self.position[1])

        self.position = updated_position
        self.path.append(updated_position)
        return self.position
    
    # Método abstrato

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