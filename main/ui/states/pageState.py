import reflex as rx


class StatePage(rx.State):
    current_route: str = "dashboard"

    def set_route(self, route: str):
        self.current_route = route

    def logout(self):
        # Aquí puedes agregar lógica adicional para cerrar la sesión si es necesario
        return rx.redirect("/login")
