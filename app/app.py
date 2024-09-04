import reflex as rx
from rxconfig import config
from app.views.intro.intro_view import intro_view
from app.views.auth.login_view import login_view
from app.views.auth.signup_view import signup_view
from app.views.auth.forgot_password_view import forgot_password_view
from app.views.auth.reset_password_view import reset_password_view


class State(rx.State):
    # manejar el estado de la aplicación
    is_logged_in: bool = False


def index() -> rx.Component:
    return intro_view()


app = rx.App()
app.add_page(index)
