class ChairManager:
    """
    A class that manages a list of chairs.

    Methods:
       find_chair_which_max_weight_more_than(max_weight):
           Find a chair with a weight greater than the given maximum weight.
       find_chair_by_name(name):
           Find a chair owned by the given name.
       add_chair(*chairs):
           Add a list of chairs to the existing list.
       get_increase_height():
           Get the adjusted height of all chairs by increasing their positions.
       get_list_enumerated():
           Print the enumerated list of chairs.
       get_zipping():
           Get the zipped records of chairs with their adjusted heights.
       get_all_any(current_weight):
           Check if all or any chairs have a maximum weight greater
           than or equal to the given current weight.

    Attributes:
        chairs (list): A list of chairs managed by the ChairManager.
    """

    def __init__(self):
        """
        Initialize an instance of ChairManager.
        """
        self.chairs = []
        self.current_item = 0
        self.design_chair_set = set()

    def find_chair_which_max_weight_more_than(self, max_weight: int) -> list:
        """
        Find a chair with a weight greater than the given maximum weight.

        Parameters:
            max_weight (int): The maximum weight to compare against.

        Returns:
            list: A list of chairs with a weight greater than the given maximum weight.
        """
        return [chair for chair in self.chairs if chair.max_weight > max_weight]

    def find_chair_by_name(self, name: str) -> list:
        """
        Find a chair owned by the given name.

        Parameters:
            name (str): The name of the owner.

        Returns:
            list: A list of chairs owned by the given name.
        """
        return [chair for chair in self.chairs if chair.owner == name]

    def add_chair(self, *chairs):
        """
        Add a list of chairs to the existing list.

        Parameters:
            *chairs (list): A list of chairs to be added.

        Returns:
            None
        """
        self.chairs.extend(chairs)

    def __len__(self):
        return len(self.chairs)

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError
        if 0 <= item < len(self.chairs):
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
        """
        Get the adjusted height of all chairs by increasing their positions.

        Returns:
            list: The adjusted height of all chairs.
        """
        return [chair.adjust_position(2) for chair in self.chairs]

    def get_list_enumerated(self) -> str:
        """
        Print the enumerated list of chairs.

        Returns:
            str: An empty string.
        """
        for i, j in enumerate(self.chairs):
            print("Index =>", i, "- value =>", j)
        return ""

    def get_zipping(self):
        """
        Get the zipped records of chairs with their adjusted heights.

        Returns:
            list: The zipped records of chairs.
        """
        records = [(f"Object: {chair}", f"-> result: {result}") for chair, result in
                   zip(self.chairs, self.get_increase_height())]
        return records

    def get_all_any(self, current_weight):
        """
        Check if all or any chairs have a maximum weight greater than
        or equal to the given current weight.

        Parameters:
            current_weight (int): The current weight to compare against.

        Returns:
            dict: A dictionary with keys 'all' and 'any' indicating
            if all or any chairs meet the condition.
        """
        result = [chair.max_weight >= current_weight for chair in self.chairs]
        return {"all": all(result), "any": any(result)}
