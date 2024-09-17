import reflex as rx
from main.ui.states.deparmentState import DepartmentState
from main.ui.states.countriesState import CountriesState
from typing import List

from main.ui.states.shipmentGuideStateV2 import ShipmentGuideStateV2


class ModalPageState(rx.State):
    current_page: int = 0

    def next_page(self):
        if self.current_page < 2:
            self.current_page += 1

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1

    @rx.var
    def total_pages(self) -> int:
        return 3  # Since you have 3 sections


class DataTableState(rx.State):
    """The app state."""

    columns: List[str] = [
        "Date",
        "Tracking #",
        "Package Type",
        "Quantity",
        "Weight",
        "Sender",
        "Recipient",
        "Recipient Company",
        "Recipient Address",
        "Options",
    ]

    data: List = []


# Vista de la página de guías
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
                                rx.dialog.title("", fontSize="0px", margin="0"),
                                rx.dialog.trigger(
                                    rx.box(
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
                                        width="100%",
                                        align="center",
                                        justify="center",
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
                                        padding_top="0px",
                                        padding_bottom="10px",
                                    ),
                                    style={
                                        "paddingTop": "90px",
                                        "paddingBottom": "0px",
                                        "paddingLeft": "65px",
                                        "paddingRight": "65px",
                                        "borderRadius": "40px",
                                        "border": "none",
                                        "backgroundImage": "url('/img/portapapeles.png')",
                                        "backgroundSize": "cover",
                                        "backgroundPosition": "0px -70px",
                                        "backgroundRepeat": "no-repeat",
                                    },
                                ),
                            )
                        ),
                        rx.box(
                            rx.data_table(
                                columns=DataTableState.columns,
                                data=DataTableState.data,
                                pagination=True,
                                search=True,
                                sort=True,
                            ),
                            height="-webkit-fill-available",
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
        on_mount=[
            DepartmentState.on_read_storage,
            CountriesState.on_read_storage,
        ],
    )


# Step-By-Step del modal de registro de guía
def new_shipment_guide_view() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.match(
                ModalPageState.current_page,
                (0, rx.box(sender_section(), width="100%", height="100%")),
                (1, rx.box(recipient_section(), width="100%", height="100%")),
                (2, rx.box(package_section(), width="100%", height="100%")),
            ),
            rx.hstack(
                rx.form.submit(
                    rx.button(
                        rx.icon(
                            "chevron-left", color="rgba(0,0,0,.4)", stroke_width="1"
                        ),
                        type="submit",
                        on_click=ModalPageState.prev_page,
                        style={
                            "color": "white",
                            "backgroundColor": "transparent",
                            "border": "none",
                            "borderRadius": "1em",
                            "cursor": "pointer",
                            "fontSize": "20px",
                            "_hover": {
                                "backgroundColor": "transparent",
                                "transform": "scale(1.05)",
                                "transition": "transform 0.2s ease",
                                "svg": {
                                    "color": "black",
                                    "strokeWidth": "2",
                                },
                            },
                        },
                        is_disabled=ModalPageState.current_page == 0,
                    ),
                ),
                rx.text(
                    f"{ModalPageState.current_page + 1}/{ModalPageState.total_pages}",
                    color="black",
                    font_size="16px",
                    font_weight="bold",
                ),
                rx.cond(
                    ModalPageState.current_page == 2,
                    rx.form.submit(
                        rx.button(
                            rx.icon("save", color="rgba(0,0,0,.5)", stroke_width="1"),
                            rx.text(
                                "Guardar",
                                color="rgba(0,0,0,.5)",
                                fontWeigh="normal",
                                fontSize="16px",
                            ),
                            type="submit",
                            form=rx.cond(
                                ModalPageState.current_page == 0,
                                "sender_form",
                                rx.cond(
                                    ModalPageState.current_page == 1,
                                    "recipient_form",
                                    "package_form",
                                ),
                            ),
                            style={
                                "color": "white",
                                "backgroundColor": "transparent",
                                "border": "none",
                                "borderRadius": "1em",
                                "cursor": "pointer",
                                "_hover": {
                                    "backgroundColor": "transparent",
                                    "border": "1px solid rgba(0, 0, 0, 0.8)",
                                    "transform": "scale(1.05)",
                                    "transition": "transform 0.2s ease",
                                    "p": {
                                        "fontWeight": "normal",
                                        "color": "rgba(0,0,0,.9)",
                                    },
                                    "svg": {
                                        "color": "rgba(0,0,0,.9)",
                                    },
                                },
                            },
                        ),
                    ),
                    rx.form.submit(
                        rx.button(
                            rx.icon(
                                "chevron-right",
                                color="rgba(0,0,0,.5)",
                                stroke_width="1",
                            ),
                            type="submit",
                            form=rx.cond(
                                ModalPageState.current_page == 0,
                                "sender_form",
                                rx.cond(
                                    ModalPageState.current_page == 1,
                                    "recipient_form",
                                    "package_form",
                                ),
                            ),
                            on_click=ModalPageState.next_page,
                            style={
                                "color": "white",
                                "backgroundColor": "transparent",
                                "border": "none",
                                "borderRadius": "1em",
                                "cursor": "pointer",
                                "fontSize": "20px",
                                "_hover": {
                                    "backgroundColor": "transparent",
                                    "transform": "scale(1.05)",
                                    "transition": "transform 0.2s ease",
                                    "svg": {
                                        "color": "black",
                                        "strokeWidth": "2",
                                    },
                                },
                            },
                        ),
                    ),
                ),
                justify="space-between",
                width="100%",
            ),
            spacing="0",
        ),
    )


