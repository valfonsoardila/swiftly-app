import reflex as rx
from main.server.controllers.user_controller import create_user, read_user
import asyncio
import base64
import json


class UserState(rx.State):
    username: str = ""
    email: str = ""
    password: str = ""
    password_confirm: str = ""
    agree: bool = False
    logged_user: dict = rx.LocalStorage({}, name="user_data")
    image_data: str = (
        ""  # Variable para almacenar los datos de la imagen como una cadena codificada
    )
    image: str = "/ico/avatar.png"

    async def handle_upload_image_profile(self, files: list[rx.UploadFile]):
        for file in files:
            # Leer el archivo como binarios
            upload_data = await file.read()

            # Codificar los datos binarios en una cadena base64
            self.image_data = base64.b64encode(upload_data).decode("utf-8")

            # Si necesitas actualizar la ruta de la imagen (opcional)
            self.image = f"data:image/png;base64,{self.image_data}"

    @rx.background
    async def on_signup_button_click(self):
        user_data = {
            "image": self.image_data,
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
                yield rx.redirect("/app")
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

    # accesores
    @rx.var
    def load_user_email(self) -> str:
        try:
            user = json.loads(self.logged_user)
            return user.get(
                "email", ""
            )  # Devuelve el email del usuario o una cadena vacía
        except json.JSONDecodeError:
            return ""

    @rx.var
    def load_user_username(self) -> str:
        try:
            user = json.loads(self.logged_user)
            return user.get(
                "username", ""
            )  # Devuelve el username del usuario o una cadena vacía
        except json.JSONDecodeError:
            return ""

    @rx.var
    def load_user_image(self) -> str:
        try:
            user = json.loads(self.logged_user)

            image = user.get(
                "image", ""
            )  # Devuelve el username del usuario o una cadena vacía

            # convertir la cadena a un formato de imagen
            return f"data:image/png;base64,{image}"
        except json.JSONDecodeError:
            return ""
