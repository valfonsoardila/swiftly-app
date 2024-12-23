import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

load_dotenv(override=True)  # Cargar variables del archivo .env


# Patron de diseño Singleton
class Firebase_Config:
    _instance = None
    _db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Firebase_Config, cls).__new__(cls)
            cls._initialize_firebase(cls)
        return cls._instance

    @classmethod
    def _initialize_firebase(self, cls):
        credentialsUser = cls._create_json_access()
        cred = credentials.Certificate(credentialsUser)
        firebase_admin.initialize_app(cred)
        cls._db = firestore.client()

    @classmethod
    def _create_json_access(cls):
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

    @classmethod
    def get_db(cls):
        if cls._db is None:
            cls._initialize_firebase()
        return cls._db
