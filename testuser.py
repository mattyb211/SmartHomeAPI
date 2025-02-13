def test_create_user():
    from user import user_data, user_id_counter, create_user
    user_data.clear()
    user_id_counter = 0

    u = create_user("Mateo", "Mateo@bu.com")
    assert u.username == "Mateo"
    assert u.email == "Mateo@bu.com"
    assert u.id == "1"
    assert user_data[u.id] == u

def test_get_user():
    from user import user_data, user_id_counter, create_user, get_user
    user_data.clear()
    user_id_counter = 0

    created = create_user("Noah", "Noah@bu.com")
    fetched = get_user(created.id)
    assert fetched == created

def test_update_user():
    from user import user_data, user_id_counter, create_user, update_user
    user_data.clear()
    user_id_counter = 0

    u = create_user("charlie", "charlie@bu.com")
    updated = update_user(u.id, "charlie_new", "charlie_new@bu.com")
    assert updated is not None
    assert updated.username == "charlie_new"
    assert updated.email == "charlie_new@bu.com"

def test_delete_user():
    from user import user_data, user_id_counter, create_user, delete_user, get_user
    user_data.clear()
    user_id_counter = 0

    u = create_user("dan", "dan@bu.com")
    user_id = u.id
    assert get_user(user_id) is not None

    result = delete_user(user_id)
    assert result is True
    assert get_user(user_id) is None