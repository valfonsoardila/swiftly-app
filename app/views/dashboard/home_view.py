import reflex as rx


def home_view() -> rx.Component:
    return rx.vstack(
        # Header
        rx.heading(
            "Dashboard",
            title="Header",  # Título del contenedor para identificarlo
            size="2xl",  # Tamaño del heading en xl
            background_color="black",  # Color de fondo del heading
            border="none",  # Sin borde
            box_shadow="0 2px 4px rgba(0, 0, 0, 0.4)",  # Sombra
            border_bottom_left_radius="10px",  # Radio de borde inferior izquierdo
            border_bottom_right_radius="10px",  # Radio de borde inferior derecho
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
                spacing="6",
                width="100%",
            ),
            title="Main Content",
            background_color="white",  # Color de fondo del contenedor
            width="-webkit-fill-available",  # ?: Ancho del contenedor acoplado con responsive design
        ),
        title="Dashboard",
        background_color="white",
        min_height="100vh",
        spacing="0",  # ?: Este espacio se asigna por defecto a los elementos hijos en 3rem
    )
