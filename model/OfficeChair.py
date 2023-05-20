from model.Chair import Chair


class OfficeChair(Chair):
    def __init__(self, back_angle, material_upholstary, material, max_weight, owner):
        self.back_angle = back_angle
        self.material_upholstary = material_upholstary
        super().__init__(material, max_weight, owner)
        self.material = material
        self.max_weight = max_weight
        self.owner = owner

    def __repr__(self):
        return f"{super().__repr__()}, {self.back_angle, self.material_upholstary}"

    def adjust_position(self, angle):
        angle += 1
        return angle



