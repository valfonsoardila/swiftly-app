import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os


def initialize_firebase():
    os.environ.clear()  # Clear the environment
    load_dotenv(override=True)  # Load the .env file
    credentialsUser = create_json_acces()
    cred = credentials.Certificate(credentialsUser)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db


def create_json_acces():
    credentialsUser = {
        "type": os.getenv("TYPE"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": os.getenv("PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
        "universe_domain": os.getenv("UNIVERSE_DOMAIN"),
    }
    return credentialsUser
