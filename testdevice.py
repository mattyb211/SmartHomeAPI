from device import create_device, get_device, device_data, device_id_counter

def test_create_device():
    from device import device_data, device_id_counter, create_device
    device_data.clear()
    device_id_counter = 0

    d = create_device("Temperature")
    assert d.type == "Temperature"
    assert d.id == "1"


def test_get_device():
    from device import device_data, device_id_counter, create_device, get_device
    device_data.clear()
    device_id_counter = 0

    d = create_device("Humidity")
    fetched = get_device(d.id)
    assert fetched == d