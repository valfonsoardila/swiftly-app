from firebase_admin import auth
from app.server.models.user import User

class UserRepository:
    def __init__(self, connection_fb):
        self.connection_fb = connection_fb
        self.table_name = "users"  # Nombre de la colección en Firestore

    def register_user(self, user):
        try:
            # Crear el usuario en Firebase Authentication
            user_record = auth.create_user(
                email=user.getEmail(),
                password=user.getPassword(),
                display_name=user.getFullname(),
            )
            # Almacenar los datos adicionales del usuario en Firestore
            user_id = user_record.uid
            user_data = user.toJson()
            user_data.pop("password")  # No almacenar la contraseña en Firestore
            self.connection_fb.insertTabla(self.table_name, user_data, user_id)
            return user_id
        except Exception as e:
            return f"Error al registrar el usuario: {str(e)}"

    def get_user_by_id(self, user_id):
        user_data = self.connection_fb.consultarTabla(self.table_name)
        if user_data:
            for data_id, data in user_data:
                if data_id == user_id:
                    return User.fromJson(data)
        return None

    def get_user_by_email(self, email):
        user_data = self.connection_fb.consultarTabla(self.table_name)
        if user_data:
            for data_id, data in user_data:
                if data["email"] == email:
                    return User.fromJson(data)
        return None

    def update_user(self, user_id, updated_data):
        result = self.connection_fb.updateTabla(self.table_name, user_id, updated_data)
        return result

    def delete_user(self, user_id):
        # Primero eliminamos el usuario de Firebase Authentication
        try:
            auth.delete_user(user_id)
        except Exception as e:
            return f"Error al eliminar el usuario de Firebase Auth: {str(e)}"

        # Luego eliminamos el usuario de Firestore
        result = self.connection_fb.deleteTabla(self.table_name, user_id)
        return result
