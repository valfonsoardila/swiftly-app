import reflex as rx


@rx.page(route="/forgot-password", title="Forgot Password")
def forgot_password_view() -> rx.Component:
    return rx.hstack(
        rx.box(  # Div adicional para el fondo con opacidad
            style={
                "position": "absolute",
                "top": "0",
                "left": "0",
                "right": "0",
                "bottom": "0",
                "background": "url('/diseño-b.png')",
                "backgroundSize": "15% auto",
                "backgroundPosition": "center",
                "backgroundRepeat": "repeat",
                "backgroundAttachment": "fixed",
                "opacity": "0.3",  # Solo la imagen de fondo tiene opacidad
                "zIndex": "0",  # Asegura que esté detrás del contenido
            },
        ),
        rx.flex(  # Contenido principal
            rx.hstack(
                rx.flex(
                    rx.card(
                        rx.vstack(
                            rx.flex(
                                rx.center(
                                    rx.image(
                                        src="/logo.png",
                                        width="40%",
                                        border_radius="25%",
                                    ),
                                    rx.heading(
                                        "Recover Your Password",
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
                                            "Enter your email to receive a password recovery link.",
                                            size="3",
                                            text_align="center",
                                            style={
                                                "color": "black",
                                            },
                                        ),
                                        rx.hstack(
                                            rx.text(
                                                "want to log in?",
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
                                            spacing="1",
                                        ),
                                        direction="column",
                                        spacing="0",  # Sin espacio adicional
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
                                    type="email",
                                    size="3",
                                    width="100%",
                                ),
                                spacing="2",
                                justify="start",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    "Send Recovery Email",
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
                                ),
                                _hover={
                                    "backgroundColor": "#333333",
                                    "transform": "scale(1.05)",
                                    "transition": "transform 0.2s ease",
                                },
                                href="/login",
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
        title="Container-forgot-password",
        background="linear-gradient(45deg, rgba(255,193,7) 0%, rgba(255,152,0) 25%, rgba(255,113,34) 50%, rgba(242, 116,5) 100%)",
        width="-webkit-fill-available",  # Ancho del contenedor acoplado con responsive design
        height="100vh",
        style={
            "position": "relative",  # Para que todo el contenido esté sobre el fondo
            "height": "100%",
            "width": "100%",
        },
    )
