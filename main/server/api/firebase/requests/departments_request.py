from main.server.api.firebase.firebase_config import Firebase_Config

# Obtener la instancia de la base de datos
db = Firebase_Config().get_db()


def create_departments(name_doc, departments_data):
    departments_ref = db.collection("departments").document(name_doc)
    departments_ref.set(departments_data)
    return True


def read_departments(number_of_departments):
    departments_ref = db.collection("departments").document(number_of_departments)
    departments_docs = departments_ref.get()
    if departments_docs.exists:
        return departments_docs.to_dict()
    else:
        return None


def read_departmentss():
    departments_ref = db.collection("departments")
    departments_docs = departments_ref.get()
    users = [user.to_dict() for user in departments_docs]
    return users


def update_departments(number_of_departments, update_data):
    departments_ref = db.collection("departments").document(number_of_departments)
    departments_ref.update(update_data)
    return "departments updated successfully"


def delete_departments(number_of_departments):
    departments_ref = db.collection("departments").document(number_of_departments)
    departments_ref.delete()
    return "departments deleted successfully"
