from typing import Final
from model.chair import Chair


class OfficeChair(Chair):
    """
        A class representing an office chair, inheriting from the Chair class.

        Attributes:
            back_angle (float): The angle of the chair back.
            material_upholstery (str): The material used for upholstery.
            material (str): The material of the chair.
            max_weight (int): The maximum weight capacity of the chair.
            owner (str): The owner of the chair.

        Methods:
            __init__(back_angle, material_upholstery, material, max_weight, owner):
                Initializes an OfficeChair object with the specified attributes.
            __repr__():
                Returns a string representation of the OfficeChair object.
            adjust_position(angle):
                Adjusts the position of the chair by increasing the angle.

        """
    POSITION_OFFSET: Final[int] = 8

    def __init__(self, back_angle, material_upholstary, material, max_weight, owner,
                 design_chair_set={"Elegant", "Industrial"}):
        self.back_angle = back_angle
        self.material_upholstary = material_upholstary
        super().__init__(material, max_weight, owner)
        self.material = material
        self.max_weight = max_weight
        self.owner = owner
        self.design_chair_set = design_chair_set

    def __repr__(self):
        return f"{super().__repr__()}, {self.back_angle, self.material_upholstary}"

    def adjust_position(self, angle):
        """
               Adjusts the position of the chair by increasing the angle.

               Parameters:
                   angle (float): The current angle of the chair.

               Returns:
                   float: The adjusted angle of the chair.

               """
        angle += self.POSITION_OFFSET
        return angle
