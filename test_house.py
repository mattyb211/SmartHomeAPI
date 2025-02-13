def test_create_house():
    from house import house_data, house_id_counter, create_house
    house_data.clear()
    house_id_counter = 0

    h = create_house("My House")
    assert h.name == "My House"
    assert h.id == "1"
    assert house_data[h.id] == h

def test_get_house():
    from house import house_data, house_id_counter, create_house, get_house
    house_data.clear()
    house_id_counter = 0

    new_house = create_house("Test House")
    fetched = get_house(new_house.id)
    assert fetched == new_house

def test_update_house():
    from house import house_data, house_id_counter, create_house, update_house
    house_data.clear()
    house_id_counter = 0

    h = create_house("Old House")
    updated = update_house(h.id, "New House")
    assert updated is not None
    assert updated.name == "New House"

def test_delete_house():
    from house import house_data, house_id_counter, create_house, delete_house, get_house
    house_data.clear()
    house_id_counter = 0

    h = create_house("His house")
    house_id = h.id
    assert get_house(house_id) is not None

    result = delete_house(house_id)
    assert result is True
    assert get_house(house_id) is None