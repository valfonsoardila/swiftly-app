class FileService:
    def __init__(self, file_repository):
        self.file_repository = file_repository

    def create_file(self, file):
        # Lógica para agregar un archivo a la base de datos
        file_id = self.file_repository.add_file(file)
        return file_id

    def get_file_details(self, file_id):
        file = self.file_repository.get_file_by_id(file_id)
        if not file:
            return "Error: Archivo no encontrado"
        return file

    def update_file(self, file_id, updated_data):
        # Lógica para actualizar los datos de un archivo existente
        result = self.file_repository.update_file(file_id, updated_data)
        return result

    def delete_file(self, file_id):
        result = self.file_repository.delete_file(file_id)
        return result
