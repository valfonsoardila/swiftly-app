import reflex as rx
from typing import Any
from datetime import date
import asyncio

# Importar controlador para crear guías
from main.server.controllers import guides_controller

# Clases para crear objetos de estado
from main.server.models.v2.Guide import Guide
from main.server.models.v2.Box import Box
from main.server.models.v2.Envelope import Envelope
from main.server.models.v2.Package import Package
from main.ui.states.countriesState import CountriesState
from main.ui.states.deparmentState import DepartmentState


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
    recipient_city: str = DepartmentState.city_input
    recipient_state: str = ""
    recipient_country: str = CountriesState.country_input
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

    # Actualizar estado de la guía
    def update_recipient_city(self, city: str):
        self.recipient_city = city

    def update_recipient_country(self, country: str):
        self.recipient_country = country

    def update_is_international(self, is_international: bool):
        self.is_international = is_international

    def handle_sender_submit(self, form_data: dict):
        print("Datos del remitente capturados:", form_data)
        if self.validate_sender_data(form_data):
            self.sender_name = form_data.get("sender_name", "")
            self.sender_lastName = form_data.get("sender_lastName", "")
            self.sender_phone = form_data.get("sender_phone", "")
            self.sender_state = form_data.get("sender_state", "")
            self.sender_section_complete = True
        else:
            return rx.window_alert("Please fill in all fields in the sender section.")

    def validate_sender_data(self, form_data: dict) -> bool:
        required_fields = [
            "sender_name",
            "sender_lastName",
            "sender_phone",
            "sender_state",
        ]
        return all(form_data.get(field) for field in required_fields)

    def handle_recipient_submit(self, form_data: dict):
        print("Datos del destinatario capturados:", form_data)
        # Validate and update sender data
        if self.validate_recipient_data(form_data):
            # Update state variables
            self.recipient_name = form_data["recipient_name"]
            self.recipient_company = form_data["recipient_company"]
            self.recipient_lastName = form_data["recipient_lastName"]
            self.recipient_street = form_data["recipient_street"]
            self.recipient_neighborhood = form_data["recipient_neighborhood"]
            self.recipient_city = form_data["recipient_city"]
            self.recipient_state = form_data["recipient_state"]
            self.recipient_country = form_data["recipient_country"]
            self.recipient_postalCode = form_data["recipient_postalCode"]
            self.recipient_phone = form_data["recipient_phone"]
            # ... (update other recipient fields) ...
            self.recipient_section_complete = True
        else:
            return rx.window_alert(
                "Please fill in all fields in the recipient section."
            )

    def validate_recipient_data(self, form_data: dict) -> bool:
        required_fields = [
            "recipient_name",
            "recipient_company",
            "recipient_lastName",
            "recipient_street",
            "recipient_neighborhood",
            "recipient_city",
            "recipient_state",
            "recipient_country",
            "recipient_postalCode",
            "recipient_phone",
        ]
        return all(form_data.get(field) for field in required_fields)

    def handle_package_submit(self, form_data: dict):
        print("Datos del paquete capturados:", form_data)
        # Validate and update sender data
        if self.validate_package_data(form_data):
            # Update state variables
            self.service_type = form_data["service_type"]
            self.weight = form_data["weight"]
            self.quantity = form_data["quantity"]
            self.declared_value = form_data["declared_value"]
            self.is_international = form_data["is_international"].lower() == "true"
            # ... (update other package fields) ...
            self.package_section_complete = True
        else:
            return rx.window_alert("Please fill in all fields in the package section.")

    def validate_package_data(self, form_data: dict) -> bool:
        required_fields = ["service_type", "weight", "quantity", "declared_value"]
        return all(form_data.get(field) for field in required_fields)

    @rx.background
    async def on_signup_button_click(self):
        guide_data = (
            {
                "sender_name": self.sender_name,
                "sender_lastName": self.sender_lastName,
                "sender_phone": self.sender_phone,
                "sender_state": self.sender_state,
                "recipient_name": self.recipient_name,
                "recipient_lastName": self.recipient_lastName,
                "recipient_company": self.recipient_company,
                "recipient_street": self.recipient_street,
                "recipient_neighborhood": self.recipient_neighborhood,
                "recipient_city": self.recipient_city,
                "recipient_state": self.recipient_state,
                "recipient_country": self.recipient_country,
                "recipient_postalCode": self.recipient_postalCode,
                "recipient_phone": self.recipient_phone,
                "service_type": self.service_type,
                "weight": self.weight,
                "quantity": self.quantity,
                "declared_value": self.declared_value,
                "is_international": self.is_international,
            },
        )
        # VAlidar si todos los campos están completos
        if (
            self.sender_section_complete
            and self.recipient_section_complete
            and self.package_section_complete
        ):
            result = guides_controller.create_guide(guide_data)
            if result:
                yield rx.toast.success(
                    "Guide created successfully! Redirecting to app...",
                    duration=5000,
                )
                await asyncio.sleep(3)  # Espera 5 segundos
                yield rx.redirect("/app")
            else:
                yield rx.toast.error(
                    "Guide creation failed. Please try again.", duration=5000
                )
        else:
            yield rx.toast.error(
                "Please fill all the fields.",
                duration=5000,
            )
