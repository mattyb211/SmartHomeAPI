def test_create_room():
    from room import room_data, room_id_counter, create_room
    room_data.clear()
    room_id_counter = 0

    r = create_room("Living Room")
    assert r.name == "Living Room"
    assert r.id == "1"
    assert room_data[r.id] == r

def test_get_room():
    from room import room_data, room_id_counter, create_room, get_room
    room_data.clear()
    room_id_counter = 0

    new_room = create_room("Kitchen")
    fetched = get_room(new_room.id)
    assert fetched == new_room

def test_update_room():
    from room import room_data, room_id_counter, create_room, update_room
    room_data.clear()
    room_id_counter = 0

    r = create_room("Study")
    updated = update_room(r.id, "Office")
    assert updated is not None
    assert updated.name == "Office"

def test_delete_room():
    from room import room_data, room_id_counter, create_room, delete_room, get_room
    room_data.clear()
    room_id_counter = 0

    r = create_room("Bathroom")
    room_id = r.id
    assert get_room(room_id) is not None

    result = delete_room(room_id)
    assert result is True
    assert get_room(room_id) is None