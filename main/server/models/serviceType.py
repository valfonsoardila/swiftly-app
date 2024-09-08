from abc import ABC, abstractmethod


# Interfaz para el Strategy
class CostStrategy(ABC):
    @abstractmethod
    def calculateCost(
        self, baseRate: float, weight: float, isInternational: bool
    ) -> float:
        pass


# Estrategia para LETTER
class LetterCostStrategy(CostStrategy):
    def calculateCost(
        self, baseRate: float, weight: float, isInternational: bool
    ) -> float:
        cost = baseRate + 10000.0  # Documento adicional
        if isInternational:
            cost += cost * 0.25
        return cost


# Estrategia para PACKAGE
class PackageCostStrategy(CostStrategy):
    def calculateCost(
        self, baseRate: float, weight: float, isInternational: bool
    ) -> float:
        cost = baseRate * weight
        if isInternational:
            cost += cost * 0.25
        return cost


# Estrategia para BOX
class BoxCostStrategy(CostStrategy):
    def calculateCost(
        self, baseRate: float, weight: float, isInternational: bool
    ) -> float:
        cost = baseRate * weight + 25000.0  # Caja adicional
        if isInternational:
            cost += cost * 0.25
        return cost


# Clase principal ServiceType
class ServiceType:
    def __init__(self, nameType: str, strategy: CostStrategy):
        self.__nameType = nameType
        self.__baseRate = 5000.0
        self.__strategy = strategy

    def calculateCost(self, weight: float, isInternational: bool = False) -> float:
        return self.__strategy.calculateCost(self.__baseRate, weight, isInternational)
