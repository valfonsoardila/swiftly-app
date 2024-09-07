from main.server.api.firebase.firebase_config import Firebase_Config
from google.cloud.firestore_v1 import FieldFilter

db =Firebase_Config.initialize_firebase()


def create_serviceType(serviceType_data):
    serviceType_ref = db.collection("serviceType")
    check = serviceType_ref.add(serviceType_data)
    check_id = check[1].id
    return True if check_id else False


def read_serviceType(serviceType_id):
    # Crear el filtro
    filter_criteria = FieldFilter("id", "==", serviceType_id)

    # Usar el filtro en la consulta
    serviceType_ref = db.collection("serviceType").where(filter=filter_criteria)
    serviceType_docs = serviceType_ref.get()

    # Verifica si la consulta devolvió algún resultado
    if len(serviceType_docs) > 0:
        serviceType = serviceType_docs[0]
        return serviceType.to_dict()
    else:
        return None


def update_serviceType(serviceType_id, update_data):
    serviceType_ref = db.collection("serviceType").document(serviceType_id)
    serviceType_ref.update(update_data)
    return "serviceType updated successfully"


def delete_serviceType(serviceType_id):
    serviceType_ref = db.collection("serviceType").document(serviceType_id)
    serviceType_ref.delete()
    return "serviceType deleted successfully"
