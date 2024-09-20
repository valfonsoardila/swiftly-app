import reflex as rx
from rxconfig import config
from main.ui.pages.intro.intro_view import intro_view
from main.ui.pages.auth.login_view import login_view
from main.ui.pages.auth.signup_view import signup_view
from main.ui.pages.auth.forgot_password_view import forgot_password_view
from main.ui.pages.auth.reset_password_view import reset_password_view
from main.ui.pages.app.app_view import app_view
from main.ui.pages.app.views.dashboard_view import dashboard_view
from main.ui.pages.app.views.guides_view import guides_view
from main.ui.pages.app.views.settings_view import settings_view
from main.ui.pages.app.views.clients_view import clients_view
from main.ui.pages.tracking.tracking_view import tracking_view

# inicializamos los estados
from main.ui.states.deparmentState import DepartmentState
from main.ui.states.countriesState import CountriesState

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
        country_state = await self.get_state(CountriesState)
        self.countries = await country_state.on_load()


@rx.page(on_load=InitialState.on_load, title="Swiftly App")
def index() -> rx.Component:
    return intro_view()


app = rx.App()
app.add_page(index, title="Swiftly App")
