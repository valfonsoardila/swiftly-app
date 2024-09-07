from main.server.api.firebase.firebase_config import initialize_firebase
from google.cloud.firestore_v1 import FieldFilter

db = initialize_firebase()


def create_department(department_data):
    department_ref = db.collection("departments")
    check = department_ref.add(department_data)
    check_id = check[1].id
    return True if check_id else False

def list_senders():
    department_ref = db.collection("departments")
    department_docs = department_ref.get()
    # Verifica si la consulta devolvió algún resultado
    if len(department_docs) > 0:
        return department_docs
    else:
        return None