house_data = {}
house_id_counter = 0

class House:
    def __init__(self, house_id, name):
        self.id = house_id
        self.name = name
        self.rooms = []  

def create_house(name):
    # Basic validation
    if not name or name.strip() == "":
        return {"error": "House name cannot be empty."}

    global house_id_counter
    house_id_counter += 1
    h_id = str(house_id_counter)
    new_house = House(h_id, name)
    house_data[h_id] = new_house

    return {
        "success": True,
        "data": {
            "id": new_house.id,
            "name": new_house.name,
            "rooms": []  
        }
    }

def get_house(house_id):
    if house_id not in house_data:
        return {"error": f"House with ID {house_id} not found."}

    h = house_data[house_id]
    return {
        "success": True,
        "data": {
            "id": h.id,
            "name": h.name
            
        }
    }

def update_house(house_id, new_name):
    if house_id not in house_data:
        return {"error": f"Cannot update: House with ID {house_id} not found."}
    
    if not new_name or new_name.strip() == "":
        return {"error": "House name cannot be empty."}

    h = house_data[house_id]
    h.name = new_name

    return {
        "success": True,
        "data": {
            "id": h.id,
            "name": h.name
        }
    }

def delete_house(house_id):
    if house_id not in house_data:
        return {"error": f"Cannot delete: House with ID {house_id} not found."}

    del house_data[house_id]
    return {"success": True}

