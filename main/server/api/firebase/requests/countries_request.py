from main.server.api.firebase.firebase_config import Firebase_Config

# Obtener la instancia de la base de datos
db = Firebase_Config().get_db()


def create_countrys(name_doc, countrys_data):
    countrys_ref = db.collection("countrys").document(name_doc)
    countrys_ref.set(countrys_data)
    return True


def read_contry(number_of_countrys):
    countrys_ref = db.collection("countrys").document(number_of_countrys)
    countrys_docs = countrys_ref.get()
    if countrys_docs.exists:
        return countrys_docs.to_dict()
    else:
        return None


def read_countrys():
    countrys_ref = db.collection("countrys")
    countrys_docs = countrys_ref.get()
    users = [user.to_dict() for user in countrys_docs]
    return users


def update_contry(number_of_countrys, update_data):
    countrys_ref = db.collection("countrys").document(number_of_countrys)
    countrys_ref.update(update_data)
    return "countrys updated successfully"


def delete_contry(number_of_countrys):
    countrys_ref = db.collection("countrys").document(number_of_countrys)
    countrys_ref.delete()
    return "countrys deleted successfully"
