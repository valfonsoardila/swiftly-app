import reflex as rx
from typing import List


class ShipmentFormState(rx.State):
    current_page: int = 0

    def next_page(self):
        if self.current_page < 2:
            self.current_page += 1

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1


class DataTableState(rx.State):
    """The app state."""

    cols: list[dict] = [
        {"title": "First Name", "type": "str"},
        {"title": "Last Name", "type": "str"},
        {"title": "Team", "type": "str"},
    ]
    data = [
        ["Lionel", "Messi", "PSG"],
        ["Christiano", "Ronaldo", "Al-Nasir"],
    ]


class GuideState(rx.State):
    guides: list[list] = []

    def add_guide(self, new_guide: list):
        self.guides.append(new_guide)


@rx.page(route="/app/guides", title="App | Guides")
def guides_view():
    return rx.box(
        rx.flex(
            rx.vstack(
                # Encabezado
                rx.heading(
                    rx.hstack(
                        rx.icon("truck", color="rgba(0, 0, 0, 0.8)"),
                        rx.text(
                            "Consulta de guias",
                            size="3xl",
                            font_weight="bold",
                            color="rgba(0, 0, 0, 0.8)",
                        ),
                        align="center",
                        justify="center",
                    ),
                ),
                # Contenido
                rx.box(
                    rx.vstack(
                        rx.box(
                            # boton para abrir el modal de registro de guía
                            rx.dialog.root(
                                rx.dialog.title(""),
                                rx.dialog.trigger(
                                    rx.button(
                                        rx.icon("plus"),
                                        rx.text("Nueva guía", color="white"),
                                        color="white",
                                        style={
                                            "color": "white",
                                            "backgroundColor": "black",
                                            "border": "none",
                                            "padding": "1em 2em",
                                            "borderRadius": "1em",
                                            "cursor": "pointer",
                                            "fontSize": "20px",
                                            "_hover": {
                                                "backgroundColor": "#333333",
                                                "transform": "scale(1.05)",
                                                "transition": "transform 0.2s ease",
                                            },
                                        },
                                    ),
                                ),
                                rx.dialog.content(
                                    rx.dialog.title(
                                        rx.heading(
                                            rx.text(
                                                "Registro de guía de envío",
                                                size="xl",
                                                font_weight="bold",
                                                color="black",
                                            ),
                                        ),
                                    ),
                                    rx.dialog.description(
                                        rx.text(
                                            "Completa los siguientes pasos para registrar tu nuevo servicio de envío.",
                                            size="lg",
                                            color="black",
                                        ),
                                    ),
                                    new_shipment_guide_view(),
                                    rx.hstack(
                                        rx.dialog.close(
                                            rx.button(
                                                rx.icon("X"),
                                                rx.text("Cerrar", color="white"),
                                                color="white",
                                                style={
                                                    "color": "white",
                                                    "backgroundColor": "black",
                                                    "border": "none",
                                                    "borderRadius": "1em",
                                                    "cursor": "pointer",
                                                    "fontSize": "18px",
                                                    "_hover": {
                                                        "backgroundColor": "#333333",
                                                        "transform": "scale(1.05)",
                                                        "transition": "transform 0.2s ease",
                                                    },
                                                },
                                            ),
                                        ),
                                        justify="end",
                                        spacing="2",
                                        padding="15px",
                                    ),
                                    style={
                                        "paddingTop": "90px",
                                        "paddingBottom": "50px",
                                        "paddingLeft": "65px",
                                        "paddingRight": "65px",
                                        "borderRadius": "40px",
                                        "border": "none",
                                        "backgroundImage": "url('/img/portapapeles.png')",
                                        "backgroundSize": "cover",
                                        "backgroundPosition": "0px -60px",
                                        "backgroundRepeat": "no-repeat",
                                    },
                                ),
                            )
                        ),
                        rx.box(
                            rx.data_table(
                                columns=DataTableState.cols,
                                data=DataTableState.data,
                                pagination=True,
                                search=True,
                                sort=True,
                            ),
                        ),
                        width="100%",
                    ),
                    width="100%",
                    height="-webkit-fill-available",
                    display="flex",
                ),
                width="100%",
                height="100%",
                align="center",
            ),
            align="center",
            justify="center",
            width="100%",
            height="100%",
        ),
        width="100%",
        height="100%",
        padding="20px",
    )


