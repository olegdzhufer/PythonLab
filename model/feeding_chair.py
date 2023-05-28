from typing import Final
from model.chair import Chair


class FeedingChair(Chair):
    """
        A class representing a feeding chair, inheriting from the Chair class.

        Attributes:
            min_height (float): The minimum height of the chair.
            max_height (float): The maximum height of the chair.
            age_designed_for (str): The age group the chair is designed for.
            material (str): The material of the chair.
            max_weight (int): The maximum weight capacity of the chair.
            owner (str): The owner of the chair.

        Methods:
            __init__(min_height, max_height, age_designed_for, material, max_weight, owner):
                Initializes a FeedingChair object with the specified attributes.
            __repr__():
                Returns a string representation of the FeedingChair object.
            adjust_position(height):
                Adjusts the position of the chair to the desired height.

        """
    POSITION_OFFSET: Final[int] = 100

    def __init__(self, min_height, max_height, age_designed_for, material, max_weight, owner):
        self.min_height = min_height
        self.max_height = max_height
        self.age_designed_for = age_designed_for
        super().__init__(material, max_weight, owner)
        self.material = material
        self.max_weight = max_weight
        self.owner = owner

    design_chair_set = {"Simple", "Contemporary"}

    def __repr__(self):
        parent_repr = super().__repr__()
        return parent_repr + f"{self.min_height}, {self.max_height}, {self.age_designed_for}"

    def adjust_position(self, height):
        """
                Adjusts the position of the chair to the desired height.

                Parameters:
                    height (float): The current height of the chair.

                Returns:
                    float: The adjusted height of the chair.

                """
        height += self.POSITION_OFFSET
        return height
