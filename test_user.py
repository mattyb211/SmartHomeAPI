
def test_create_user():
    from user import user_data, user_id_counter, create_user
    user_data.clear()
    user_id_counter = 0

    result = create_user("Mateo", "Mateo@bu.com")
    # Check basic success structure
    assert "success" in result
    assert result["success"] is True

    data = result["data"]
    assert data["username"] == "Mateo"
    assert data["email"] == "Mateo@bu.com"
    assert data["id"] == "1"

    # Optionally confirm user_data was updated
    assert "1" in user_data

def test_create_user_invalid():
    from user import user_data, user_id_counter, create_user
    user_data.clear()
    user_id_counter = 0

    # Empty username
    result = create_user("", "test@bu.com")
    assert "error" in result
    assert "cannot be empty" in result["error"].lower()

    # Invalid email
    result2 = create_user("TestUser", "testbu.com")
    assert "error" in result2
    assert "invalid email" in result2["error"].lower()

def test_get_user():
    from user import user_data, user_id_counter, create_user, get_user
    user_data.clear()
    user_id_counter = 0

    create_result = create_user("Noah", "Noah@bu.com")
    user_id = create_result["data"]["id"]

    get_result = get_user(user_id)
    assert "success" in get_result
    assert get_result["success"] is True

    data = get_result["data"]
    assert data["id"] == user_id
    assert data["username"] == "Noah"
    assert data["email"] == "Noah@bu.com"

def test_get_nonexistent_user():
    from user import user_data, user_id_counter, get_user
    user_data.clear()
    user_id_counter = 0

    result = get_user("999")  # no user with ID 999
    assert "error" in result
    assert "not found" in result["error"].lower()

def test_update_user():
    from user import user_data, user_id_counter, create_user, update_user
    user_data.clear()
    user_id_counter = 0

    create_result = create_user("Charlie", "charlie@bu.com")
    user_id = create_result["data"]["id"]

    update_result = update_user(user_id, "charlie_new", "charlie_new@bu.com")
    assert "success" in update_result
    assert update_result["success"] is True

    data = update_result["data"]
    assert data["username"] == "charlie_new"
    assert data["email"] == "charlie_new@bu.com"

def test_update_user_invalid():
    from user import user_data, user_id_counter, create_user, update_user
    user_data.clear()
    user_id_counter = 0

    create_result = create_user("Alicia", "alicia@bu.com")
    user_id = create_result["data"]["id"]

    # Update with invalid email
    result = update_user(user_id, "Alicia", "aliciabu.com")
    assert "error" in result
    assert "invalid email" in result["error"].lower()

def test_delete_user():
    from user import user_data, user_id_counter, create_user, delete_user, get_user
    user_data.clear()
    user_id_counter = 0

    create_result = create_user("Dan", "dan@bu.com")
    user_id = create_result["data"]["id"]

    # Confirm user is present
    get_result = get_user(user_id)
    assert "success" in get_result

    # Delete user
    delete_result = delete_user(user_id)
    assert "success" in delete_result
    assert delete_result["success"] is True

    # Now user should not be found
    get_result2 = get_user(user_id)
    assert "error" in get_result2
    assert "not found" in get_result2["error"].lower()