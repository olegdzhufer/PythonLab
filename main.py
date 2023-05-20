from model.CarChair import CarChair
from model.DentalChair import DentalChair
from model.FeedingChair import FeedingChair
from model.OfficeChair import OfficeChair
from manager.ChairManager import ChairManager

if __name__ == "__main__":
    chair_manager = ChairManager()
chair_manager.add_chair(OfficeChair(90, "skin", "metal", 100, "Oleh"))
chair_manager.add_chair(OfficeChair(100, "skin", "plastic", 110, "Ihor"))
chair_manager.add_chair(FeedingChair(50, 70, 2, "wood", 90, "Oleksiy"))
chair_manager.add_chair(FeedingChair(45, 70, 3, "metal", 60, "Andriy"))
chair_manager.add_chair(CarChair(50, True, "skin", 150, "Ivan"))
chair_manager.add_chair(CarChair(60, False, "flock", 160, "Maks"))
chair_manager.add_chair(DentalChair(170, "velor", 170, "Ostap"))
chair_manager.add_chair(DentalChair(165, "imitation leather", 180, "Danylo"))

for chair in chair_manager.chairs:
    print(chair)

print("\nFILTERED BY MAX_WEIGHT")

filtered_chairs = chair_manager.find_chair_which_max_weight_more_than(120)
for chair in filtered_chairs:
    print(chair)

print("\nFILTERED BY NAME")

filtered_chairs = chair_manager.find_chair_by_name("Oleh")
for chair in filtered_chairs:
    print(chair)

