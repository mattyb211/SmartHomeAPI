# test_device.py

def test_create_device():
    from device import device_data, device_id_counter, create_device
    device_data.clear()
    device_id_counter = 0

    result = create_device("Thermostat")
    assert "success" in result
    assert result["success"] is True

    data = result["data"]
    assert data["type"] == "Thermostat"
    assert data["id"] == "1"
    assert "1" in device_data

def test_create_device_invalid():
    from device import device_data, device_id_counter, create_device
    device_data.clear()
    device_id_counter = 0

    # Attempt empty device type
    result = create_device("")
    assert "error" in result
    assert "cannot be empty" in result["error"].lower()

def test_get_device():
    from device import device_data, device_id_counter, create_device, get_device
    device_data.clear()
    device_id_counter = 0

    create_result = create_device("Humidifier")
    dev_id = create_result["data"]["id"]

    fetched = get_device(dev_id)
    assert "success" in fetched
    assert fetched["success"] is True

    data = fetched["data"]
    assert data["id"] == dev_id
    assert data["type"] == "Humidifier"

def test_get_device_nonexistent():
    from device import device_data, device_id_counter, get_device
    device_data.clear()
    device_id_counter = 0

    result = get_device("999")
    assert "error" in result
    assert "not found" in result["error"].lower()

def test_update_device():
    from device import device_data, device_id_counter, create_device, update_device
    device_data.clear()
    device_id_counter = 0

    create_result = create_device("OldType")
    dev_id = create_result["data"]["id"]

    update_result = update_device(dev_id, "NewType")
    assert "success" in update_result
    assert update_result["success"] is True

    data = update_result["data"]
    assert data["type"] == "NewType"

def test_update_device_invalid():
    from device import device_data, device_id_counter, create_device, update_device
    device_data.clear()
    device_id_counter = 0

    create_result = create_device("InitialType")
    dev_id = create_result["data"]["id"]

    # Attempt update to empty
    result = update_device(dev_id, "")
    assert "error" in result
    assert "cannot be empty" in result["error"].lower()

def test_delete_device():
    from device import device_data, device_id_counter, create_device, get_device, delete_device
    device_data.clear()
    device_id_counter = 0

    create_result = create_device("Something")
    dev_id = create_result["data"]["id"]
    assert "success" in create_result

    # Confirm device is present
    get_result = get_device(dev_id)
    assert "success" in get_result

    # Delete device
    result = delete_device(dev_id)
    assert "success" in result
    assert result["success"] is True

    # Confirm device is gone
    get_result2 = get_device(dev_id)
    assert "error" in get_result2
    assert "not found" in get_result2["error"].lower()

    # Deleting again
    result2 = delete_device(dev_id)
    assert "error" in result2
    assert "not found" in result2["error"].lower()


    