import reflex as rx
from app.server.controllers.user_controller import create_user,read_user
import asyncio
import json


class UserState(rx.State):
    username: str = ""
    email: str = ""
    password: str = ""
    password_confirm: str = ""
    agree: bool = False
    logged_user: dict = rx.LocalStorage({}, name="user_data")

    @rx.background
    async def on_signup_button_click(self):
        user_data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }
        if self.password == self.password_confirm and self.password:
            result = create_user(user_data)
            if result:
                yield rx.toast.success(
                    "Registration successful! Redirecting to login...",
                    duration=5000,
                )
                await asyncio.sleep(3)  # Espera 5 segundos
                yield rx.redirect("/login")
            else:
                yield rx.toast.error(
                    "Registration failed. Please try again.", duration=5000
                )
        else:
            yield rx.toast.error(
                "Passwords do not match. Please try again.",
                duration=5000,
            )

    @rx.background
    async def on_login_button_click(self):
        user_data = {
            "email": self.email,
            "password": self.password,
        }
        if self.email != "" and self.password != "":
            result = read_user(
                user_data["email"]
            )  # hago la peticion a la base de datos
            if result["password"] == user_data["password"]:
                async with self:
                    # guardar con el nombre user_data
                    self.logged_user = json.dumps(
                        result
                    )  # Convierte el diccionario a JSON string
                yield rx.toast.success(
                    "Login successful. Redirecting...",
                    duration=3000,
                )
                await asyncio.sleep(3)
                yield rx.redirect("/dashboard")
            elif result["password"] != user_data["password"]:
                yield rx.toast.error(
                    "Invalid password. Please try again.",
                    duration=5000,
                )
            elif result["email"] != user_data["email"]:
                yield rx.toast.error(
                    "Invalid email. Please try again.",
                    duration=5000,
                )
        else:
            yield rx.toast.error(
                "Please fill all the fields.",
                duration=5000,
            )

    @rx.var
    def load_user(self) -> str:
        try:
            user = json.loads(self.logged_user)
            return user.get(
                "email", ""
            )  # Devuelve el email del usuario o una cadena vacía
        except json.JSONDecodeError:
            return ""
