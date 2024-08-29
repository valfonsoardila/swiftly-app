import reflex as rx


def home_view() -> rx.Component:
    return rx.vstack(
        # Header
        rx.heading(
            "Dashboard",
            size="2xl",
            background_color="rgba(130, 13, 13, 0.5)",  # Color de fondo con opacidad
            color="primary-foreground",
            padding="4",  # Espaciado interno alrededor del texto
            width="100%",  # Ancho completo del contenedor
            margin="0",  # Márgenes alrededor del heading
            text_align="center",  # Alineación del texto
            font_weight="bold",  # Peso de la fuente
            font_family="Arial",  # Familia de la fuente
            font_size="2rem",  # Tamaño de la fuente en rem
            line_height="1.5",  # Altura de línea
        ),
        # Main Content
        rx.container(
            rx.vstack(
                rx.button("Crear Nueva Guía", size="md"),
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.heading("Guías", size="xl"),
                            spacing="4",
                        ),
                    ),
                ),
                width="100%",
            ),
            padding="6",
            background_color="white",  # Color de fondo del contenedor
        ),
        min_height="100vh",
        width="100%",
    )
