import reflex as rx
from main.ui.states.userState import UserState
import base64


class StateImageAvatar(rx.State):
    image_data: str = (
        ""  # Variable para almacenar los datos de la imagen como una cadena codificada
    )
    image: str = "/ico/avatar.png"

    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            # Leer el archivo como binarios
            upload_data = await file.read()

            # Codificar los datos binarios en una cadena base64
            self.image_data = base64.b64encode(upload_data).decode("utf-8")

            # Si necesitas actualizar la ruta de la imagen (opcional)
            self.image = f"data:image/png;base64,{self.image_data}"


@rx.page(route="/signup", title="Sign Up")
def signup_view() -> rx.Component:
    return rx.hstack(
        rx.box(  # Div adicional para el fondo con opacidad
            style={
                "position": "absolute",
                "top": "0",
                "left": "0",
                "right": "0",
                "bottom": "0",
                "background": "url('/design/diseño-b.png')",
                "backgroundSize": "15% auto",
                "backgroundPosition": "center",
                "backgroundRepeat": "repeat",
                "backgroundAttachment": "fixed",
                "opacity": "0.3",  # Solo la imagen de fondo tiene opacidad
                "zIndex": "0",  # Asegura que esté detrás del contenido
            },
        ),
        rx.flex(
            rx.hstack(
                rx.flex(
                    rx.card(
                        rx.vstack(
                            rx.flex(
                                rx.center(
                                    rx.image(
                                        src="/ico/logo.png",
                                        width="40%",
                                        border_radius="25%",
                                    ),
                                    rx.heading(
                                        "Create an account",
                                        size="6",
                                        as_="h2",
                                        width="100%",
                                        align="center",
                                        style={
                                            "color": "black",
                                            "fontWeight": "bold",
                                        },
                                    ),
                                    rx.hstack(
                                        rx.text(
                                            "Already registered?",
                                            size="3",
                                            text_align="center",
                                            style={
                                                "color": "black",
                                            },
                                        ),
                                        rx.link(
                                            "Sign in",
                                            size="3",
                                            text_align="center",
                                            color="black",
                                            underline="always",
                                            style={
                                                "color": "black",
                                                "fontWeight": "bold",
                                            },
                                            href="/login",  # Cambio de href para apuntar al login
                                        ),
                                        spacing="2",
                                        opacity="0.8",
                                        width="100%",
                                        justify="center",
                                        align="center",
                                    ),
                                    justify="center",
                                    align="center",
                                    direction="column",
                                ),
                                justify="start",
                                direction="column",
                                spacing="4",
                                width="100%",
                            ),
                            rx.vstack(
                                circle_avatar(
                                    image=StateImageAvatar.image,
                                    size="150px",
                                    on_upload=StateImageAvatar.handle_upload(
                                        rx.upload_files(upload_id="avatar_upload")
                                    ),
                                ),
                                align="center",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text(
                                    "Username",
                                    size="3",
                                    weight="medium",
                                    text_align="left",
                                    width="100%",
                                    style={
                                        "color": "black",
                                        "fontWeight": "bold",
                                    },
                                ),
                                rx.input(
                                    rx.input.slot(rx.icon("user")),
                                    placeholder="Enter your username",
                                    type="email",
                                    size="3",
                                    width="100%",
                                    on_change=UserState.set_username,
                                    color_scheme="orange",
                                    variant="surface",
                                    radius="full",
                                    required=True,
                                ),
                                spacing="2",
                                justify="start",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text(
                                    "Email address",
                                    size="3",
                                    weight="medium",
                                    text_align="left",
                                    width="100%",
                                    style={
                                        "color": "black",
                                        "fontWeight": "bold",
                                    },
                                ),
                                rx.input(
                                    rx.input.slot(rx.icon("user")),
                                    placeholder="user@reflex.dev",
                                    type="username",
                                    size="3",
                                    width="100%",
                                    on_change=UserState.set_email,
                                    color_scheme="orange",
                                    variant="surface",
                                    radius="full",
                                    required=True,
                                ),
                                spacing="2",
                                justify="start",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text(
                                    "Password",
                                    size="3",
                                    weight="medium",
                                    style={
                                        "color": "black",
                                        "fontWeight": "bold",
                                    },
                                ),
                                rx.input(
                                    rx.input.slot(rx.icon("lock")),
                                    placeholder="Enter your password",
                                    type="password",
                                    size="3",
                                    width="100%",
                                    on_change=UserState.set_password,
                                    color_scheme="orange",
                                    variant="surface",
                                    radius="full",
                                    required=True,
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text(
                                    "Confirm Password",
                                    size="3",
                                    weight="medium",
                                    style={
                                        "color": "black",
                                        "fontWeight": "bold",
                                    },
                                ),
                                rx.input(
                                    rx.input.slot(rx.icon("lock")),
                                    placeholder="Confirm your password",
                                    type="password",
                                    size="3",
                                    width="100%",
                                    on_change=UserState.set_password_confirm,
                                    color_scheme="orange",
                                    variant="surface",
                                    radius="full",
                                    required=True,
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            rx.box(
                                rx.checkbox(
                                    rx.text(
                                        "Agree to Terms and Conditions",
                                        size="3",
                                        weight="normal",
                                        style={
                                            "color": "black",
                                        },
                                    ),
                                    default_checked=True,
                                    spacing="2",
                                    color_scheme="orange",
                                    on_change=UserState.set_agree,
                                    _hover={"cursor": "pointer"},
                                ),
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    "Register",
                                    size="large",
                                    width="100%",
                                    style={
                                        "color": "white",
                                        "backgroundColor": "black",
                                        "border": "none",
                                        "padding": "1em 2em",
                                        "borderRadius": "1em",
                                        "cursor": "pointer",
                                        "fontSize": "20px",
                                    },
                                    on_click=UserState.on_signup_button_click,
                                ),
                                _hover={
                                    "backgroundColor": "#333333",
                                    "transform": "scale(1.05)",
                                    "transition": "transform 0.2s ease",
                                },
                                width="100%",
                            ),
                            spacing="6",
                            width="100%",
                        ),
                        size="4",
                        max_width="28em",
                        width="100%",
                        style={
                            "background": "linear-gradient(135deg, rgba(255,255,255, 0.42) 0%, rgba(224,224,224, 0.24) 100%)",
                        },
                    ),
                    filter="drop-shadow(0px 0px 10px rgba(0,0,0,0.1))",
                    justify="center",  # Centrado horizontal
                    align="center",  # Centrado vertical
                    style={
                        "position": "relative",
                        "height": "100%",
                        "width": "100%",
                    },
                ),
                justify="center",  # Centrado horizontal
                align="center",  # Centrado vertical
                height="100%",
                width="90%",
            ),
            align="center",
            justify="center",
            height="100%",
            width="100%",
        ),
        title="Container-signup",
        background="linear-gradient(45deg, rgba(255,193,7) 0%, rgba(255,152,0) 25%, rgba(255,113,34) 50%, rgba(242, 116,5) 100%)",
        width="-webkit-fill-available",  # Ancho del contenedor acoplado con responsive design
        height="100vh",
        style={
            "position": "relative",  # Para que todo el contenido esté sobre el fondo
            "height": "100%",
            "width": "100%",
        },
    )


def circle_avatar(image: str, size: str = "3em", on_upload=None) -> rx.Component:
    return rx.box(
        rx.avatar(
            src=image,
            size="9",
            fallback="",
        ),
        rx.upload(
            rx.button(
                rx.icon("camera"),
                position="absolute",
                top="50%",
                left="50%",
                transform="translate(-50%, -50%)",
                background_color="rgba(0, 0, 0, 0.5)",
                color="white",
                border_radius="50%",
                style={
                    "height": "30%",
                    "width": "30%",
                },
                _hover={
                    "background": "rgba(0, 0, 0, 0.7)",
                    "cursor": "pointer",
                },
            ),
            id="avatar_upload",
            multiple=False,
            accept={
                "image/png": [".png"],
                "image/jpeg": [".jpg", ".jpeg"],
                "image/gif": [".gif"],
            },
            max_files=1,
            on_drop=on_upload,
        ),
        style={
            "border": "2px solid rgba(0, 0, 0, 0.4)",
            "borderRadius": "50%",
            "overflow": "hidden",
            "position": "relative",
            "width": size,
            "height": size,
        },
        position="relative",
        width=size,
        height=size,
    )
