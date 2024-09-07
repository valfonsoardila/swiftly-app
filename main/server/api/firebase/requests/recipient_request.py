from main.server.api.firebase.firebase_config import initialize_firebase
from google.cloud.firestore_v1 import FieldFilter

db = initialize_firebase()


def create_recipient(recipient_data):
    recipient_ref = db.collection("recipients")
    check = recipient_ref.add(recipient_data)
    check_id = check[1].id
    return True if check_id else False


def read_recipient(recipient_id):
    # Crear el filtro
    filter_criteria = FieldFilter("id", "==", recipient_id)

    # Usar el filtro en la consulta
    recipient_ref = db.collection("recipients").where(filter=filter_criteria)
    recipient_docs = recipient_ref.get()

    # Verifica si la consulta devolvió algún resultado
    if len(recipient_docs) > 0:
        recipient = recipient_docs[0]
        return recipient.to_dict()
    else:
        return None


def update_recipient(recipient_id, update_data):
    recipient_ref = db.collection("recipients").document(recipient_id)
    recipient_ref.update(update_data)
    return "recipient updated successfully"


def delete_recipient(recipient_id):
    recipient_ref = db.collection("recipients").document(recipient_id)
    recipient_ref.delete()
    return "recipient deleted successfully"

def list_recipient():
    recipient_ref = db.collection("recipients")
    recipient_docs = recipient_ref.get()
    # Verifica si la consulta devolvió algún resultado
    if len(recipient_docs) > 0:
        return recipient_docs
    else:
        return None