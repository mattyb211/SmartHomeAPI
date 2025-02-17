user_data = {}
user_id_counter = 0

class User:
    def __init__(self, user_id, username, email):
        self.id = user_id
        self.username = username
        self.email = email

def create_user(username, email):

    if not username or username.strip() == "":
        return {"error": "Username cannot be empty."}
    if "@" not in email:
        return {"error": "Invalid email address, must contain '@'."}

    global user_id_counter
    user_id_counter += 1
    uid = str(user_id_counter)
    new_user = User(uid, username, email)
    user_data[uid] = new_user
    return {
        "success": True,
        "data": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }
    }

def get_user(user_id):
    if user_id not in user_data:
        return {"error": f"User with ID {user_id} not found."}

    u = user_data[user_id]
    return {
        "success": True,
        "data": {
            "id": u.id,
            "username": u.username,
            "email": u.email
        }
    }

def update_user(user_id, new_username, new_email):
    if user_id not in user_data:
        return {"error": f"Cannot update: user with ID {user_id} not found."}

    if not new_username or new_username.strip() == "":
        return {"error": "Username cannot be empty."}
    if "@" not in new_email:
        return {"error": "Invalid email address, must contain '@'."}

    u = user_data[user_id]
    u.username = new_username
    u.email = new_email
    return {
        "success": True,
        "data": {
            "id": u.id,
            "username": u.username,
            "email": u.email
        }
    }

def delete_user(user_id):
    if user_id not in user_data:
        return {"error": f"Cannot delete: user with ID {user_id} not found."}

    del user_data[user_id]
    return {"success": True}