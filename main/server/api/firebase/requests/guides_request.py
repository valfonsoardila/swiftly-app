from main.server.api.firebase.firebase_config import Firebase_Config
from google.cloud.firestore_v1 import FieldFilter

db =Firebase_Config.initialize_firebase()


def create_guide(guide_data):
    guides_ref = db.collection("guides")
    check = guides_ref.add(guide_data)
    check_id = check[1].id
    return True if check_id else False


def read_guide(number_of_guide):
    guide_ref = db.collection("guides").document(number_of_guide)
    guide_docs = guide_ref.get()
    if guide_docs.exists:
        return guide_docs.to_dict()
    else:
        return None


def read_guides():
    guide_ref = db.collection("guides")
    guide_docs = guide_ref.get()
    users = [user.to_dict() for user in guide_docs]
    return users


def update_guide(number_of_guide, update_data):
    guide_ref = db.collection("users").document(number_of_guide)
    guide_ref.update(update_data)
    return "Guide updated successfully"


def delete_guide(number_of_guide):
    guide_ref = db.collection("users").document(number_of_guide)
    guide_ref.delete()
    return "Guide deleted successfully"
