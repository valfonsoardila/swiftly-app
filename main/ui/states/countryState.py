import reflex as rx
from typing import List, Dict

# Creacion de departamentos sino existen en la base de datos
from main.server.controllers.countrys_controller import check_and_create_countrys


class Countrystate(rx.State):
    contrys: List[Dict[str, str]] = []
    filtered_country: List[str] = []
    country_input: str = ""
    show_suggestions: bool = False

    async def on_load(self):
        self.contrys = (
            check_and_create_countrys()
        )  # Remove await if this function is not async
        return self.contrys

    def filter_countries(self, value: str):
        self.country_input = value
        if (
            value.strip()
        ):  # Comprueba si el input no está vacío después de quitar espacios en blanco
            self.filtered_country = [
                dept["name"]
                for dept in self.contrys
                if value.lower() in dept["name"].lower()
            ]
            self.show_suggestions = len(self.filtered_country) > 0
        else:
            self.filtered_country = []
            self.show_suggestions = False

    def set_country_input(self, city: str):
        self.country_input = city
        self.show_suggestions = False
