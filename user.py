user_data = {}
user_id_counter = 0

class User:
    def __init__(self, user_id, username, email):
        self.id = user_id
        self.username = username
        self.email = email

# Functions to create and get users

def create_user(username, email):
    global user_id_counter
    user_id_counter += 1
    user_id = str(user_id_counter)
    new_user = User(user_id, username, email)
    user_data[user_id] = new_user
    return new_user

def get_user(user_id):
    return user_data.get(user_id, None)
