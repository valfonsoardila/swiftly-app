from models.guide import Guide


class GuideRepository:
    def __init__(self, conexion_fb):
        self.conexion_fb = conexion_fb
        self.collection_name = "guides"

    def add_guide(self, guide):
        try:
            guide_id = self.conexion_fb.insertTabla(self.collection_name, guide.toJson())
            return guide_id
        except Exception as e:
            return f"Error al agregar guía: {str(e)}"

    def delete_guide(self, guide_id):
        try:
            result = self.conexion_fb.deleteTabla(self.collection_name, guide_id)
            return result
        except Exception as e:
            return f"Error al eliminar guía: {str(e)}"

    def get_all_guides(self):
        try:
            guides_data = self.conexion_fb.consultarTabla(self.collection_name)
            guides = []
            for guide_id, guide_data in guides_data:
                guide = Guide.fromJson(guide_data)
                guides.append((guide_id, guide))
            return guides
        except Exception as e:
            return f"Error al consultar guías: {str(e)}"

    def update_guide(self, guide_id, new_data):
        try:
            result = self.conexion_fb.updateTabla(self.collection_name, guide_id, new_data)
            return result
        except Exception as e:
            return f"Error al actualizar guía: {str(e)}"
