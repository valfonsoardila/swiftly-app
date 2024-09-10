from datetime import date
from typing import Optional
from main.server.models.v1.Recipient import Recipient
from main.server.models.v1.Sender import Sender
from main.server.models.v1.ServiceType import ServiceType


# Patron de diseño Active Record
class Guide:
    def __init__(
        self,
        guideNumber: str,
        date: date,
        status: str,
        weight: float,
        quantity: float,
        declaredValue: float,
        serviceType: ServiceType,
        isInternational: bool,
        sender: Sender,
        recipient: Recipient,
    ):
        self.__guideNumber = guideNumber
        self.__date = date
        self.__status = status
        self.__weight = weight
        self.__quantity = quantity
        self.__declaredValue = declaredValue
        self.__serviceType = serviceType
        self.__isInternational = isInternational
        self.__deliveryCost = self.calculateDeliveryCost()
        self.__recipient = recipient
        self.__sender = sender

    def getGuideNumber(self) -> str:
        return self.__guideNumber

    def setGuideNumber(self, guideNumber: str):
        self.__guideNumber = guideNumber

    def getDate(self) -> date:
        return self.__date

    def setDate(self, date: date):
        self.__date = date

    def getStatus(self) -> str:
        return self.__status

    def setStatus(self, status: str):
        self.__status = status

    def getWeight(self) -> float:
        return self.__weight

    def setWeight(self, weight: float):
        self.__weight = weight

    def getQuantity(self) -> float:
        return self.__quantity

    def setQuantity(self, quantity: float):
        self.__quantity = quantity

    def getDeclaredValue(self) -> float:
        return self.__declaredValue

    def setDeclaredValue(self, declaredValue: float):
        self.__declaredValue = declaredValue

    def getServiceType(self) -> ServiceType:
        return self.__serviceType

    def setServiceType(self, serviceType: ServiceType):
        self.__serviceType = serviceType

    def getIsInternational(self) -> bool:
        return self.__isInternational

    def setIsInternational(self, isInternational: bool):
        self.__isInternational = isInternational

    def getDeliveryCost(self) -> float:
        return self.__deliveryCost

    def getRecipient(self) -> Optional[Recipient]:
        return self.__recipient

    def setRecipient(self, recipient: Recipient):
        self.__recipient = recipient

    def getSender(self) -> Optional[Sender]:
        return self.__sender

    def setSender(self, sender: Sender):
        self.__sender = sender

    def calculateDeliveryCost(self) -> float:
        return self.__serviceType.calculateCost(
            self.__weight, self.__quantity, self.__isInternational
        )

    def deliverGuide(self):
        self.__status = "COMPLETED"

    def toJson(self):
        return {
            "guide_number": self.__guide_number,
            "date": self.__date.isoformat(),
            "status": self.__status,
            "weight": self.__weight,
            "quantity": self.__quantity,
            "declared_value": self.__declared_value,
            "is_international": self.__is_international,
            "delivery_cost": self.__delivery_cost,
            "recipient_id": self.__recipient_id,
            "sender_id": self.__sender_id,
            "service_type_id": self.__service_type_id,
        }

    @staticmethod
    def fromJson(data):
        guide = Guide(
            data.get("guide_number"),
            data.get("date"),
            data.get("status"),
            data.get("weight"),
            data.get("quantity"),
            data.get("declared_value"),
            data.get("is_international"),
            data.get("delivery_cost"),
            data.get("recipient_id"),
            data.get("sender_id"),
            data.get("service_type_id"),
        )
        return guide
