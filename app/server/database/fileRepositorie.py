

from models.file import File


class FileRepository:
    def __init__(self, conexion_fb):
        self.conexion_fb = conexion_fb
        self.collection_name = "files"

    def add_file(self, file):
        try:
            file_id = self.conexion_fb.insertTabla(self.collection_name, file.toJson())
            return file_id
        except Exception as e:
            return f"Error al agregar archivo: {str(e)}"

    def delete_file(self, file_id):
        try:
            result = self.conexion_fb.deleteTabla(self.collection_name, file_id)
            return result
        except Exception as e:
            return f"Error al eliminar archivo: {str(e)}"

    def get_all_files(self):
        try:
            files_data = self.conexion_fb.consultarTabla(self.collection_name)
            files = []
            for file_id, file_data in files_data:
                file = File.fromJson(file_data)
                files.append((file_id, file))
            return files
        except Exception as e:
            return f"Error al consultar archivos: {str(e)}"

    def update_file(self, file_id, new_data):
        try:
            result = self.conexion_fb.updateTabla(self.collection_name, file_id, new_data)
            return result
        except Exception as e:
            return f"Error al actualizar archivo: {str(e)}"

