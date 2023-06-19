"""Module that contains class of dental chair"""
from typing import Final



from decorator.logging import logged
from model.chair import Chair
from exception.max_of_angle_chair import MaxOfAngleChair


class DentalChair(Chair):
    """
       A class representing a dental chair, inheriting from the Chair class.

       Attributes:
           angle_chair (float): The angle of the chair.
           material (str): The material of the chair.
           max_weight (int): The maximum weight capacity of the chair.
           owner (str): The owner of the chair.

       Methods:
           __init__(angle_chair, material, max_weight, owner):
               Initializes a DentalChair object with the specified attributes.
           __repr__():
               Returns a string representation of the DentalChair object.
           adjust_position(angle_chair):
               Adjusts the position of the chair by increasing the angle.

       """
    POSITION_OFFSET: Final[int] = 11

    def __init__(self, angle_chair, material, max_weight, owner,
                 design_chair_set=None):
        if design_chair_set is None:
            design_chair_set = {"Modern", "Plastic"}
        self.angle_chair = angle_chair
        super().__init__(material, max_weight, owner)
        self.material = material
        self.max_weight = max_weight
        self.owner = owner
        self.design_chair_set = design_chair_set

    def __repr__(self):
        parent_repr = super().__repr__()
        return parent_repr + f"{self.angle_chair}"

    @logged(MaxOfAngleChair, mode="file.txt")
    def adjust_position(self, angle_chair):
        """
        Adjusts the position of the chair by increasing the angle.

               Parameters:
                   angle_chair (float): The current angle of the chair.

               Returns:
                   float: The adjusted angle of the chair.
        """
        if self.angle_chair > 180:
            raise MaxOfAngleChair("Angle already max")
        else:
            angle_chair += self.POSITION_OFFSET
        return angle_chair
