class ChairManager:
    def __init__(self):
        self.chairs = []

    def find_chair_which_max_weight_more_than(self, kilo):
        """
        Функція знаходить крісло з вагою яка більша ніж задано
        :param kilo: int
        :return: ChairManager
        """
        return [chair for chair in self.chairs if chair.max_weight > kilo]

    def find_chair_by_name(self, name):
        return [chair for chair in self.chairs if chair.owner == name]

    def add_chair(self, *chairs):
        self.chairs.extend(chairs)