# Secciones del formulario de registro de guía
# Seccion de datos del remitente
def sender_section() -> rx.Component:
    return rx.form.root(
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
                    rx.form.field(
                        rx.input(
                            rx.input.slot(
                                rx.icon("user", color="black"), position="left"
                            ),
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
                            name="sender_name",
                            id="sender_name",
                        ),
                    ),
                ),
                rx.vstack(
                    rx.text("Apellidos", color="black"),
                    rx.form.field(
                        rx.input(
                            rx.input.slot(
                                rx.icon("user", color="black"), position="left"
                            ),
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
                            name="sender_lastName",
                            id="sender_lastName",
                        ),
                    ),
                ),
                rx.vstack(
                    rx.text("Número de teléfono", color="black"),
                    rx.form.field(
                        rx.input(
                            rx.input.slot(
                                rx.icon("phone", color="black"), position="left"
                            ),
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
                            name="sender_phone",
                            id="sender_phone",
                        ),
                    ),
                ),
                rx.vstack(
                    rx.text("Departamento", color="black"),
                    rx.select.root(
                        rx.select.trigger(
                            placeholder="Selecciona un estado",
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
                                    "color": "rgba(0, 0, 0, 0.6)",
                                    "fontSize": "16px",
                                },
                                "svg": {
                                    "height": "20px",
                                    "width": "20px",
                                    "fontWeight": "bold !important",
                                },
                            },
                        ),
                        rx.select.content(
                            rx.foreach(
                                DepartmentState.departments,
                                lambda department: rx.select.item(
                                    rx.hstack(
                                        rx.icon(
                                            "map-pin",
                                            color="black",
                                            position="left",
                                        ),
                                        rx.text(
                                            department["departamento"],
                                            color="black",
                                        ),
                                        style={
                                            "display": "flex",
                                            "alignItems": "center",
                                        },
                                    ),
                                    value=department["id"],
                                ),
                            ),
                            color_scheme="orange",
                            background_color="white",
                            color="black",
                        ),
                        size="3",
                        color_scheme="orange",
                        variant="surface",
                        name="sender_state",
                    ),
                    width="-webkit-fill-available",
                ),
                columns="2",
                spacing="2",
            ),
        ),
        on_submit=ShipmentGuideStateV2.handle_sender_submit,
        id="sender_form",
    )


