import reflex as rx
from rxconfig import config
from app.views.auth.login_view import login_view
from app.views.auth.signup_view import signup_view
from app.views.dashboard.home_view import home_view
from app.views.anim.animation_view import animation_view


class State(rx.State):
    # manejar el estado de la aplicación
    is_logged_in: bool = False


def index() -> rx.Component:
    return animation_view()


app = rx.App()
app.add_page(index)
app.add_page(login_view, route="/login")  # Añadir la vista de inicio de sesión
app.add_page(signup_view, route="/signup")  # Añadir la vista de registro
app.add_page(home_view, route="/dashboard")  # Añadir la vista del dashboard
