from manager.set_manager import SetManager
from model.car_chair import CarChair
from model.chair import ChairException
from model.dental_chair import DentalChair
from model.feeding_chair import FeedingChair
from model.office_chair import OfficeChair
from manager.chair_manager import ChairManager

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

srd = DentalChair(190, "velor", 170, "Ostap")
srd.adjust_position(200)

filtered_chairs = chair_manager.find_chair_which_max_weight_more_than(120)
for chair in filtered_chairs:
    print(chair)

print("\nFILTERED BY NAME")

filtered_chairs = chair_manager.find_chair_by_name("Oleh")
for chair in filtered_chairs:
    print(chair)

print("\nlist_comprehension")

print(chair_manager.get_increase_height())

print("\nenumerate")
print(chair_manager.get_list_enumerated())

print("\nzip")
print(chair_manager.get_zipping())

print("\nCondition dictionary")
print(chair_manager.get_all_any(100))

print("\nget_dictionary")

chair_manager1 = CarChair(12, True, "saddd", 123, "asd")
print(chair_manager1.get_dict_comprehension(bool))

sm = SetManager(chair_manager)
print(len(sm))

sm = SetManager(chair_manager)
for item in sm:
    print(item)
