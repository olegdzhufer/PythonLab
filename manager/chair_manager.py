class ChairManager:
    """
    A class that manages a list of chairs.

    Methods:
       find_chair_which_max_weight_more_than(max_weight):
               find a chair with a given weight
       find_chair_by_name:
               finds a chair with a given owner
       add_chair:
               Adds a list of chairs to the existing list.

     Attributes:
        chairs (list): A list of chairs managed by the ChairManager.
    """

    def __init__(self):
        """
        Initialize an instance of ChairManager
        """
        self.chairs = []
        self.current_item = 0
        self.design_chair_set = set()

    def find_chair_which_max_weight_more_than(self, kilo: int):
        """
        find a chair with a given weight
        :param kilo (int): the max weight of chair
        :return:list:
        a list of chairs with a given weight
        """
        return [chair for chair in self.chairs if chair.max_weight > kilo]

    def find_chair_by_name(self, name: str):
        """
        finds a chair with a given owner
        :param name (str): the name of owner
        :return:list:
        a list of chairs with a given owner
        """
        return [chair for chair in self.chairs if chair.owner == name]

    def add_chair(self, *chairs):
        """
        Adds a list of chairs to the existing list.
        :param chairs(list): A list of chairs to be added.
        :return: None
        """
        self.chairs.extend(chairs)

    def __len__(self):
        return len(self.chairs)

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError
        if 0 <= item <= len(self.chairs):
            return self.chairs[item]
        else:
            raise IndexError

    def __iter__(self):
        return iter(self.chairs)

    def __next__(self):
        if self.current_item >= len(self.chairs):
            raise StopIteration
        item = self.chairs[self.current_item]
        self.current_item += 1
        return item

    def get_increase_height(self):
        return list([chair.adjust_position(2) for chair in self.chairs])

    def get_list_enumerated(self):
        for i, j in enumerate(self.chairs):
            print("Index =>", i, "- value =>", j)
        return ""

    def get_zipping(self):
        records = [(f"Object: {chair}", f"-> result: {result}") for chair, result in
                   zip(self.chairs, self.get_increase_height())]
        return records

    def get_all_any(self, current_weght):
        dict = [chair.max_weight >= current_weght for chair in self.chairs]
        return {"all": all(dict), "any": any(dict)}

