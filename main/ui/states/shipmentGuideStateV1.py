import reflex as rx
from typing import Any
from datetime import date

# Importar controlador para crear guías
from main.server.controllers import guides_controller

# Clases para crear objetos de estado
from main.server.models.guide import Guide
from main.server.models.sender import Sender
from main.server.models.recipient import Recipient
from main.server.models.serviceType import ServiceType


class ShipmentGuideStateV1(rx.State):
    guide: Guide = Guide(
        guideNumber="000000",  # Ejemplo de número de guía
        date=date.today(),
        status="PENDING",  # Estado por defecto
        weight=0.0,  # Peso por defecto
        quantity=1,  # Cantidad por defecto
        declaredValue=0.0,  # Valor declarado por defecto
        serviceType=ServiceType(
            nameType="Paquete", weight=0.0, quantity=1, declared_value=0.0
        ),  # Tipo de servicio por defecto
        isInternational=False,  # Por defecto, no internacional
        sender=Sender(),  # Enviar un objeto Sender vacío o predeterminado
        recipient=Recipient(
            "", "", "", "", "", "", "", "", []
        ),  # Enviar un objeto Recipient vacío o predeterminado
    )

    def next_page(self):
        if self.current_page < 2:
            self.current_page += 1

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1

    def update_sender(self, field: str, value: str):
        if field == "name":
            self.sender.setName(value)
        elif field == "lastName":
            self.sender.setLastName(value)
        elif field == "department":
            self.sender.setDepartment(value)
        elif field == "phone":
            self.sender.setPhone(value)

    def build_sender(self):
        try:
            return self.sender.build()
        except ValueError as e:
            self.error_message = str(e)
            return None

    def update_recipient(self, field: str, value: Any):
        if field == "name":
            self.recipient.setName(value)
        elif field == "lastName":
            self.recipient.setLastName(value)
        elif field == "company":
            self.recipient.setCompany(value)
        elif field == "street":
            self.recipient.setStreet(value)
        elif field == "neighborhood":
            self.recipient.setNeighborhood(value)
        elif field == "city":
            self.recipient.setCity(value)
        elif field == "state":
            self.recipient.setState(value)
        elif field == "country":
            self.recipient.setCountry(value)
        elif field == "postalCode":
            self.recipient.setPostalCode(value)
        elif field == "phones":
            if isinstance(value, str):
                # If a single phone number is provided, add it to the list
                current_phones = self.recipient.getPhones()
                current_phones.append(value)
                self.recipient.setPhones(current_phones)
            elif isinstance(value, list):
                # If a list of phone numbers is provided, set it directly
                self.recipient.setPhones(value)

    def update_service_type(self, name_type: str):
        if self.weight > 0 and self.quantity > 0 and self.declared_value > 0:
            self.service_type = ServiceType(
                nameType=name_type,
                weight=self.weight,
                quantity=self.quantity,
                declared_value=self.declared_value,
                is_international=self.is_international,
            )

    def update_guide(self, field: str, value: Any):
        if not self.guide:
            self.guide = Guide("", date.today(), "", 0.0, 0.0, 0.0, False, 0.0)

        if field == "guideNumber":
            self.guide.setGuideNumber(value)
        elif field == "date":
            self.guide.setDate(value)
        elif field == "status":
            self.guide.setStatus(value)
        elif field == "weight":
            self.guide.setWeight(float(value))
        elif field == "quantity":
            self.guide.setQuantity(float(value))
        elif field == "declaredValue":
            self.guide.setDeclaredValue(float(value))
        elif field == "serviceType":
            self.guide.setServiceType(value)
        elif field == "isInternational":
            self.guide.setIsInternational(bool(value))
        elif field == "sender":
            self.guide.setSender(value)
        elif field == "recipient":
            self.guide.setRecipient(value)

    def update_weight(self, weight: float):
        self.weight = float(weight)
        self._update_service_type()

    def update_quantity(self, quantity: int):
        self.quantity = int(quantity)
        self._update_service_type()

    def update_declared_value(self, value: float):
        self.declared_value = float(value)
        self._update_service_type()

    def update_international(self, is_international: bool):
        self.is_international = bool(is_international)
        self._update_service_type()

    def _update_service_type(self):
        if self.service_type:
            self.update_service_type(self.service_type.nameType)

    @rx.var
    def calculated_cost(self) -> float:
        if self.service_type:
            return self.service_type.calculateCost()
        return 0.0

    @rx.var
    def is_service_type_complete(self) -> bool:
        return (
            self.service_type is not None
            and self.weight > 0
            and self.quantity > 0
            and self.declared_value > 0
        )

    @rx.var
    def is_sender_complete(self) -> bool:
        return bool(
            self.sender._Sender__name,
            self.sender._Sender__lastName,
            self.sender._Sender__department,
            self.sender._Sender__phone,
        )

    @rx.var
    def is_recipient_complete(self) -> bool:
        return all(
            [
                self.recipient.getName(),
                self.recipient.getLastName(),
                self.recipient.getStreet(),
                self.recipient.getCity(),
                self.recipient.getState(),
                self.recipient.getCountry(),
                self.recipient.getPhones(),
            ]
        )

    def build_and_save_guide(self):
        self.guide.sender = self.sender
        self.guide.recipient = self.recipient
        self.guide.service_type = self.service_type
        guides_controller.create_guide(self.guide.to_dict())
