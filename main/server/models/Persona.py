from abc import ABC, abstractmethod
import json
import uuid

class Persona(ABC):
    def __init__(self, name: str, phones: list):
        self.__id = str(uuid.uuid4())
        self.__name = name
        self.__phones = phones

    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def set_id(self, id: str):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def set_name(self, name: str):
        pass

    def add_phone(self, phone: str):
        self.__phones.append(phone)

    def remove_phone(self, phone: str):
        if phone in self.__phones:
            self.__phones.remove(phone)

    def get_phones(self) -> list:
        return self.__phones

    def to_json(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "phones": self.__phones
        }

    @classmethod
    def from_json(cls, data):
        # Este método debe ser implementado en las clases derivadas
        raise NotImplementedError("Subclasses should implement this method.")
