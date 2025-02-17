room_data = {}
room_id_counter = 0

class Room:
    def __init__(self, room_id, name):
        self.id = room_id
        self.name = name
        self.devices = []  

def create_room(name):
   
    if not name or name.strip() == "":
        return {"error": "Room name cannot be empty."}

    global room_id_counter
    room_id_counter += 1
    r_id = str(room_id_counter)
    new_room = Room(r_id, name)
    room_data[r_id] = new_room

    return {
        "success": True,
        "data": {
            "id": new_room.id,
            "name": new_room.name,
            "devices": []
        }
    }

def get_room(room_id):
    if room_id not in room_data:
        return {"error": f"Room with ID {room_id} not found."}

    r = room_data[room_id]
    return {
        "success": True,
        "data": {
            "id": r.id,
            "name": r.name,
           
        }
    }

def update_room(room_id, new_name):
    if room_id not in room_data:
        return {"error": f"Cannot update: Room with ID {room_id} not found."}

    if not new_name or new_name.strip() == "":
        return {"error": "Room name cannot be empty."}

    r = room_data[room_id]
    r.name = new_name
    return {
        "success": True,
        "data": {
            "id": r.id,
            "name": r.name
        }
    }

def delete_room(room_id):
    if room_id not in room_data:
        return {"error": f"Cannot delete: Room with ID {room_id} not found."}

    del room_data[room_id]
    return {"success": True}