# Seccion de datos del destinatario
def recipient_section() -> rx.Component:
    return rx.form.root(
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
                    rx.form.field(
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
                            name="recipient_company",
                            id="recipient_company",
                        ),
                    ),
                ),
                rx.vstack(
                    rx.text("Nombres", color="black"),
                    rx.form.field(
                        rx.input(
                            rx.input.slot(
                                rx.icon("person-standing", color="black"),
                                position="left",
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
                            name="recipient_name",
                            id="recipient_name",
                        ),
                    ),
                ),
                rx.vstack(
                    rx.text("Apellidos", color="black"),
                    rx.form.field(
                        rx.input(
                            rx.input.slot(
                                rx.icon("person-standing", color="black"),
                                position="left",
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
                            name="recipient_lastName",
                            id="recipient_lastName",
                        ),
                    ),
                ),
                rx.accordion.root(
                    rx.accordion.item(
                        header=rx.hstack(
                            rx.icon("navigation", color="black", size=20),
                            rx.text(
                                "Dirección",
                                color="rgba(0, 0, 0, 0.6)",
                                font_size="16px",
                            ),
                        ),
                        content=rx.vstack(
                            rx.form.field(
                                rx.input(
                                    rx.input.slot(
                                        rx.icon("map-pin", color="black"),
                                        position="left",
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
                                    name="recipient_street",
                                    id="recipient_street",
                                ),
                            ),
                            rx.form.field(
                                rx.input(
                                    rx.input.slot(
                                        rx.icon("parking-meter", color="black"),
                                        position="left",
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
                                    name="recipient_neighborhood",
                                    id="recipient_neighborhood",
                                ),
                            ),
                            rx.vstack(
                                rx.box(
                                    rx.form.field(
                                        rx.input(
                                            rx.input.slot(
                                                rx.icon("hotel", color="black"),
                                                position="left",
                                            ),
                                            placeholder="Ciudad o municipio",
                                            type="text",
                                            size="3",
                                            width="100%",
                                            color_scheme="orange",
                                            variant="surface",
                                            radius="full",
                                            required=True,
                                            on_change=lambda v: [
                                                DepartmentState.filter_cities(v),
                                                ShipmentGuideStateV2.update_recipient_city(
                                                    v
                                                ),
                                            ],
                                            value=DepartmentState.city_input,
                                            style={
                                                "color": "black",
                                                "border": "1px solid rgba(0, 0, 0, 0.8)",
                                                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                                "backgroundColor": "rgba(235, 235, 235, 0.4)",
                                                "& input::placeholder": {
                                                    "color": "rgba(0, 0, 0, 0.6)",
                                                },
                                            },
                                            name="recipient_city",
                                            id="recipient_city",
                                        ),
                                    ),
                                    position="relative",
                                    width="100%",
                                ),
                                rx.cond(
                                    DepartmentState.show_suggestions,
                                    rx.box(
                                        rx.vstack(
                                            rx.foreach(
                                                DepartmentState.filtered_cities,
                                                lambda city: rx.text(
                                                    city,
                                                    on_click=lambda: DepartmentState.set_city_input(
                                                        city
                                                    ),
                                                    color="black",
                                                    cursor="pointer",
                                                    _hover={
                                                        "background": "rgba(250, 250, 250, 0.3)",
                                                        "border": "none",
                                                        "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                                        "borderRadius": "10px",
                                                    },
                                                    align="center",
                                                    width="100%",
                                                ),
                                            ),
                                            max_height="200px",
                                            overflow="auto",
                                        ),
                                        position="absolute",
                                        top="100%",
                                        left="0",
                                        width="100%",
                                        bg="white",
                                        z_index="1",
                                        style={
                                            "border": "none",
                                            "borderRadius": "10px",
                                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                        },
                                    ),
                                ),
                                position="relative",
                                width="100%",
                            ),
                            rx.form.field(
                                rx.select.root(
                                    rx.select.trigger(
                                        placeholder="Departamento",
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
                                                "color": "rgba(0, 0, 0, 0.6)",
                                                "fontSize": "16px",
                                            },
                                            "svg": {
                                                "height": "20px",
                                                "width": "20px",
                                                "fontWeight": "bold !important",
                                            },
                                        },
                                    ),
                                    rx.select.content(
                                        rx.foreach(
                                            DepartmentState.departments,
                                            lambda department: rx.select.item(
                                                rx.hstack(
                                                    rx.icon(
                                                        "map-pin",
                                                        color="black",
                                                        position="left",
                                                    ),
                                                    rx.text(
                                                        department["departamento"],
                                                        color="black",
                                                    ),
                                                    style={
                                                        "display": "flex",
                                                        "alignItems": "center",
                                                    },
                                                ),
                                                value=department["id"],
                                            ),
                                        ),
                                        color_scheme="orange",
                                        background_color="white",
                                        color="black",
                                    ),
                                    size="3",
                                    color_scheme="orange",
                                    variant="surface",
                                    name="recipient_state",
                                ),
                                width="-webkit-fill-available",
                            ),
                            # Pendiente por implementar el atrapar el país
                            rx.vstack(
                                rx.box(
                                    rx.form.field(
                                        rx.input(
                                            rx.input.slot(
                                                rx.icon("compass", color="black"),
                                                position="left",
                                            ),
                                            placeholder="Pais",
                                            type="text",
                                            size="3",
                                            width="100%",
                                            color_scheme="orange",
                                            variant="surface",
                                            radius="full",
                                            required=True,
                                            # Tengo setear el valor de Countrystate.country_input a country_recipient
                                            on_change=lambda v: [
                                                CountriesState.filter_countries(v),
                                                ShipmentGuideStateV2.update_recipient_country(
                                                    v
                                                ),
                                            ],
                                            value=CountriesState.country_input,
                                            style={
                                                "color": "black",
                                                "border": "1px solid rgba(0, 0, 0, 0.8)",
                                                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                                "backgroundColor": "rgba(235, 235, 235, 0.4)",
                                                "& input::placeholder": {
                                                    "color": "rgba(0, 0, 0, 0.6)",
                                                },
                                            },
                                            name="recipient_country",
                                            id="recipient_country",
                                        ),
                                    ),
                                    position="relative",
                                    width="100%",
                                ),
                                rx.cond(
                                    CountriesState.show_suggestions,
                                    rx.box(
                                        rx.vstack(
                                            rx.foreach(
                                                CountriesState.filtered_country,
                                                lambda country: rx.text(
                                                    country,
                                                    on_click=lambda: CountriesState.set_country_input(
                                                        country
                                                    ),
                                                    color="black",
                                                    cursor="pointer",
                                                    _hover={
                                                        "background": "rgba(250, 250, 250, 0.3)",
                                                        "border": "none",
                                                        "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                                        "borderRadius": "10px",
                                                    },
                                                    align="center",
                                                    width="100%",
                                                ),
                                            ),
                                            max_height="200px",
                                            overflow="auto",
                                        ),
                                        position="fixed",  # Change to fixed
                                        width="10%",
                                        bg="white",
                                        z_index="9999",  # Increase z-index
                                        style={
                                            "border": "none",
                                            "borderRadius": "10px",
                                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                        },
                                        # Add an ID to the box for JavaScript targeting
                                        id="country-suggestions",
                                    ),
                                ),
                                position="relative",
                                width="100%",
                            ),
                            spacing="0",
                        ),  # content
                        value="direccion",
                    ),
                    width="100%",
                    easing="ease-in-out",
                    style={
                        "button": {
                            "svg": {
                                "color": "black !important",
                            },
                            "borderRadius": "20px",
                            "border": "1px solid rgba(0, 0, 0, 0.8)",
                            "color": "black",
                            "backgroundColor": "rgba(235, 235, 235, 0.4)",
                            "_hover": {
                                "backgroundColor": "rgba(230, 230, 230, 0.8)",
                                "color": "black",
                            },
                        },
                        "marginTop": "auto",
                    },
                    variant="ghost",
                    collapsible=True,
                ),
                rx.vstack(
                    rx.text("Teléfono", color="black"),
                    rx.form.field(
                        rx.input(
                            rx.input.slot(
                                rx.icon("phone", color="black"), position="left"
                            ),
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
                            name="recipient_phone",
                            id="recipient_phone",
                        ),
                    ),
                ),
                rx.vstack(
                    rx.text("Codigo Postal", color="black"),
                    rx.form.field(
                        rx.input(
                            rx.input.slot(
                                rx.icon("book-copy", color="black"), position="left"
                            ),
                            placeholder="Ingresa el código postal del destinatario",
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
                            name="recipient_postalCode",
                            id="recipient_postalCode",
                        ),
                    ),
                ),
                columns="2",
                spacing="2",
            ),
            spacing="0",
        ),
        on_submit=ShipmentGuideStateV2.handle_recipient_submit,
        id="recipient_form",
    )


