import reflex as rx
from typing import List, Dict
import json

# Creacion de departamentos sino existen en la base de datos
from main.server.controllers.countries_controller import check_and_create_countries


class CountriesState(rx.State):
    storage: List[Dict[str, str]] = rx.LocalStorage([], name="countries_data")
    contries: List[Dict[str, str]] = []
    filtered_country: List[str] = []
    country_input: str = ""
    show_suggestions: bool = False

    # Cargar paises de la base de datos a la aplicacion
    async def on_load(self):
        self.storage = json.dumps(check_and_create_countries())
        if storage := self.storage:
            self.contries = storage
            # prints de verificacion aqui
        return self.contries

    async def on_read_storage(self):
        self.contries = json.loads(self.storage)

    def filter_countries(self, value: str):
        self.country_input = value
        if (
            value.strip()
        ):  # Comprueba si el input no está vacío después de quitar espacios en blanco
            self.filtered_country = [
                dept["name"]
                for dept in self.contries
                if value.lower() in dept["name"].lower()
            ]
            self.show_suggestions = len(self.filtered_country) > 0
        else:
            self.filtered_country = []
            self.show_suggestions = False

    def set_country_input(self, city: str):
        self.country_input = city
        self.show_suggestions = False
