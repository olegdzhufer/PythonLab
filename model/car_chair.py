from typing import Final

from model.chair import Chair


class CarChair(Chair, ):
    """A class representing a car chair, inheriting from the Chair class.

    Attributes:
        length_to_wheel (float): The length from the chair to the wheel.
        heating (bool): Indicates if the chair has heating functionality.
        material (str): The material of the chair.
        max_weight (int): The maximum weight capacity of the chair.
        owner (str): The owner of the chair.

    Methods:
        __init__(length_to_wheel, heating, material, max_weight, owner):
            Initializes a CarChair object with the specified attributes.
        __repr__():
            Returns a string representation of the CarChair object.
        adjust_position(length_to_wheel):
            Adjusts the position of the chair by increasing the length to the wheel.
"""
    POSITION_OFFSET: Final[int] = 5

    def __init__(self, length_to_wheel, heating, material, max_weight, owner, design_chair_set={"Classic", "Vintage"}):
        self.length_to_wheel = length_to_wheel
        self.heating = heating
        super().__init__(material, max_weight, owner)
        self.material = material
        self.max_weight = max_weight
        self.owner = owner
        self.design_chair_set = design_chair_set

    def __repr__(self):
        parent_repr = super().__repr__()
        return parent_repr + f"{self.length_to_wheel}, {self.heating}"

    def adjust_position(self, length_to_wheel):
        """
        Adjusts the position of the chair by increasing the length to the wheel.

        Parameters:
            length_to_wheel (float): The current length from the chair to the wheel.

        Returns:
            float: The adjusted length to the wheel.
        """
        length_to_wheel += self.POSITION_OFFSET
        return length_to_wheel
