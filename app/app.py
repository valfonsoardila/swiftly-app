import reflex as rx
from rxconfig import config
from app.views.auth.login_view import login_view
from app.views.auth.signup_view import signup_view
from app.views.dashboard.home_view import home_view


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Página de bienvenida (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Victory Docs"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
app.add_page(login_view, route="/login")  # Añadir la vista de inicio de sesión
app.add_page(signup_view, route="/signup")  # Añadir la vista de registro
app.add_page(home_view, route="/dashboard")  # Añadir la vista del dashboard
