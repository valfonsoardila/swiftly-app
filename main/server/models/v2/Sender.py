from .Persona import Persona
from datetime import datetime


class Sender(Persona):
    def __init__(self, name: str, department: str, phone: list):
        super().__init__(name, phone)
        self.__department = department

    def get_department(self):
        return self.__department

    def set_department(self, department: str):
        self.__department = department

    def get_name(self) -> str:
        return super().get_name()

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
            "phones": self.get_phones(),
        }

    @classmethod
    def from_json(cls, data):
        id = data.get("id")
        name = data.get("name")
        departament = data.get("department")
        phone = data.get("phone")
        sender = cls(name, departament, phone)
        sender.setId(id)
        return sender
