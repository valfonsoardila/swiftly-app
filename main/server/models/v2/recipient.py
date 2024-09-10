from .Persona import Persona
from .Address import Address
import json

class Recipient(Persona):
    def __init__(self, name: str, company: str, street: str, neighborhood: str, city: str, state: str, country: str, postal_code: str,phones:list):
        super().__init__(name,phones)
        self.__company = company
        self.__address = Address(street=street, neighborhood=neighborhood,city=city, state=state, country=country, postal_code=postal_code)

    def getAddress(self)->Address:
        return self.__address
    
    def setAddress(self, address: Address):
        self.__address = address
    
    def getCompany(self):
        return self.__company

    def setCompany(self, company: str):
        self.__company = company

    def get_name(self) -> str:
        return super().get_name()
    def set_name(self, name: str):
        return super().set_name(name)
    def setId(self, id: str):
        return super().setId(id)
    def getId(self) -> str:
        return super().getId()
    def get_phones(self) -> list:
        return super().get_phones()
        
    def to_json(self):
        return {
            "id": self.getId(),
            "name": self.get_name(),
            "company": self.__company,
            "address":self.__address.to_json(),
            "phones": self.get_phones()
        }

    @classmethod
    def from_json(cls, data):
        id = data.get("id")
        name = data.get("name")
        company = data.get("company")
        address_data = data.get("address")
        phones = data.get("phones")

        # Crear la dirección a partir del JSON
        address = Address.from_json(address_data)

        # Crear una instancia de Recipient con los datos obtenidos
        recipient = cls(
            name=name,
            company=company,
            street=address.get_street(),
            neighborhood=address.get_neighborhood(),
            city=address.get_city(),
            state=address.get_state(),
            country=address.get_country(),
            postal_code=address.get_postal_code(),
            phones=phones
        )

        # Establecer el ID
        recipient.setId(id)

        return recipient