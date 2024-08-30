class GuideService:
    def __init__(self, guide_repository, recipient_repository, sender_repository, service_type_repository):
        self.guide_repository = guide_repository
        self.recipient_repository = recipient_repository
        self.sender_repository = sender_repository
        self.service_type_repository = service_type_repository

    def create_guide(self, guide, recipient_id, sender_id, service_type_id):
        # Lógica para verificar si los datos necesarios existen
        recipient = self.recipient_repository.get_recipient_by_id(recipient_id)
        sender = self.sender_repository.get_sender_by_id(sender_id)
        service_type = self.service_type_repository.get_service_type_by_id(service_type_id)
        
        if not recipient:
            return "Error: Destinatario no existe"
        if not sender:
            return "Error: Remitente no existe"
        if not service_type:
            return "Error: Tipo de servicio no existe"
        
        # Lógica para calcular el costo basado en el tipo de servicio
        cost = self.calculate_cost(service_type, guide.weight, guide.volume)
        guide.setCost(cost)
        
        # Agregar la guía a la base de datos
        guide_id = self.guide_repository.add_guide(guide)
        return guide_id

    def calculate_cost(self, service_type, weight, volume):
        # Ejemplo de una lógica de negocio para calcular el costo de la guía
        base_cost = service_type.getRatePerWeight() * weight + service_type.getRatePerVolume() * volume
        if service_type.getIsInternational():
            base_cost += 50  # Suplemento para servicios internacionales
        return base_cost

    def finalize_guide(self, guide_id):
        # Lógica para cambiar el estado de la guía a 'FINALIZADA'
        guide_data = {"status": "FINALIZADA"}
        result = self.guide_repository.update_guide(guide_id, guide_data)
        return result

    def get_guide_details(self, guide_id):
        # Lógica para obtener detalles completos de la guía
        guide = self.guide_repository.get_guide_by_id(guide_id)
        if not guide:
            return "Error: Guía no encontrada"
        
        # Puedes añadir más lógica aquí si es necesario (ej. juntar datos del destinatario/remitente)
        return guide
