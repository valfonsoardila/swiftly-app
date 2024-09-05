from main.server.api.firebase.service import user_service


def create_user(user_data):
    result = user_service.create_user(user_data)
    return result


def read_user(email):
    result = user_service.read_user(email)
    if result:
        return result
    else:
        return "User not found"


def update_user(user_id, update_data):
    result = user_service.update_user(user_id, update_data)
    return result


def delete_user(user_id):
    result = user_service.delete_user(user_id)
    return result
