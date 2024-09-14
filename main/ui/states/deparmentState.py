import reflex as rx
from typing import List, Dict
import json

# Creacion de departamentos sino existen en la base de datos
from main.server.controllers.departments_controller import check_and_create_departments


class DepartmentState(rx.State):
    storage: List[Dict[str, str]] = rx.LocalStorage([], name="department_state")
    departments: List[Dict[str, str]] = []
    filtered_cities: List[str] = []
    city_input: str = ""
    show_suggestions: bool = False

    # Cargar departamentos de la base de datos a la aplicacion
    async def on_load(self):
        self.storage = json.dumps(check_and_create_departments())
        if storage := self.storage:
            self.departments = storage
            # prints de verificacion aqui
        return self.departments

    async def on_read_storage(self):
        self.departments = json.loads(self.storage)

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
