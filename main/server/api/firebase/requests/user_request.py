from main.server.api.firebase.firebase_config import Firebase_Config
from google.cloud.firestore_v1 import FieldFilter

db =Firebase_Config.initialize_firebase()


def create_user(user_data):
    users_ref = db.collection("users")
    check = users_ref.add(user_data)
    check_id = check[1].id
    return True if check_id else False


def read_user(email):
    # Crear el filtro
    filter_criteria = FieldFilter("email", "==", email)

    # Usar el filtro en la consulta
    user_ref = db.collection("users").where(filter=filter_criteria)
    user_docs = user_ref.get()

    # Verifica si la consulta devolvió algún resultado
    if len(user_docs) > 0:
        user = user_docs[0]
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
