from typing import Optional

class ServiceType:
    def __init__(self, nameType: str):
        self.__nameType = nameType
        self.__baseRate = 5000.0  # Valor base de liquidación
        self.__additionalDocumentRate = 10000.0
        self.__additionalBoxRate = 25000.0
        self.__internationalSurcharge = 0.25  # 25% recargo internacional

    def getNameType(self) -> str:
        return self.__nameType

    def setNameType(self, nameType: str):
        self.__nameType = nameType

    def getBaseRate(self) -> float:
        return self.__baseRate

    def setBaseRate(self, baseRate: float):
        self.__baseRate = baseRate

    def getAdditionalDocumentRate(self) -> float:
        return self.__additionalDocumentRate

    def setAdditionalDocumentRate(self, additionalDocumentRate: float):
        self.__additionalDocumentRate = additionalDocumentRate

    def getAdditionalBoxRate(self) -> float:
        return self.__additionalBoxRate

    def setAdditionalBoxRate(self, additionalBoxRate: float):
        self.__additionalBoxRate = additionalBoxRate

    def getInternationalSurcharge(self) -> float:
        return self.__internationalSurcharge

    def setInternationalSurcharge(self, internationalSurcharge: float):
        self.__internationalSurcharge = internationalSurcharge

    def calculateCost(self, weight: float, volume: Optional[float] = 0.0, isInternational: bool = False) -> float:
        if self.__nameType == 'LETTER':
            cost = self.__baseRate + self.__additionalDocumentRate
        elif self.__nameType == 'PACKAGE':
            cost = self.__baseRate * weight
        elif self.__nameType == 'BOX':
            cost = self.__baseRate * weight + self.__additionalBoxRate
        else:
            raise ValueError(f"Unknown service type: {self.__nameType}")

        if isInternational:
            cost += cost * self.__internationalSurcharge

        return cost

    def toJson(self):
        return {
            "name_type": self.__name_type,
            "weight": self.__weight,
            "volume": self.__volume
        }
    
    @staticmethod
    def fromJson(data):
        service_type = ServiceType(
            data.get('name_type'),
            data.get('weight'),
            data.get('volume')
        )
        return service_type
