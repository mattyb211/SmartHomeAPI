from house import create_house, get_house, house_data, house_id_counter

def test_create_house():
    from house import house_data, house_id_counter, create_house
    house_data.clear()
    house_id_counter = 0

    h = create_house("My House")
    assert h.name == "My House"
    assert h.id == "1"


def test_get_house():
    from house import house_data, house_id_counter, create_house, get_house
    house_data.clear()
    house_id_counter = 0

    h = create_house("Test House")
    fetched = get_house(h.id)
    assert fetched == h