def new_shipment_guide_view() -> rx.Component:
    return rx.box(
        rx.form(
            rx.vstack(
                rx.match(
                    ShipmentFormState.current_page,
                    (0, rx.box(sender_section(), width="100%", height="100%")),
                    (1, rx.box(recipient_section(), width="100%", height="100%")),
                    (2, rx.box(package_section(), width="100%", height="100%")),
                ),
                rx.hstack(
                    rx.button(
                        rx.icon("arrow-left"),
                        style={
                            "color": "white",
                            "backgroundColor": "black",
                            "border": "none",
                            "borderRadius": "1em",
                            "cursor": "pointer",
                            "fontSize": "20px",
                            "_hover": {
                                "backgroundColor": "#333333",
                                "transform": "scale(1.05)",
                                "transition": "transform 0.2s ease",
                            },
                        },
                        on_click=ShipmentFormState.prev_page,
                        is_disabled=ShipmentFormState.current_page == 0,
                    ),
                    rx.cond(
                        ShipmentFormState.current_page == 2,
                        rx.button(
                            rx.icon("save"),
                            rx.text("Guardar", color="white"),
                            style={
                                "color": "white",
                                "backgroundColor": "black",
                                "border": "none",
                                "borderRadius": "1em",
                                "cursor": "pointer",
                                "fontSize": "20px",
                                "_hover": {
                                    "backgroundColor": "#333333",
                                    "transform": "scale(1.05)",
                                    "transition": "transform 0.2s ease",
                                },
                            },
                            # on_click=handle_submit,  # You need to define this function
                        ),
                        rx.button(
                            rx.icon("arrow-right"),
                            style={
                                "color": "white",
                                "backgroundColor": "black",
                                "border": "none",
                                "borderRadius": "1em",
                                "cursor": "pointer",
                                "fontSize": "20px",
                                "_hover": {
                                    "backgroundColor": "#333333",
                                    "transform": "scale(1.05)",
                                    "transition": "transform 0.2s ease",
                                },
                            },
                            on_click=ShipmentFormState.next_page,
                            is_disabled=ShipmentFormState.current_page == 2,
                        ),
                    ),
                ),
                spacing="4",
            ),
        ),
    )


