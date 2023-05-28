from manager.chair_manager import ChairManager


class SetManager:
    manager_obj = ChairManager()

    def __init__(self, manager_obj):
        self.values = []
        self.manager_obj = manager_obj

    values = [item.design_chair_set for item in manager_obj]

    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return sum(len(item.design_chair_set)
                   for item in self.manager_obj)


        # lenght = 0
        # for item in self.manager_obj:
        #     lenght += len(item.design_chair_set)
        # return lenght











        
        