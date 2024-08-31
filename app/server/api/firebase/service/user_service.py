from app.server.api.firebase.firebase_config import initialize_firebase

db = initialize_firebase()


def create_user(user_data):
    users_ref = db.collection("users")
    check = users_ref.add(user_data)
    check_id = check[1].id
    return True if check_id else False


def read_user(user_id):
    user_ref = db.collection("users").document(user_id)
    user = user_ref.get()
    if user.exists:
        return user.to_dict()
    else:
        return None


def update_user(user_id, update_data):
    user_ref = db.collection("users").document(user_id)
    user_ref.update(update_data)
    return "User updated successfully"


def delete_user(user_id):
    user_ref = db.collection("users").document(user_id)
    user_ref.delete()
    return "User deleted successfully"
