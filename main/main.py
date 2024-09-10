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

# inicializamos los estados
from main.ui.states.deparmentState import DepartmentState
from main.ui.states.countryState import Countrystate

# inicializo el servicio de firebase
from main.server.api.firebase.firebase_config import Firebase_Config

# Inicializar Firebase una vez
firebase_service = Firebase_Config()


class InitialState(rx.State):
    departments: list = []
    countries: list = []

    async def on_load(self):
        # Load departments
        department_state = await self.get_state(DepartmentState)
        self.departments = await department_state.on_load()

        # Load countries
        country_state = await self.get_state(Countrystate)
        self.countries = await country_state.on_load()


@rx.page(on_load=InitialState.on_load, title="Swiftly App")
def index() -> rx.Component:
    return intro_view()


app = rx.App()
app.add_page(index, title="Swiftly App")
