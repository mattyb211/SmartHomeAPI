# test_room.py

def test_create_room():
    from room import room_data, room_id_counter, create_room
    room_data.clear()
    room_id_counter = 0

    result = create_room("Living Room")
    assert "success" in result
    assert result["success"] is True

    data = result["data"]
    assert data["name"] == "Living Room"
    assert data["id"] == "1"
    assert "1" in room_data

def test_create_room_invalid():
    from room import room_data, room_id_counter, create_room
    room_data.clear()
    room_id_counter = 0

    # Attempt empty room name
    result = create_room("")
    assert "error" in result
    assert "cannot be empty" in result["error"].lower()

def test_get_room():
    from room import room_data, room_id_counter, create_room, get_room
    room_data.clear()
    room_id_counter = 0

    create_result = create_room("Kitchen")
    r_id = create_result["data"]["id"]

    fetched = get_room(r_id)
    assert "success" in fetched
    assert fetched["success"] is True

    data = fetched["data"]
    assert data["id"] == r_id
    assert data["name"] == "Kitchen"

def test_get_room_nonexistent():
    from room import room_data, room_id_counter, get_room
    room_data.clear()
    room_id_counter = 0

    result = get_room("999")
    assert "error" in result
    assert "not found" in result["error"].lower()

def test_update_room():
    from room import room_data, room_id_counter, create_room, update_room
    room_data.clear()
    room_id_counter = 0

    create_result = create_room("Study")
    r_id = create_result["data"]["id"]

    update_result = update_room(r_id, "Office")
    assert "success" in update_result
    assert update_result["success"] is True

    data = update_result["data"]
    assert data["name"] == "Office"

def test_update_room_invalid():
    from room import room_data, room_id_counter, create_room, update_room
    room_data.clear()
    room_id_counter = 0

    create_result = create_room("Workshop")
    r_id = create_result["data"]["id"]

    result = update_room(r_id, "")
    assert "error" in result
    assert "cannot be empty" in result["error"].lower()

def test_delete_room():
    from room import room_data, room_id_counter, create_room, delete_room, get_room
    room_data.clear()
    room_id_counter = 0

    create_result = create_room("Bathroom")
    r_id = create_result["data"]["id"]

    # Confirm room is present
    get_result = get_room(r_id)
    assert "success" in get_result

    # Delete
    del_result = delete_room(r_id)
    assert "success" in del_result
    assert del_result["success"] is True

    # Now should be gone
    get_result2 = get_room(r_id)
    assert "error" in get_result2
    assert "not found" in get_result2["error"].lower()