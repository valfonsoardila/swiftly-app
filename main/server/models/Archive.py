import json
from Guide import Guide

class Archive:
    def __init__(self, year: str, month: str):
        self.__id = f"{year}{month}"
        self.__year = year
        self.__month = month
        self.guides = []

    # Getters y Setters para __id
    def get_id(self) -> str:
        return self.__id

    def set_id(self, id: str):
        self.__id = id
    
    # Getters y Setters para year
    def get_year(self) -> str:
        return self.__year

    def set_year(self, year: str):
        self.__year = year

    # Getters y Setters para month
    def get_month(self) -> str:
        return self.__month

    def set_month(self, month: str):
        self.__month = month

    # Obtener lista de guías
    def get_guide_list(self):
        return self.guides

    # Añadir una guía
    def add_guide(self, guide: Guide):
        self.guides.append(guide)

    # Encontrar guía por número
    def find_guide_by_number(self, guide_number: int):
        for guide in self.guides:
            if guide.get_guide_number() == guide_number:
                return guide
        return None

    # Encontrar guías por destinatario
    def find_guides_by_recipient(self, recipient):
        return [guide for guide in self.guides if guide.get_recipient() == recipient]

    # Convertir a JSON
    def to_json(self):
        return {
            "id": self.get_id(),
            "year": self.get_year(),
            "month": self.get_month(),
            "guides": [guide.to_json() for guide in self.get_guide_list()]
        }

    # Crear instancia desde JSON
    @classmethod
    def from_json(cls, data):
        year = data.get("year")
        month = data.get("month")
        archive = cls(year, month)
        
        guides_data = data.get("guides", [])
        for guide_data in guides_data:
            guide = Guide.from_json(guide_data)  # Ajusta esta línea según cómo implementes `from_json` en `Guide`
            archive.add_guide(guide)
        
        return archive
