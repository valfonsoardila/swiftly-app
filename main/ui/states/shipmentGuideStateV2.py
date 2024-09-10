import reflex as rx
from typing import Any
from datetime import date

# Importar controlador para crear guías
from main.server.controllers import guides_controller

# Clases para crear objetos de estado
from main.server.models.v2.Guide import Guide
from main.server.models.v2.Box import Box
from main.server.models.v2.Envelope import Envelope
from main.server.models.v2.Package import Package


class ShipmentGuideStateV2(rx.State):
    # Sender fields
    sender_name: str = ""
    sender_lastName: str = ""
    sender_state: str = ""
    sender_phone: str = ""

    # Recipient fields
    recipient_name: str = ""
    recipient_lastName: str = ""
    recipient_company: str = ""
    recipient_street: str = ""
    recipient_neighborhood: str = ""
    recipient_city: str = ""
    recipient_state: str = ""
    recipient_country: str = ""
    recipient_postalCode: str = ""
    recipient_phone: str = ""

    # Package fields
    service_type: str = ""
    weight: float = 0.0
    quantity: int = 0
    declared_value: float = 0.0
    is_international: bool = False

    # Section completion flags
    sender_section_complete: bool = False
    recipient_section_complete: bool = False
    package_section_complete: bool = False

    def update_recipient_city(self, city: str):
        self.recipient_city = city

    def update_recipient_country(self, country: str):
        self.recipient_country = country

    @rx.var
    def all_sections_complete(self) -> bool:
        return all(
            [
                self.sender_section_complete,
                self.recipient_section_complete,
                self.package_section_complete,
            ]
        )
