from model.Chair import Chair


class DentalChair(Chair):

    def __init__(self, angle_chair, material, max_weight, owner):
        self.angle_chair = angle_chair
        super().__init__(material, max_weight, owner)
        self.material = material
        self.max_weight = max_weight
        self.owner = owner

    def __repr__(self):
        parent_repr = super().__repr__()
        return parent_repr + f"{self.angle_chair}"

    def adjust_position(self, angle_chair):
        angle_chair += 1
        return angle_chair


dental_chair = DentalChair(1, "dsf", 133, "fds")
