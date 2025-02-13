def test_create_user():
    from user import user_data, user_id_counter, create_user
    user_data.clear()
    user_id_counter = 0

    result = create_user("Mateo", "Mateo@bu.com")
    # Now we expect a dictionary with 'success' and 'data'
    assert "success" in result
    assert result["success"] is True

    data = result["data"]
    assert data["username"] == "Mateo"
    assert data["email"] == "Mateo@bu.com"
    assert data["id"] == "1"
    # Optionally confirm user_data was updated
    assert "1" in user_data

def test_get_user():
    from user import user_data, user_id_counter, create_user, get_user
    user_data.clear()
    user_id_counter = 0

    create_result = create_user("Noah", "Noah@bu.com")
    # Grab the user ID from create_result
    user_id = create_result["data"]["id"]

    get_result = get_user(user_id)
    # Should be 'success' in the returned dict
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

    # There's no user with ID '999', so we expect an error dict
    result = get_user("999")
    assert "error" in result
    # You can check the error message
    assert "not found" in result["error"].lower()

def test_update_user():
    from user import user_data, user_id_counter, create_user, update_user
    user_data.clear()
    user_id_counter = 0

    # Create a user
    create_result = create_user("Charlie", "charlie@bu.com")
    user_id = create_result["data"]["id"]

    # Update the user
    update_result = update_user(user_id, "charlie_new", "charlie_new@bu.com")
    assert "success" in update_result
    assert update_result["success"] is True

    data = update_result["data"]
    assert data["username"] == "charlie_new"
    assert data["email"] == "charlie_new@bu.com"

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