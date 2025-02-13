room_data = {}
room_id_counter = 0

class Room:
    def __init__(self, room_id, name):
        self.id = room_id
        self.name = name
        self.devices = []

# Stub functions.

def create_room(name):
    global room_id_counter
    room_id_counter += 1
    r_id = str(room_id_counter)
    new_room = Room(r_id, name)
    room_data[r_id] = new_room
    return new_room

def get_room(room_id):
    return room_data.get(room_id, None)

def update_room(room_id, new_name):
    r = room_data.get(room_id)
    if r is not None:
        r.name = new_name
        return r
    return None

def delete_room(room_id):
    if room_id in room_data:
        del room_data[room_id]
        return True
    return False