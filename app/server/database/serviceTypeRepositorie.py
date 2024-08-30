from models.serviceType import ServiceType


class ServiceTypeRepository:
    def __init__(self, conexion_fb):
        self.conexion_fb = conexion_fb
        self.collection_name = "service_types"

    def add_service_type(self, service_type):
        try:
            service_type_id = self.conexion_fb.insertTabla(self.collection_name, service_type.toJson())
            return service_type_id
        except Exception as e:
            return f"Error al agregar tipo de servicio: {str(e)}"

    def delete_service_type(self, service_type_id):
        try:
            result = self.conexion_fb.deleteTabla(self.collection_name, service_type_id)
            return result
        except Exception as e:
            return f"Error al eliminar tipo de servicio: {str(e)}"

    def get_all_service_types(self):
        try:
            service_types_data = self.conexion_fb.consultarTabla(self.collection_name)
            service_types = []
            for service_type_id, service_type_data in service_types_data:
                service_type = ServiceType.fromJson(service_type_data)
                service_types.append((service_type_id, service_type))
            return service_types
        except Exception as e:
            return f"Error al consultar tipos de servicio: {str(e)}"

    def update_service_type(self, service_type_id, new_data):
        try:
            result = self.conexion_fb.updateTabla(self.collection_name, service_type_id, new_data)
            return result
        except Exception as e:
            return f"Error al actualizar tipo de servicio: {str(e)}"
