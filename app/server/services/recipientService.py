class RecipientService:
    def __init__(self, recipient_repository):
        self.recipient_repository = recipient_repository

    def create_recipient(self, recipient):
        # Lógica para verificar si el destinatario ya existe
        existing_recipient = self.recipient_repository.get_recipient_by_email(recipient.getEmail())
        if existing_recipient:
            return "Error: El destinatario ya existe"
        
        # Agregar el destinatario a la base de datos
        recipient_id = self.recipient_repository.add_recipient(recipient)
        return recipient_id

    def get_recipient_details(self, recipient_id):
        recipient = self.recipient_repository.get_recipient_by_id(recipient_id)
        if not recipient:
            return "Error: Destinatario no encontrado"
        return recipient

    def update_recipient(self, recipient_id, updated_data):
        # Lógica para actualizar los datos de un destinatario existente
        result = self.recipient_repository.update_recipient(recipient_id, updated_data)
        return result

    def delete_recipient(self, recipient_id):
        result = self.recipient_repository.delete_recipient(recipient_id)
        return result
