house_data = {}
house_id_counter = 0

class House:
    def __init__(self, house_id, name):
        self.id = house_id
        self.name = name
        self.rooms = []  

# Stub functions

def create_house(name):
    global house_id_counter
    house_id_counter += 1
    h_id = str(house_id_counter)
    new_house = House(h_id, name)
    house_data[h_id] = new_house
    return new_house

def get_house(house_id):
    return house_data.get(house_id, None)

def update_house(house_id, new_name):
    h = house_data.get(house_id)
    if h is not None:
        h.name = new_name
        return h
    return None

def delete_house(house_id):
    if house_id in house_data:
        del house_data[house_id]
        return True
    return False

