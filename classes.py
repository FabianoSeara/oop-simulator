from datetime import datetime, timedelta


class Truck:
    def __init__(self, license_plate, driver, container_number, yard_block, equipment_needed, arrival_time, service_duration, departure_time=None, plate_verified_on_exit=None):
        self.license_plate = license_plate
        self.driver = driver
        self.container_number = container_number
        self.yard_block = yard_block
        self.equipment_needed = equipment_needed
        self.arrival_time = arrival_time
        self.service_duration = service_duration
        self.departure_time = departure_time
        self.plate_verified_on_exit = plate_verified_on_exit


    def calculate_departure_time(self, arrival_time, duration_minutes):
        time_obj = datetime.strptime(arrival_time, "%H:%M")
        new_time_obj = time_obj + timedelta(minutes=duration_minutes)
        self.departure_time = new_time_obj.strftime("%H:%M")


class Equipment:
    def __init__(self, equipment_id, equipment_type, busy=False, current_truck=None):
        self.equipment_id = equipment_id
        self.equipment_type = equipment_type
        self.busy = busy
        self.current_truck = current_truck    

    def release(self):
        self.busy = False
        self.current_truck = None

    def occupy(self, truck):
        self.busy = True
        self.current_truck = truck.license_plate


class Yard:
    def __init__(self, equipment_list):
        self.equipment_list = equipment_list    
        self.waiting = []                        # Queue of Truck objects (FIFO)
        self.all_trucks = []                     # Every truck that entered the yard


    def add_truck(self, truck):
        self.all_trucks.append(truck)
        process_truck(truck, self.equipment_list)
        if truck.departure_time is None:
            self.waiting.append(truck)
            

    def release_equipment(self, equipment):
        equipment.release()
        for truck in self.waiting:
            if truck.equipment_needed == equipment.equipment_type:
                self.waiting.remove(truck)
                process_truck(truck, self.equipment_list)
                break


    def print_report(self):
        attended = 0
        total_duration = 0
        for truck in self.all_trucks:
            if truck.departure_time is not None:
                attended += 1
                total_duration += truck.service_duration

        if attended > 0:
            average = total_duration / attended
        else:
            average = 0

        waiting = len(self.waiting)
        total = len(self.all_trucks)

        print(f"Attended: {attended}")
        print(f"Waiting: {waiting}")
        print(f"Total: {total}")
        print(f"Average service time: {average:.1f} min") 


def find_available_equipment(needed_type, equipment_list):
    for item in equipment_list:
        if item.equipment_type == needed_type and not item.busy:
            return item
    return None


def process_truck(truck, equipment_list):
    # 1. Searches for the type of equipment the truck requires
    equipment = find_available_equipment(truck.equipment_needed, equipment_list)

    # 2. If found, load it and calculate the departure
    if equipment:
        equipment.occupy(truck)
        truck.calculate_departure_time(truck.arrival_time, truck.service_duration)
    # 3. If not found, provide notification that it is still waiting
    else:
        print(f"Truck {truck.license_plate} waiting equipment ...{truck.equipment_needed} available...")
    






    
  

    




    
