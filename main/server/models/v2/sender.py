from .Persona import  Persona
import json
from datetime import datetime
class Sender(Persona):
    def __init__(self, name: str, department: str,phone:list):
        super().__init__(name,phone)
        self.__department = department
    
    def get_department(self):
        return self.__department

    def set_department(self, department: str):
        self.__department = department
        
    def get_name(self) -> str:
        return super().get_name()
    from datetime import datetime
from Guide import Guide
import json

class Package(Guide):
    def __init__(self, guide_number: int, description: str, weight: float, declared_value: float, international: bool):
        super().__init__(guide_number, description, weight, declared_value, international)
        self.__additional_fee = 0

    # Getters y setters para atributos heredados
    def get_guide_number(self) -> int:
        return super().get_guide_number()

    def set_guide_number(self, guide_number: int):
        super().set_guide_number(guide_number)

    def get_description(self) -> str:
        return super().get_description()

    def set_description(self, description: str):
        super().set_description(description)

    def get_weight(self) -> float:
        return super().get_weight()

    def set_weight(self, weight: float):
        super().set_weight(weight)

    def get_declared_value(self) -> float:
        return super().get_declared_value()

    def set_declared_value(self, declared_value: float):
        super().set_declared_value(declared_value)

    def is_international(self) -> bool:
        return super().is_international()

    def set_international(self, international: bool):
        super().set_international(international)

    def getDate(self) -> datetime:
        return super().getDate()

    def setDate(self, date: datetime):
        super().setDate(date)

    # Métodos específicos de Package
    def get_additional_fee(self) -> float:
        return self.__additional_fee

    def set_additional_fee(self, additional_fee: float):
        self.__additional_fee = additional_fee

    def calculate_cost(self):
        return (super().calculate_cost() * self.get_weight()) + self.__additional_fee

    # Métodos JSON
    def to_json(self):
        return {
            "guide_number": self.get_guide_number(),
            "description": self.get_description(),
            "weight": self.get_weight(),
            "declared_value": self.get_declared_value(),
            "international": self.is_international(),
            "additional_fee": self.get_additional_fee(),
            "date": self.getDate().isoformat()  # Assuming getDate() returns a datetime object
        }

    @classmethod
    def from_json(cls, data):
        guide_number = data.get("guide_number")
        description = data.get("description")
        weight = data.get("weight")
        declared_value = data.get("declared_value")
        international = data.get("international")
        additional_fee = data.get("additional_fee")
        date_str = data.get("date")
        date = datetime.fromisoformat(date_str) if date_str else datetime.now()

        package = cls(guide_number, description, weight, declared_value, international)
        package.set_additional_fee(additional_fee)
        package.setDate(date)
        return package

    def set_name(self, name: str):
        return super().set_name(name)
    
    def get_phones(self) -> list:
        return super().get_phones()
    
    def getId(self) -> str:
        return super().getId()
    
    def setId(self, id: str):
        return super().setId(id)

    def to_json(self):
        return {
            "id": self.getId(),
            "name": self.get_name(),
            "department": self.__department,
            "phones": self.get_phones()
        }

    
    @classmethod
    def from_json(cls, data):
        id = data.get("id")
        name = data.get("name")
        departament = data.get("department")
        phone = data.get("phone")
        sender = cls(name,departament,phone)
        sender.setId(id)
        return sender