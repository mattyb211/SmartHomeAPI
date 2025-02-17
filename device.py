device_data = {}
device_id_counter = 0

class Device:
    def __init__(self, device_id, device_type):
        self.id = device_id
        self.type = device_type

def create_device(device_type):
    # Validate device_type
    if not device_type or device_type.strip() == "":
        return {"error": "Device type cannot be empty."}

    global device_id_counter
    device_id_counter += 1
    d_id = str(device_id_counter)
    new_device = Device(d_id, device_type)
    device_data[d_id] = new_device

    return {
        "success": True,
        "data": {
            "id": new_device.id,
            "type": new_device.type
        }
    }

def get_device(device_id):
    if device_id not in device_data:
        return {"error": f"Device with ID {device_id} not found."}

    d = device_data[device_id]
    return {
        "success": True,
        "data": {
            "id": d.id,
            "type": d.type
        }
    }

def update_device(device_id, new_type):
    if device_id not in device_data:
        return {"error": f"Cannot update: Device with ID {device_id} not found."}

    if not new_type or new_type.strip() == "":
        return {"error": "Device type cannot be empty."}

    d = device_data[device_id]
    d.type = new_type

    return {
        "success": True,
        "data": {
            "id": d.id,
            "type": d.type
        }
    }

def delete_device(device_id):
    if device_id not in device_data:
        return {"error": f"Cannot delete: Device with ID {device_id} not found."}

    del device_data[device_id]
    return {"success": True}