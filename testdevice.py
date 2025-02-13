
def test_create_device():
    from device import device_data, device_id_counter, create_device
    device_data.clear()
    device_id_counter = 0

    d = create_device("Thermostat")
    assert d.type == "Thermostat"
    assert d.id == "1"
    assert device_data["1"] == d

def test_get_device():
    from device import device_data, device_id_counter, create_device, get_device
    device_data.clear()
    device_id_counter = 0

    d = create_device("Humidifier")
    fetched = get_device(d.id)
    assert fetched == d

def test_update_device():
    from device import device_data, device_id_counter, create_device, update_device
    device_data.clear()
    device_id_counter = 0

    d = create_device("OldType")
    updated = update_device(d.id, "NewType")
    assert updated is not None
    assert updated.type == "NewType"

def test_delete_device():
    from device import device_data, device_id_counter, create_device, get_device, delete_device
    device_data.clear()
    device_id_counter = 0

    d = create_device("Something")
    device_id = d.id
    assert get_device(device_id) is not None

    # Delete device
    result = delete_device(device_id)
    assert result is True
    # Confirm device is gone
    assert get_device(device_id) is None

    # Deleting again should fail
    result2 = delete_device(device_id)
    assert result2 is False