def sender_section() -> rx.Component:
    return (
        rx.vstack(
            rx.text(
                "Datos del remitente",
                color="black",
                font_size="18px",
                font_weight="bold",
            ),
            rx.grid(
                rx.vstack(
                    rx.text("Nombres", color="black"),
                    rx.input(
                        rx.input.slot(rx.icon("user", color="black"), position="left"),
                        placeholder="Ingresa tus nombres",
                        type="text",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                ),
                rx.vstack(
                    rx.text("Apellidos", color="black"),
                    rx.input(
                        rx.input.slot(rx.icon("user", color="black"), position="left"),
                        placeholder="Ingresa tus apellidos",
                        type="text",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                ),
                rx.vstack(
                    rx.text("Número de teléfono", color="black"),
                    rx.input(
                        rx.input.slot(rx.icon("phone", color="black"), position="left"),
                        placeholder="Ingresa el número de teléfono del remitente",
                        type="tel",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                ),
                rx.vstack(
                    rx.text("Departamento", color="black"),
                    rx.select.root(
                        rx.select.trigger(
                            placeholder="Selecciona una opción",
                            color_scheme="orange",
                            color="black",
                            width="100%",
                            style={
                                "backgroundColor": "rgba(255, 255, 255, 0.4)",
                                "border": "1px solid rgba(0, 0, 0, 0.8)",
                                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                "borderRadius": "20px",
                                "fontSize": "20px",
                                "span": {
                                    "color": "rgba(0, 0, 0, 0.8)",
                                },
                                "svg": {
                                    "height": "20px",
                                    "width": "20px",
                                    "fontWeight": "bold !important",
                                },
                            },
                        ),
                        rx.select.content(
                            rx.select.item(
                                rx.hstack(
                                    rx.icon("box", color="black", position="left"),
                                    rx.text("Caja"),
                                    style={
                                        "display": "flex",
                                        "alignItems": "center",
                                    },
                                ),
                                value="1",
                            ),
                            rx.select.item(
                                rx.hstack(
                                    rx.icon("package", color="black", position="left"),
                                    rx.text("Paquete"),
                                    style={
                                        "display": "flex",
                                        "alignItems": "center",
                                    },
                                ),
                                value="2",
                            ),
                            rx.select.item(
                                rx.hstack(
                                    rx.icon("mail", color="black", position="left"),
                                    rx.text("Sobre"),
                                    style={
                                        "display": "flex",
                                        "alignItems": "center",
                                    },
                                ),
                                value="3",
                            ),
                            color_scheme="orange",
                            background_color="white",
                            color="black",
                        ),
                        size="3",
                        color_scheme="orange",
                        variant="surface",
                    ),
                ),
                columns="2",
                spacing="2",
            ),
        ),
    )


def recipient_section() -> rx.Component:
    return (
        rx.vstack(
            rx.text(
                "Datos del destinatario",
                font_size="18px",
                font_weight="bold",
                color="black",
            ),
            rx.grid(
                rx.vstack(
                    rx.text("Compañía", color="black"),
                    rx.input(
                        rx.input.slot(
                            rx.icon("building-2", color="black"), position="left"
                        ),
                        placeholder="Ingresa el nombre de la compañía",
                        type="text",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                ),
                rx.vstack(
                    rx.text("Nombres", color="black"),
                    rx.input(
                        rx.input.slot(
                            rx.icon("person-standing", color="black"), position="left"
                        ),
                        placeholder="Ingresa los nombres del destinatario",
                        type="text",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                ),
                rx.vstack(
                    rx.text("Apellidos", color="black"),
                    rx.input(
                        rx.input.slot(
                            rx.icon("person-standing", color="black"), position="left"
                        ),
                        placeholder="Ingresa los apellidos del destinatario",
                        type="text",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                ),
                rx.vstack(
                    rx.text("Dirección", color="black"),
                    rx.input(
                        rx.input.slot(
                            rx.icon("map-pin", color="black"), position="left"
                        ),
                        placeholder="Calle y número",
                        type="text",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                    rx.input(
                        rx.input.slot(
                            rx.icon("parking-meter", color="black"), position="left"
                        ),
                        placeholder="Barrio o colonia",
                        type="text",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("hotel", color="black"), position="left"),
                        placeholder="Ciudad o municipio",
                        type="text",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                    rx.select.root(
                        rx.select.trigger(
                            placeholder="Departamento o estado",
                            color_scheme="orange",
                            color="black",
                            width="100%",
                            style={
                                "backgroundColor": "rgba(255, 255, 255, 0.4)",
                                "border": "1px solid rgba(0, 0, 0, 0.8)",
                                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                "borderRadius": "20px",
                                "fontSize": "20px",
                                "span": {
                                    "color": "rgba(0, 0, 0, 0.8)",
                                },
                                "svg": {
                                    "height": "20px",
                                    "width": "20px",
                                    "fontWeight": "bold !important",
                                },
                            },
                        ),
                        rx.select.content(
                            rx.select.item(
                                rx.hstack(
                                    rx.icon("box", color="black"),
                                    rx.text("Caja"),
                                    style={
                                        "display": "flex",
                                        "alignItems": "center",
                                    },
                                ),
                                value="1",
                            ),
                            rx.select.item(
                                rx.hstack(
                                    rx.icon("package", color="black"),
                                    rx.text("Paquete"),
                                    style={
                                        "display": "flex",
                                        "alignItems": "center",
                                    },
                                ),
                                value="2",
                            ),
                            rx.select.item(
                                rx.hstack(
                                    rx.icon("mail", color="black"),
                                    rx.text("Sobre"),
                                    style={
                                        "display": "flex",
                                        "alignItems": "center",
                                    },
                                ),
                                value="3",
                            ),
                            color_scheme="orange",
                            background_color="white",
                            color="black",
                        ),
                        size="3",
                        color_scheme="orange",
                        variant="surface",
                    ),
                    rx.input(
                        rx.input.slot(
                            rx.icon("compass", color="black"), position="left"
                        ),
                        placeholder="Pais",
                        type="text",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                ),
                rx.vstack(
                    rx.text("Teléfono", color="black"),
                    rx.input(
                        rx.input.slot(rx.icon("phone", color="black"), position="left"),
                        placeholder="Ingresa el número de teléfono del destinatario",
                        type="tel",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                ),
                columns="2",
                spacing="4",
            ),
        ),
    )


def package_section() -> rx.Component:
    return (
        rx.vstack(
            rx.text(
                "Datos del paquete",
                font_size="18px",
                font_weight="bold",
                color="black",
            ),
            rx.grid(
                rx.vstack(
                    rx.text("Tipo de servicio", color="black"),
                    rx.select.root(
                        rx.select.trigger(
                            placeholder="Selecciona un tipo de servicio",
                            color_scheme="orange",
                            color="black",
                            width="100%",
                            style={
                                "backgroundColor": "rgba(255, 255, 255, 0.4)",
                                "border": "1px solid rgba(0, 0, 0, 0.8)",
                                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                "borderRadius": "20px",
                                "fontSize": "20px",
                                "span": {
                                    "color": "rgba(0, 0, 0, 0.8)",
                                },
                                "svg": {
                                    "height": "20px",
                                    "width": "20px",
                                    "fontWeight": "bold !important",
                                },
                            },
                        ),
                        rx.select.content(
                            rx.select.item(
                                rx.hstack(
                                    rx.icon("box", color="black"),
                                    rx.text("Caja"),
                                    style={
                                        "display": "flex",
                                        "alignItems": "center",
                                    },
                                ),
                                value="1",
                            ),
                            rx.select.item(
                                rx.hstack(
                                    rx.icon("package", color="black"),
                                    rx.text("Paquete"),
                                    style={
                                        "display": "flex",
                                        "alignItems": "center",
                                    },
                                ),
                                value="2",
                            ),
                            rx.select.item(
                                rx.hstack(
                                    rx.icon("mail", color="black"),
                                    rx.text("Sobre"),
                                    style={
                                        "display": "flex",
                                        "alignItems": "center",
                                    },
                                ),
                                value="3",
                            ),
                            color_scheme="orange",
                            background_color="white",
                            color="black",
                        ),
                        size="3",
                        color_scheme="orange",
                        variant="surface",
                    ),
                ),
                rx.vstack(
                    rx.text("Peso", color="black"),
                    rx.input(
                        rx.input.slot(
                            rx.icon("weight", color="black"), position="left"
                        ),
                        placeholder="Ingresa el peso del paquete",
                        type="number",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                ),
                rx.vstack(
                    rx.text("Cantidad", color="black"),
                    rx.input(
                        rx.input.slot(
                            rx.icon("package", color="black"), position="left"
                        ),
                        placeholder="Ingresa la cantidad de paquetes",
                        type="number",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                ),
                rx.vstack(
                    rx.text("Valor declarado", color="black"),
                    rx.input(
                        rx.input.slot(
                            rx.icon("weight", color="black"), position="left"
                        ),
                        placeholder="Ingresa el valor declarado del paquete",
                        type="number",
                        size="3",
                        width="100%",
                        color_scheme="orange",
                        variant="surface",
                        radius="full",
                        required=True,
                        style={
                            "color": "black",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "& input::placeholder": {
                                "color": "rgba(0, 0, 0, 0.6)",
                            },
                        },
                    ),
                ),
                rx.hstack(
                    rx.checkbox(),
                    rx.text("¿Es un envío internacional?", color="black"),
                ),
                columns="2",
                spacing="4",
            ),
        ),
    )