# Seccion de datos del paquete
def package_section() -> rx.Component:
    return rx.form.root(
        rx.vstack(
            rx.text(
                "Datos del paquete",
                font_size="18px",
                font_weight="bold",
                color="black",
            ),
            rx.grid(
                # Pendiente por implementar el atrapar el tipo de servicio
                rx.vstack(
                    rx.text("Tipo de servicio", color="black"),
                    rx.form.field(
                        rx.select.root(
                            rx.select.trigger(
                                placeholder="Tipo de servicio",
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
                            name="service_type",
                        ),
                    ),
                ),
                rx.vstack(
                    rx.text("Peso", color="black"),
                    rx.form.field(
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
                            name="weight",
                            id="weight",
                        ),
                    ),
                ),
                rx.vstack(
                    rx.text("Cantidad", color="black"),
                    rx.form.field(
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
                            name="quantity",
                            id="quantity",
                        ),
                    ),
                ),
                rx.vstack(
                    rx.text("Valor declarado", color="black"),
                    rx.form.field(
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
                            name="declared_value",
                            id="declared_value",
                        ),
                    ),
                ),
                rx.hstack(
                    rx.form.field(
                        rx.checkbox(
                            color_scheme="orange",
                            variant="surface",
                            value=str(ShipmentGuideStateV2.is_international).lower(),
                            on_change=ShipmentGuideStateV2.update_is_international,
                            style={
                                "borderRadius": "20%",
                                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                "cursor": "pointer",
                            },
                            name="is_international",
                            id="is_international",
                        ),
                        style={
                            "label": {
                                "--line-height": "none",
                            },
                            "margin": "0",
                            "padding": "0",
                            "border": "none",
                        },
                    ),
                    rx.text(
                        "¿Es un envío internacional?", color="black", font_size="14px"
                    ),
                    style={
                        "padding": "10px 0",
                    },
                    align="center",
                    justify="center",
                ),
                columns="2",
                spacing="4",
            ),
        ),
        on_submit=ShipmentGuideStateV2.handle_package_submit,
        id="package_form",
    )