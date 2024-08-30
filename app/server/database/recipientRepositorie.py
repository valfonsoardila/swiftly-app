from models.recipient import Recipient


class RecipientRepository:
    def __init__(self, conexion_fb):
        self.conexion_fb = conexion_fb
        self.collection_name = "recipients"

    def add_recipient(self, recipient):
        try:
            recipient_id = self.conexion_fb.insertTabla(self.collection_name, recipient.toJson())
            return recipient_id
        except Exception as e:
            return f"Error al agregar destinatario: {str(e)}"

    def delete_recipient(self, recipient_id):
        try:
            result = self.conexion_fb.deleteTabla(self.collection_name, recipient_id)
            return result
        except Exception as e:
            return f"Error al eliminar destinatario: {str(e)}"

    def get_all_recipients(self):
        try:
            recipients_data = self.conexion_fb.consultarTabla(self.collection_name)
            recipients = []
            for recipient_id, recipient_data in recipients_data:
                recipient = Recipient.fromJson(recipient_data)
                recipients.append((recipient_id, recipient))
            return recipients
        except Exception as e:
            return f"Error al consultar destinatarios: {str(e)}"

    def update_recipient(self, recipient_id, new_data):
        try:
            result = self.conexion_fb.updateTabla(self.collection_name, recipient_id, new_data)
            return result
        except Exception as e:
            return f"Error al actualizar destinatario: {str(e)}"
