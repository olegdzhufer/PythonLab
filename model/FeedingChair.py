from model.Chair import Chair


class FeedingChair(Chair):

    def __init__(self, min_height, max_height, age_designed_for, material, max_weight, owner):
        self.min_height = min_height
        self.max_height = max_height
        self.age_designed_for = age_designed_for
        super().__init__(material, max_weight, owner)
        self.material = material
        self.max_weight = max_weight
        self.owner = owner

    def __repr__(self):
        parent_repr = super().__repr__()
        return parent_repr + f"{self.min_height}, {self.max_height}, {self.age_designed_for}"

    def adjust_position(height):
        max_height = 100

        while height < max_height:
            height += 1

        return height
