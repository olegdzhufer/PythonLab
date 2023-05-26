from model.Chair import Chair


class CarChair(Chair):

    def __init__(self, length_to_wheel, heating, material, max_weight, owner):
        self.length_to_wheel = length_to_wheel
        self.heating = heating
        super().__init__(material, max_weight, owner)
        self.material = material
        self.max_weight = max_weight
        self.owner = owner

    def __repr__(self):
        parent_repr = super().__repr__()
        return parent_repr + f"{self.length_to_wheel}, {self.heating}"

    def adjust_position(self, length_to_wheel):
        length_to_wheel += 1
        return length_to_wheel
