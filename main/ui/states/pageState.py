import reflex as rx


class StatePage(rx.State):
    current_route: str = "dashboard"
    content_spanish_labels = {
        "dashboard": "Dashboard",
        "guides": "Guías",
        "shipping": "Envíos",
        "clients": "Clientes",
        "settings": "Configuración",
    }
    labael_component_route: str = content_spanish_labels[current_route].capitalize()

    def set_route(self, route: str):
        self.current_route = route
        self.labael_component_route = self.content_spanish_labels[route].capitalize()

    def logout(self):
        # Aquí puedes agregar lógica adicional para cerrar la sesión si es necesario
        return rx.redirect("/login")
