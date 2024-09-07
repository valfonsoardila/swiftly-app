import reflex as rx
from rxconfig import config
from main.ui.views.intro.intro_view import intro_view
from main.ui.views.auth.login_view import login_view
from main.ui.views.auth.signup_view import signup_view
from main.ui.views.auth.forgot_password_view import forgot_password_view
from main.ui.views.auth.reset_password_view import reset_password_view
from main.ui.views.app.app_view import app_view
from main.ui.views.app.modules.dashboard_view import dashboard_view
from main.ui.views.app.modules.guides_view import guides_view
from main.ui.views.app.modules.settings_view import settings_view
from main.ui.views.app.modules.clients_view import clients_view
from main.ui.views.tracking.tracking_view import tracking_view

# inicializo el servicio de firebase
from main.server.api.firebase.firebase_config import Firebase_Config

# Inicializar Firebase una vez
firebase_service = Firebase_Config()
# Obtener la instancia de la base de datos
db = firebase_service.get_db()


class State(rx.State):
    # manejar el estado de la aplicación
    is_logged_in: bool = False


def index() -> rx.Component:
    return intro_view()


app = rx.App()
app.add_page(index, title="Swiftly App")
