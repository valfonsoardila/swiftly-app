import reflex as rx


def animation_view() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.center(
                rx.image(
                    src="/logo.png",
                    height="250px",
                    border_radius="25%",
                    style={
                        "animation": "fadeInDown 2s ease-out",  # Aplicar la animación CSS
                    },
                ),
                rx.heading(
                    rx.text(
                        "Swiftly App",
                        size="6",
                        text_align="center",
                        style={
                            "fontSize": "50px",
                            "color": "black",
                            "fontWeight": "bold",
                            "margin": "50px 0",
                        },
                    ),
                ),
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "Tu envío, nuestro compromiso. Rápido, seguro y siempre a tiempo.",
                            size="3",
                            text_align="center",
                            style={
                                "color": "black",
                                "fontSize": "1.5em",
                                "marginTop": "1em",
                                "marginBottom": "1em",
                            },
                        ),
                        rx.link(
                            rx.button(
                                "¡Comencemos!",
                                size="large",
                                style={
                                    "color": "white",
                                    "backgroundColor": "black",
                                    "border": "none",
                                    "padding": "1em 2em",
                                    "borderRadius": "1em",
                                    "cursor": "pointer",
                                    "fontSize": "1.5em",
                                },
                                _hover={
                                    "backgroundColor": "#333333",
                                    "transform": "scale(1.05)",
                                    "transition": "transform 0.2s ease",
                                },
                            ),
                            href="/login",  # Redirigir a la ruta /login
                        ),
                        autofocus=True,
                        align="center",
                        justify="center",
                        spacing="2",
                    ),
                    spacing="4",
                    width="100%",
                    justify="center",
                    align="center",
                ),
                justify="center",
                align="center",
                direction="column",
                title="center-animation",
            ),
            title="flex-animation",
            justify="center",
            align="center",
            direction="column",
            spacing="6",
            width="100%",
            height="100vh",
            style={
                "background": "url('/repartidor-paquete-hombro.png')",
                "backgroundSize": "contain",
                "backgroundPosition": "right",
                "backgroundRepeat": "no-repeat",
                "maxWidth": "100vw !important",
            },
        ),
        title="container-animation",
        padding="0",
        style={
            "background": "linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)",
            "height": "100vh",
            "width": "100%",
        },
    )
