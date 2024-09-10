from datetime import datetime
from abc import ABC, abstractmethod
import json
from .GuideStatus import GuideStatus
from .Sender import Sender
from .Recipient import Recipient


class Guide(ABC):
    def __init__(
        self,
        guide_number: int,
        date: datetime,
        description: str,
        weight: float,
        declared_value: float,
        international: bool,
        sender_name: str,
        sender_department: str,
        sender_phone: list,
        recipient_name: str,
        recipient_company: str,
        recipient_street: str,
        recipient_neighborhood: str,
        recipient_city: str,
        recipient_state: str,
        recipient_country: str,
        recipient_postal_code: str,
    ):
        self.__guide_number = guide_number
        self.__date = date
        self.__description = description
        self.__weight = weight
        self.__declared_value = declared_value
        self.__international = international
        self.__sender = Sender(sender_name, sender_department, sender_phone)
        self.__status = GuideStatus()
        self.__status.add_detalle(
            f"Central de logística de {self.__sender.get_department()}"
        )
        self.__recipient = Recipient(
            recipient_name,
            recipient_company,
            recipient_street,
            recipient_neighborhood,
            recipient_city,
            recipient_state,
            recipient_country,
            recipient_postal_code,
        )
        self.__base_cost = 5000  # Valor por defecto para el costo base

    # Getters y setters para base_cost
    def get_base_cost(self) -> float:
        return self.__base_cost

    def set_base_cost(self, base_cost: float):
        self.__base_cost = base_cost

    # Getters y setters para sender, status y recipient
    def getSender(self) -> Sender:
        return self.__sender

    def getStatus(self) -> GuideStatus:
        return self.__status

    def getRecipient(self) -> Recipient:
        return self.__recipient

    def getGuide_number(self) -> int:
        return self.__guide_number

    def setGuide_number(self, guide_number: int):
        self.__guide_number = guide_number

    def getDate(self) -> datetime:
        return self.__date

    def setDate(self, date: datetime):
        self.__date = date

    def getDescription(self) -> str:
        return self.__description

    def setDescription(self, description: str):
        self.__description = description

    def getWeight(self) -> float:
        return self.__weight

    def setWeight(self, weight: float):
        self.__weight = weight

    def getDeclared_value(self) -> float:
        return self.__declared_value

    def setDeclared_value(self, declared_value: float):
        self.__declared_value = declared_value

    def getInternational(self) -> bool:
        return self.__international

    def setInternational(self, international: bool):
        self.__international = international

    def calculate_cost(self) -> float:
        return self.__base_cost + self.cost_International()

    def cost_International(self) -> float:
        if self.__international:
            return self.__declared_value * 0.25
        else:
            return 0

    # Métodos JSON
    def to_json(self) -> dict:
        return {
            "guide_number": self.getGuide_number(),
            "date": self.getDate().isoformat(),
            "description": self.getDescription(),
            "weight": self.getWeight(),
            "declared_value": self.getDeclared_value(),
            "international": self.getInternational(),
            "sender": {
                "name": self.getSender().get_name(),
                "department": self.getSender().get_department(),
                "phone": self.getSender().get_phones(),
            },
            "recipient": {
                "name": self.getRecipient().get_name(),
                "company": self.getRecipient().get_company(),
                "street": self.getRecipient().get_street(),
                "neighborhood": self.getRecipient().get_neighborhood(),
                "city": self.getRecipient().get_city(),
                "state": self.getRecipient().get_state(),
                "country": self.getRecipient().get_country(),
                "postal_code": self.getRecipient().get_postal_code(),
            },
            "base_cost": self.get_base_cost(),
        }

    @classmethod
    def from_json(cls, data):
        # Este método debe ser implementado en las clases derivadas
        raise NotImplementedError("Subclasses should implement this method.")
