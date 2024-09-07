from main.server.api.firebase.requests import user_request


def create_user(user_data):
    result = user_request.create_user(user_data)
    return result


def read_user(email):
    result = user_request.read_user(email)
    if result:
        return result
    else:
        return "User not found"


def update_user(user_id, update_data):
    result = user_request.update_user(user_id, update_data)
    return result


def delete_user(user_id):
    result = user_request.delete_user(user_id)
    return result
