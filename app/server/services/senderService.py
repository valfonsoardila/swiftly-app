class SenderService:
    def __init__(self, sender_repository):
        self.sender_repository = sender_repository

    def create_sender(self, sender):
        # Lógica para verificar si el remitente ya existe
        existing_sender = self.sender_repository.get_sender_by_email(sender.getEmail())
        if existing_sender:
            return "Error: El remitente ya existe"
        
        # Agregar el remitente a la base de datos
        sender_id = self.sender_repository.add_sender(sender)
        return sender_id

    def get_sender_details(self, sender_id):
        sender = self.sender_repository.get_sender_by_id(sender_id)
        if not sender:
            return "Error: Remitente no encontrado"
        return sender

    def update_sender(self, sender_id, updated_data):
        # Lógica para actualizar los datos de un remitente existente
        result = self.sender_repository.update_sender(sender_id, updated_data)
        return result

    def delete_sender(self, sender_id):
        result = self.sender_repository.delete_sender(sender_id)
        return result
