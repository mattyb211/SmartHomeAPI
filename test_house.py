# test_house.py

def test_create_house():
    from house import house_data, house_id_counter, create_house
    house_data.clear()
    house_id_counter = 0

    result = create_house("My House")
    assert "success" in result
    assert result["success"] is True

    data = result["data"]
    assert data["name"] == "My House"
    assert data["id"] == "1"
    # Confirm in house_data
    assert "1" in house_data

def test_create_house_invalid():
    from house import house_data, house_id_counter, create_house
    house_data.clear()
    house_id_counter = 0

    # Attempt empty house name
    result = create_house("")
    assert "error" in result
    assert "cannot be empty" in result["error"].lower()

def test_get_house():
    from house import house_data, house_id_counter, create_house, get_house
    house_data.clear()
    house_id_counter = 0

    create_result = create_house("Test House")
    house_id = create_result["data"]["id"]

    fetched = get_house(house_id)
    assert "success" in fetched
    assert fetched["success"] is True

    data = fetched["data"]
    assert data["id"] == house_id
    assert data["name"] == "Test House"

def test_get_house_nonexistent():
    from house import house_data, house_id_counter, get_house
    house_data.clear()
    house_id_counter = 0

    result = get_house("999")
    assert "error" in result
    assert "not found" in result["error"].lower()

def test_update_house():
    from house import house_data, house_id_counter, create_house, update_house
    house_data.clear()
    house_id_counter = 0

    create_result = create_house("Old House")
    house_id = create_result["data"]["id"]

    update_result = update_house(house_id, "New House")
    assert "success" in update_result
    assert update_result["success"] is True

    data = update_result["data"]
    assert data["name"] == "New House"

def test_update_house_invalid():
    from house import house_data, house_id_counter, create_house, update_house
    house_data.clear()
    house_id_counter = 0

    # Create a house
    create_result = create_house("Some House")
    h_id = create_result["data"]["id"]

    # Try update with empty name
    result = update_house(h_id, "")
    assert "error" in result
    assert "cannot be empty" in result["error"].lower()

def test_delete_house():
    from house import house_data, house_id_counter, create_house, delete_house, get_house
    house_data.clear()
    house_id_counter = 0

    create_result = create_house("His House")
    h_id = create_result["data"]["id"]

    # Confirm house is present
    fetched = get_house(h_id)
    assert "success" in fetched

    # Delete
    delete_result = delete_house(h_id)
    assert "success" in delete_result
    assert delete_result["success"] is True

    # Now not found
    fetched2 = get_house(h_id)
    assert "error" in fetched2
    assert "not found" in fetched2["error"].lower()