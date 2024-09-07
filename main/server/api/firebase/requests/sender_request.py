from main.server.api.firebase.firebase_config import Firebase_Config
from google.cloud.firestore_v1 import FieldFilter

db =Firebase_Config.initialize_firebase()



def create_sender(sender_data):
    sender_ref = db.collection("senders")
    check = sender_ref.add(sender_data)
    check_id = check[1].id
    return True if check_id else False


def read_sender(sender_id):
    # Crear el filtro
    filter_criteria = FieldFilter("id", "==", sender_id)

    # Usar el filtro en la consulta
    sender_ref = db.collection("senders").where(filter=filter_criteria)
    sender_docs = sender_ref.get()

    # Verifica si la consulta devolvió algún resultado
    if len(sender_docs) > 0:
        sender = sender_docs[0]
        return sender.to_dict()
    else:
        return None


def update_sender(sender_id, update_data):
    sender_ref = db.collection("senders").document(sender_id)
    sender_ref.update(update_data)
    return "sender updated successfully"


def delete_sender(sender_id):
    sender_ref = db.collection("senders").document(sender_id)
    sender_ref.delete()
    return "sender deleted successfully"

def list_senders():
    sender_ref = db.collection("senders")
    sender_docs = sender_ref.get()
    # Verifica si la consulta devolvió algún resultado
    if len(sender_docs) > 0:
        return sender_docs
    else:
        return None