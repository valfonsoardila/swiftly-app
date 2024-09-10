import reflex as rx
from typing import List, Dict

# Creacion de departamentos sino existen en la base de datos
from main.server.controllers.departments_controller import check_and_create_departments


class DepartmentState(rx.State):
    departments: List[Dict[str, str]] = []
    filtered_cities: List[str] = []
    city_input: str = ""
    show_suggestions: bool = False

    async def on_load(self):
        self.departments = (
            check_and_create_departments()
        )  # Remove await if this function is not async
        return self.departments

    def filter_cities(self, value: str):
        self.city_input = value
        if (
            value.strip()
        ):  # Comprueba si el input no está vacío después de quitar espacios en blanco
            self.filtered_cities = [
                dept["capital"]
                for dept in self.departments
                if value.lower() in dept["capital"].lower()
            ]
            self.show_suggestions = len(self.filtered_cities) > 0
        else:
            self.filtered_cities = []
            self.show_suggestions = False

    def set_city_input(self, city: str):
        self.city_input = city
        self.show_suggestions = False