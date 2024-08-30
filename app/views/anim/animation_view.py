import reflex as rx


def animation_view() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.center(
                rx.image(
                    src="/logo.png",
                    height="250px",
                    border_radius="25%",
                ),
                # Título con espacio en la parte superior e inferior
                rx.heading(
                    rx.text(
                        "Swiftly App",
                        size="6",
                        text_align="center",
                        style={
                            "fontSize": "50px",
                            "color": "black",
                            "fontWeight": "bold",
                            "margin": "50px 0",  # Espacio en la parte superior e inferior
                        },
                    ),
                ),
                rx.hstack(
                    # Texto con margen adicional
                    rx.text(
                        "Tu envío, nuestro compromiso. Rápido, seguro y siempre a tiempo.",
                        size="3",
                        text_align="center",
                        style={
                            "color": "black",
                            "fontSize": "1.5em",
                            "marginTop": "1em",  # Espacio encima del texto
                            "marginBottom": "1em",  # Espacio debajo del texto
                        },
                    ),
                    spacing="4",  # Espacio entre elementos en el hstack (si hay más de uno)
                    width="100%",
                    justify="center",
                    align="center",
                ),
                justify="center",
                align="center",
                direction="column",
            ),
            title="center-animation",
            justify="center",
            align="center",
            direction="column",
            spacing="6",  # Espacio entre elementos en el flex contenedor
            width="-webkit-fill-available",
            height="100vh",  # Configura la altura de la vista
        ),
        title="container-animation",
        padding="0",
        style={
            "background": "linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)",
            "height": "100vh",
        },
    )
