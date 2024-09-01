import firebase_admin
from firebase_admin import credentials, firestore, auth, storage
from dotenv import load_dotenv
import os


def initialize_firebase():
    load_dotenv()
    credentialsUser = create_json_acces()
    cred = credentials.Certificate(credentialsUser)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db


def create_json_acces():
    # Obtiene el directorio del script actual
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construye la ruta a 4 niveles hacia atrás
    parent_dir = os.path.abspath(os.path.join(base_dir, "../../../../"))

    # Construye la ruta al archivo de clave privada
    private_key_path = os.path.join(parent_dir, "private_key.pem")

    # Lee el contenido del archivo de clave privada
    with open(private_key_path, "r") as file:
        private_key = file.read()
    credentialsUser = {
        "type": os.getenv("TYPE"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": private_key,
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
        "universe_domain": os.getenv("UNIVERSE_DOMAIN"),
    }
    return credentialsUser
