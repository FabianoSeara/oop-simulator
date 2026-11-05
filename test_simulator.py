from classes import Truck, Equipment, Yard


fleet = [Equipment(1, "RTG", busy=True), Equipment(2, "RTG")]
yard = Yard(fleet)
t = Truck("TEST1", "X", "C1", "A", "RTG", "08:00", 20)
yard.add_truck(t)
assert t.departure_time == "08:20"     # RTG2 was free
assert len(yard.waiting) == 0


t2 = Truck("TESTE2", "Y", "C2", "B", "RTG", "09:00", 10)
yard.add_truck(t2)
assert t2.departure_time is None       # no free RTG
assert len(yard.waiting) == 1


yard.release_equipment(fleet[1])
assert t2.departure_time == "09:10"
assert len(yard.waiting) == 0
print("Ok")