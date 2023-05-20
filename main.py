class Chair:
    instance = None

    def __init__(self, material='tree', maxWeight=123, owner='Ihor'):
        self.material = material
        self.maxWeight = maxWeight
        self.owner = owner

    def __str__(self):
        return f"{self.material}, {self.maxWeight}, {self.owner}"

    def occupy(self, owner):
        if self.is_occupied() is True:
            return
        self.owner = owner

    def is_occupied(self):
        return self.owner is not None

    def release(self):
        self.owner = None

    @staticmethod
    def get_instance():
        if not Chair.instance:
            Chair.instance = Chair()
        return Chair.instance

chairs = [Chair('skin', 123, 'Oleh'), Chair(),
          Chair(), Chair.get_instance()]

for chair in chairs:
    print(chair)