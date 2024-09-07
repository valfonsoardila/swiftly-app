from main.server.api.firebase.firebase_config import Firebase_Config
from google.cloud.firestore_v1 import FieldFilter

db =Firebase_Config.initialize_firebase()




def create_guide(guide_data):
    guide_ref = db.collection("guides")
    check = guide_ref.add(guide_data)
    check_id = check[1].id
    return True if check_id else False

def read_guide(guide_id):
    # Crear el filtro
    filter_criteria = FieldFilter("id", "==", guide_id)

    # Usar el filtro en la consulta
    guide_ref = db.collection("guides").where(filter=filter_criteria)
    guide_docs = guide_ref.get()

    # Verifica si la consulta devolvió algún resultado
    if len(guide_docs) > 0:
        guide = guide_docs[0]
        return guide.to_dict()
    else:
        return None


def update_guide(guide_id, update_data):
    guide_ref = db.collection("guides").document(guide_id)
    guide_ref.update(update_data)
    return "guide updated successfully"


def delete_guide(guide_id):
    guide_ref = db.collection("guides").document(guide_id)
    guide_ref.delete()
    return "guide deleted successfully"

def list_guide():
    guide_ref = db.collection("recipients")
    guide_docs = guide_ref.get()
    # Verifica si la consulta devolvió algún resultado
    if len(guide_docs) > 0:
        return guide_docs
    else:
        return None
