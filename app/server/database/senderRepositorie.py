from models.sender import Sender


class SenderRepository:
    def __init__(self, conexion_fb):
        self.conexion_fb = conexion_fb
        self.collection_name = "senders"

    def add_sender(self, sender):
        try:
            sender_id = self.conexion_fb.insertTabla(self.collection_name, sender.toJson())
            return sender_id
        except Exception as e:
            return f"Error al agregar remitente: {str(e)}"

    def delete_sender(self, sender_id):
        try:
            result = self.conexion_fb.deleteTabla(self.collection_name, sender_id)
            return result
        except Exception as e:
            return f"Error al eliminar remitente: {str(e)}"

    def get_all_senders(self):
        try:
            senders_data = self.conexion_fb.consultarTabla(self.collection_name)
            senders = []
            for sender_id, sender_data in senders_data:
                sender = Sender.fromJson(sender_data)
                senders.append((sender_id, sender))
            return senders
        except Exception as e:
            return f"Error al consultar remitentes: {str(e)}"

    def update_sender(self, sender_id, new_data):
        try:
            result = self.conexion_fb.updateTabla(self.collection_name, sender_id, new_data)
            return result
        except Exception as e:
            return f"Error al actualizar remitente: {str(e)}"
