import reflex as rx
from typing import Any
from datetime import date

# Importar controlador para crear guías
from main.server.controllers import guides_controller

# Clases para crear objetos de estado
from main.server.models.v2.Guide import Guide


class ShipmentGuideStateV2(rx.State):
    pass
