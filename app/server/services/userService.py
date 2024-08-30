from firebase_admin import auth

from app.server.models.user import User

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, fullname, password, email):
        # Lógica para verificar si el usuario ya existe en Firebase Auth
        try:
            existing_user = auth.get_user_by_email(email)
            if existing_user:
                return "Error: El usuario con este correo ya existe"
        except auth.UserNotFoundError:
            pass  # Si no se encuentra, podemos continuar

        # Crear un nuevo usuario y agregarlo a Firebase Authentication y Firestore
        new_user = User(fullname, password, email)
        user_id = self.user_repository.register_user(new_user)
        return user_id

    def get_user_details(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            return "Error: Usuario no encontrado"
        return user

    def update_user(self, user_id, fullname=None, password=None, email=None):
        # Obtener el usuario actual
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            return "Error: Usuario no encontrado"
        
        # Actualizar los datos en Firebase Auth si es necesario
        try:
            if fullname:
                auth.update_user(user_id, display_name=fullname)
            if email:
                auth.update_user(user_id, email=email)
            if password:
                auth.update_user(user_id, password=password)
        except Exception as e:
            return f"Error al actualizar el usuario en Firebase Auth: {str(e)}"

        # Actualizar los datos en Firestore
        if fullname:
            user.setFullname(fullname)
        if email:
            user.setEmail(email)
        updated_data = user.toJson()
        result = self.user_repository.update_user(user_id, updated_data)
        return result

    def delete_user(self, user_id):
        result = self.user_repository.delete_user(user_id)
        return result

    def authenticate_user(self, email, password):
        # Firebase Admin SDK no tiene un método directo para verificar credenciales,
        # así que normalmente esto se haría en el lado del cliente con Firebase SDK
        # para apps móviles/web. Sin embargo, podemos manejar lógica personalizada aquí.
        try:
            user = auth.get_user_by_email(email)
            # Aquí deberías usar el cliente Firebase para autenticar (generalmente desde el lado del cliente)
            if user:
                return user.uid
            else:
                return "Error: Usuario no encontrado"
        except Exception as e:
            return f"Error al autenticar el usuario: {str(e)}"
