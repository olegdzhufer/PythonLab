from manager.chair_manager import ChairManager


class SetManager:

    def __init__(self, manager_obj):
        self.manager_obj = manager_obj
        self.values = iter([item.design_chair_set for item in self.manager_obj])

    manager_obj = ChairManager()

    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return sum(len(item.design_chair_set) for item in self.manager_obj)

    def __getitem__(self, item):
        return self.manager_obj[item].design_chair_set

    def __next__(self):
        return next(self.values)
