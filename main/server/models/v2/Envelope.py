from datetime import datetime
from .Guide import Guide
import json
from .GuideStatus import GuideStatus
from .Sender import Sender
from .Recipient import Recipient


class Envelope(Guide):
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
        envelope_fee: float,
    ):
        super().__init__(
            guide_number,
            date,
            description,
            weight,
            declared_value,
            international,
            sender_name,
            sender_department,
            sender_phone,
            recipient_name,
            recipient_company,
            recipient_street,
            recipient_neighborhood,
            recipient_city,
            recipient_state,
            recipient_country,
            recipient_postal_code,
        )
        self.__envelope_fee = envelope_fee

    # Getters y setters para atributos heredados
    def get_guide_number(self) -> int:
        return super().getGuide_number()

    def set_guide_number(self, guide_number: int):
        super().setGuide_number(guide_number)

    def get_date(self) -> datetime:
        return super().getDate()

    def set_date(self, date: datetime):
        super().setDate(date)

    def get_description(self) -> str:
        return super().getDescription()

    def set_description(self, description: str):
        super().setDescription(description)

    def get_weight(self) -> float:
        return super().getWeight()

    def set_weight(self, weight: float):
        super().setWeight(weight)

    def get_declared_value(self) -> float:
        return super().getDeclared_value()

    def set_declared_value(self, declared_value: float):
        super().setDeclared_value(declared_value)

    def is_international(self) -> bool:
        return super().getInternational()

    def set_international(self, international: bool):
        super().setInternational(international)

    def get_status(self):
        return super().getStatus()

    def get_recipient(self):
        return super().getRecipient()

    def get_sender(self):
        return super().getSender()

    def get_envelope_fee(self) -> float:
        return self.__envelope_fee

    def set_envelope_fee(self, envelope_fee: float):
        self.__envelope_fee = envelope_fee

    def calculate_cost(self) -> float:
        return super().calculate_cost() + self.__envelope_fee

    # Métodos JSON
    def to_json(self):
        return {
            "guide_number": self.get_guide_number(),
            "date": self.get_date().isoformat(),
            "description": self.get_description(),
            "weight": self.get_weight(),
            "declared_value": self.get_declared_value(),
            "international": self.is_international(),
            "envelope_fee": self.get_envelope_fee(),
            "type": "envelope",
            "sender": self.get_sender().to_json(),
            "recipient": self.get_recipient().to_json(),
            "status": self.get_status().to_json(),
        }

    @classmethod
    def from_json(cls, data):
        guide_number = data.get("guide_number")
        date = datetime.fromisoformat(data.get("date"))
        description = data.get("description")
        weight = data.get("weight")
        declared_value = data.get("declared_value")
        international = data.get("international")
        envelope_fee = data.get("envelope_fee")
        sender_data = data.get("sender")
        recipient_data = data.get("recipient")
        status_data = data.get("status")

        # Crear instancias de Sender y Recipient desde JSON
        sender = Sender.from_json(sender_data)
        recipient = Recipient.from_json(recipient_data)
        status = GuideStatus.from_json(status_data)

        # Crear instancia de Envelope
        envelope = cls(
            guide_number,
            date,
            description,
            weight,
            declared_value,
            international,
            sender.get_name(),
            sender.get_department(),
            sender.get_phones(),
            recipient.get_name(),
            recipient.get_company(),
            recipient.get_street(),
            recipient.get_neighborhood(),
            recipient.get_city(),
            recipient.get_state(),
            recipient.get_country(),
            recipient.get_postal_code(),
            envelope_fee,
        )
        return envelope
