class ServiceTypeService:
    def __init__(self, service_type_repository):
        self.service_type_repository = service_type_repository

    def create_service_type(self, service_type):
        # Lógica para verificar si el tipo de servicio ya existe
        existing_service_type = self.service_type_repository.get_service_type_by_name(service_type.getName())
        if existing_service_type:
            return "Error: El tipo de servicio ya existe"
        
        # Agregar el tipo de servicio a la base de datos
        service_type_id = self.service_type_repository.add_service_type(service_type)
        return service_type_id

    def get_service_type_details(self, service_type_id):
        service_type = self.service_type_repository.get_service_type_by_id(service_type_id)
        if not service_type:
            return "Error: Tipo de servicio no encontrado"
        return service_type

    def update_service_type(self, service_type_id, updated_data):
        # Lógica para actualizar los datos de un tipo de servicio existente
        result = self.service_type_repository.update_service_type(service_type_id, updated_data)
        return result

    def delete_service_type(self, service_type_id):
        result = self.service_type_repository.delete_service_type(service_type_id)
        return result
