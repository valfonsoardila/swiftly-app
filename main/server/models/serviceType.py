# Patron de diseño Factory Method
class ServiceType:
    def __init__(
        self,
        nameType: str,  # Nombre del tipo de servicio (Caja, Paquete, Sobre)
        weight: float,
        quantity: int,
        declared_value: float,
        is_international: bool = False,
    ):
        self.nameType = nameType
        self.weight = weight
        self.quantity = quantity
        self.declared_value = declared_value
        self.is_international = is_international
        self.baseRate = 5000.0

    # Función para calcular el costo basado en el tipo de servicio
    def calculateCost(self) -> float:
        cost = 0.0

        # Lógica para calcular el costo según el tipo de servicio
        if self.nameType == "Caja":
            cost = self.baseRate * self.weight + 25000.0  # Caja adicional
        elif self.nameType == "Paquete":
            cost = self.baseRate * self.weight
        elif self.nameType == "Sobre":
            cost = self.baseRate + 10000.0  # Documento adicional

        # Si es internacional, se añade un 25% al costo
        if self.is_international:
            cost += cost * 0.25

        # Multiplicar el costo por la cantidad de paquetes
        total_cost = cost * self.quantity

        return total_cost
