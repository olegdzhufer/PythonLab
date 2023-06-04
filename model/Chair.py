"""Module that contains abstract chair class"""
from abc import ABC, abstractmethod

class Chair(ABC):
    """
       Abstract base class representing a chair.

       Attributes:
           material (str): The material of the chair.
           max_weight (int): The maximum weight capacity of the chair.
           owner (str): The owner of the chair.

       Methods:
           __init__(material, max_weight, owner):
               Initializes a Chair object with the specified attributes.
           __repr__():
               Returns a string representation of the Chair object.
           adjust_position(value):
               Abstract method for adjusting the position of the chair.

       """

    def __init__(self, material, max_weight, owner):
        self.material = material
        self.max_weight = max_weight
        self.owner = owner
        self.design_chair_set = set()

    def __repr__(self):
        return f"{self.material}, {self.max_weight}, {self.owner}"

    @abstractmethod
    def adjust_position(self, value):
        """
        Abstract method for adjusting the position of the chair.

        Parameters:
            value: The value used for adjusting the position of the chair.
            """
        pass

    def get_dict_comprehension(self, data_type):
        field_dict = {}
        for attr_name, attr_value in self.__dict__.items():
            field_dict[attr_name] = isinstance(attr_value, data_type)
        return field_dict

    def __iter__(self):
        return iter(self.design_chair_set)
