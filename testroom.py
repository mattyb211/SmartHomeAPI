from room import create_room, get_room, room_data, room_id_counter

def test_create_room():
    from room import room_data, room_id_counter, create_room
    room_data.clear()
    room_id_counter = 0

    r = create_room("Living Room")
    assert r.name == "Living Room"
    assert r.id == "1"


def test_get_room():
    from room import room_data, room_id_counter, create_room, get_room
    room_data.clear()
    room_id_counter = 0

    r = create_room("Kitchen")
    fetched = get_room(r.id)
    assert fetched == r
