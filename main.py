from classes import Truck, Equipment, Yard


def main():
# 1. Fleet: equipment 1 and 4 start busy
    fleet = [
        Equipment(1, "RTG", busy=True),
        Equipment(2, "RTG"),
        Equipment(3, "RTG"),
        Equipment(4, "RS", busy=True),
        Equipment(5, "RS"),
    ]


    # 2. yard with a fleet
    yard = Yard(fleet)


    # 3. Trucks in the same order as in the original simulator
    trucks = [
        Truck("ABC1234", "João",    "MSCU 222333-3", "A", "RTG", "08:00", 20),
        Truck("AXF 3333", "Marcos", "MSCU 123444-3", "B", "RS",  "09:00", 40),
        Truck("GHI9012", "Alfredo","YMLU 000033-7", "C", "RTG", "07:30", 15),
        Truck("JKL3456", "Jack",   "HTMU 122333-3", "D", "RS",  "13:00", 25),
        Truck("DEF5678", "Tiago",  "NXDU 222445-3", "E", "RTG", "10:00", 50),
    ]


    # 4. Each truck enters through the yard
    for truck in trucks:
        yard.add_truck(truck)


    # 5. Initial report
    yard.print_report()
    print("===========================")


    # 6. Release RTG 2(fleet[1]) Tiago is attended 
    yard.release_equipment(fleet[1])
    yard.print_report()
    print("===========================")


    # 7. Release RS 4(fleet[3]) Jack is attended
    yard.release_equipment(fleet[3])
    yard.print_report()


if __name__ == "__main__":
    main()