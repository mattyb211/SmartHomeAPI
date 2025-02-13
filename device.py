device_data = {}
device_id_counter = 0

class Device:
    def __init__(self, device_id, device_type):
        self.id = device_id
        self.type = device_type

# Stub functions.

def create_device(device_type):
    global device_id_counter
    device_id_counter += 1
    d_id = str(device_id_counter)
    new_device = Device(d_id, device_type)
    device_data[d_id] = new_device
    return new_device

def get_device(device_id):
    return device_data.get(device_id, None)
