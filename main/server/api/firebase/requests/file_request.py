from main.server.api.firebase.firebase_config import Firebase_Config
from google.cloud.firestore_v1 import FieldFilter

db =Firebase_Config.initialize_firebase()


def create_file(file_data):
    users_ref = db.collection("files")
    check = users_ref.add(file_data)
    check_id = check[1].id
    return True if check_id else False


def read_file(file_id):
    # Crear el filtro
    filter_criteria = FieldFilter("id", "==", file_id)

    # Usar el filtro en la consulta
    file_ref = db.collection("files").where(filter=filter_criteria)
    file_docs = file_ref.get()

    # Verifica si la consulta devolvió algún resultado
    if len(file_docs) > 0:
        file = file_docs[0]
        return file.to_dict()
    else:
        return None


def update_file(file_id, update_data):
    file_ref = db.collection("files").document(file_id)
    file_ref.update(update_data)
    return "User updated successfully"


def delete_file(file_id):
    file_ref = db.collection("files").document(file_id)
    file_ref.delete()
    return "User deleted successfully"
