import firebase_admin
from firebase_admin import credentials, firestore, auth, storage

class ConnecionFB():
    def __init__(self):
        super().__init__()
        self.estado = self.conexion()

    def conexion(self, ):
        try:
            cred = credentials.Certificate("database\serviceAccountKey.json")
            #self. app =firebase_admin.initialize_app(cred,{'storageBucket': 'dulce-tentacion-app.appspot.com'})
            self. app =firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            self.auth = auth
            self.storage = storage
            return True
        except Exception as e:
            print("Error de conexión a Firebase:", e)
            return False

    def closeConnection(self):
        firebase_admin.delete_app(self.app)
    # Operaciones CRUD para Firestore
    def consultarTabla(self, tabla):
        if self.estado:
            try:
                datos = self.db.collection(tabla).get()
                listaDatos = []
                for dato in datos:
                    listaDatos.append((dato.id, dato.to_dict()))
                return listaDatos
            except Exception as e:
                print("Error al consultar tabla:", e)
                return []
        else:
            return "No hay conexión a Firebase"

        
    def insertTabla(self, tabla, dato, id=None):
        if self.estado:
            try:
                if id is None:
                    _,doc_ref= self.db.collection(tabla).add(dato)
                else:
                    _,doc_ref= self.db.collection(tabla).add(dato,id)
                return doc_ref.id
            except Exception as e:
                return "Error al insertar en tabla:", e
        else:
            return "No hay conexión a Firebase"

    def deleteTabla(self, tabla, id):
        if self.estado:
            try:
                self.db.collection(tabla).document(id).delete()
                return "Documento eliminado correctamente"
            except Exception as e:
                return ("Error al eliminar documento de tabla:", e)
        else:
            return "No hay conexión a Firebase"

    def updateTabla(self, tabla, id, new_data):
        try:
            self.db.collection(tabla).document(id).update(new_data)
            return "datos actualizados correctamente."
        except Exception as e:
            return f"Error al actualizar: {str(e)}"
    # Operaciones CRUD para la autenticación
    def crear_usuario(self, email, password):
        try:
            user = self.auth.create_user(email=email, password=password)
            print
            return user.uid,("Usuario creado exitosamente")
        except Exception as e:
            return None,("Error al crear usuario:", e)

    def leer_usuario(self, uid):
        try:
            user = self.auth.get_user(uid)
            print("Usuario encontrado:", user.email)
            return user
        except Exception as e:
            print("Error al leer usuario:", e)

    def actualizar_usuario(self, uid, email=None, password=None):
        try:
            user = self.auth.update_user(uid, email=email, password=password)
            print("Usuario actualizado exitosamente:", user.uid)
            return user.uid
        except Exception as e:
            print("Error al actualizar usuario:", e)

    def eliminar_usuario(self, uid):
        try:
            self.auth.delete_user(uid)
            print("Usuario eliminado exitosamente.")
        except Exception as e:
            print("Error al eliminar usuario:", e)

    # Operaciones CRUD para el almacenamiento (Storage)
    def subir_archivo(self, source_file_name, destination_blob_name):
        try:
            bucket = self.storage.bucket(app=self. app)
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_string(source_file_name)
            return "Archivo subido exitosamente."
        except Exception as e:
            return "Error al subir archivo:", e

    def descargar_archivo(self, bucket_name, source_blob_name, destination_file_name):
        try:
            bucket = self.storage.Client().bucket(bucket_name)
            blob = bucket.blob(source_blob_name)
            blob.download_to_filename(destination_file_name)
            print("Archivo descargado exitosamente.")
        except Exception as e:
            print("Error al descargar archivo:", e)

    def eliminar_archivo(self, bucket_name, blob_name):
        try:
            bucket = self.storage.Client().bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.delete()
            print("Archivo eliminado exitosamente.")
        except Exception as e:
            print("Error al eliminar archivo:", e)

