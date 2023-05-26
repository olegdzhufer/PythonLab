from abc import ABC, abstractmethod


class Chair(ABC):

    def __init__(self, material, max_weight, owner):
        self.material = material
        self.max_weight = max_weight
        self.owner = owner

    def __repr__(self):
        return f"{self.material}, {self.max_weight}, {self.owner}"

    @abstractmethod
    def adjust_position(self, value):
        pass
