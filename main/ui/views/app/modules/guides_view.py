import reflex as rx
from main.ui.states.deparmentState import DepartmentState
from main.ui.states.countryState import Countrystate
from typing import List


class ShipmentGuideStateV2(rx.State):
    # Sender fields
    sender_name: str = ""
    sender_lastName: str = ""
    sender_state: str = ""
    sender_phone: str = ""

    # Recipient fields
    recipient_name: str = ""
    recipient_lastName: str = ""
    recipient_company: str = ""
    recipient_street: str = ""
    recipient_neighborhood: str = ""
    recipient_city: str = ""
    recipient_state: str = ""
    recipient_country: str = ""
    recipient_postalCode: str = ""
    recipient_phone: str = ""

    # Package fields
    service_type: str = ""
    weight: float = 0.0
    quantity: int = 0
    declared_value: float = 0.0
    is_international: bool = False

    # Section completion flags
    sender_section_complete: bool = False
    recipient_section_complete: bool = False
    package_section_complete: bool = False

    # Actualizar estado de la guía
    def update_recipient_city(self, city: str):
        self.recipient_city = city

    def update_recipient_country(self, country: str):
        self.recipient_country = country

    def update_is_international(self, is_international: bool):
        self.is_international = is_international

    def handle_sender_submit(self, form_data: dict):
        print("Datos del remitente capturados:", form_data)
        # Validate and update sender data
        if self.validate_sender_data(form_data):
            # Update state variables
            self.sender_name = form_data["sender_name"]
            self.sender_lastName = form_data["sender_lastName"]
            self.sender_phone = form_data["sender_phone"]
            self.sender_state = form_data["sender_state"]
            # ... (update other sender fields) ...
            self.sender_section_complete = True
            ModalPageState.next_page()
        else:
            return rx.window_alert("Please fill all required fields")

    def handle_recipient_submit(self, form_data: dict):
        print("Datos del destinatario capturados:", form_data)
        # Validate and update sender data
        if self.validate_recipient_data(form_data):
            # Update state variables
            self.recipient_name = form_data["recipient_name"]
            self.recipient_company = form_data["recipient_company"]
            self.recipient_lastName = form_data["recipient_lastName"]
            self.recipient_street = form_data["recipient_street"]
            self.recipient_neighborhood = form_data["recipient_neighborhood"]
            self.recipient_city = form_data["recipient_city"]
            self.recipient_state = form_data["recipient_state"]
            self.recipient_country = form_data["recipient_country"]
            self.recipient_postalCode = form_data["recipient_postalCode"]
            self.recipient_phone = form_data["recipient_phone"]
            # ... (update other recipient fields) ...
            self.recipient_section_complete = True
            ModalPageState.next_page()
        else:
            return rx.window_alert("Please fill all required fields")

    def handle_package_submit(self, form_data: dict):
        print("Datos del paquete capturados:", form_data)
        # Validate and update sender data
        if self.validate_package_data(form_data):
            # Update state variables
            self.service_type = form_data["service_type"]
            self.weight = form_data["weight"]
            self.quantity = form_data["quantity"]
            self.declared_value = form_data["declared_value"]
            self.is_international = form_data["is_international"].lower() == "true"
            # ... (update other package fields) ...
            self.package_section_complete = True
            ModalPageState.next_page()
        else:
            return rx.window_alert("Please fill all required fields")

    def validate_sender_data(self, form_data: dict) -> bool:
        # Implement validation logic
        return all(form_data.values())

    def validate_recipient_data(self, form_data: dict) -> bool:
        # Implement validation logic
        return all(form_data.values())

    def validate_package_data(self, form_data: dict) -> bool:
        # Implement validation logic
        return all(form_data.values())


class ModalPageState(rx.State):
    current_page: int = 0

    def next_page(self):
        if self.current_page < 2:
            self.current_page += 1

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1


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
    ]

    data: List = []


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
                                        padding="15px",
                                    ),
                                    style={
                                        "paddingTop": "90px",
                                        "paddingBottom": "38px",
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
        on_mount=DepartmentState.on_read_storage,
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
                rx.button(
                    rx.icon("chevron-left", color="rgba(0,0,0,.4)", stroke_width="1"),
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
                                "color": "rgba(0,0,0,.9)",
                            },
                        },
                    },
                    on_click=ModalPageState.prev_page,
                    is_disabled=ModalPageState.current_page == 0,
                ),
                rx.cond(
                    ModalPageState.current_page == 2,
                    rx.form.submit(
                        rx.button(
                            rx.icon("save", color="rgba(0,0,0,.5)", stroke_width="1"),
                            rx.text(
                                "Guardar",
                                color="rgba(0,0,0,.6)",
                                fontWeigh="normal",
                                fontSize="16px",
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
                                        "color": "rgba(0,0,0,.9)",
                                    },
                                },
                            },
                        ),
                        on_click=ModalPageState.next_page,
                    ),
                ),
            ),
            spacing="4",
        ),
    )


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
                        ),
                        name="sender_name",
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
                        ),
                        name="sender_lastName",
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
                        ),
                        name="sender_phone",
                    ),
                ),
                rx.vstack(
                    rx.text("Departamento", color="black"),
                    rx.form.field(
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
                        ),
                        name="sender_state",
                        width="-webkit-fill-available",
                    ),
                ),
                columns="2",
                spacing="2",
            ),
        ),
        on_submit=ShipmentGuideStateV2.handle_sender_submit,
    )


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
                        ),
                        name="recipient_company",
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
                        ),
                        name="recipient_name",
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
                        ),
                        name="recipient_lastName",
                    ),
                ),
                rx.accordion.root(
                    rx.accordion.item(
                        header=rx.hstack(
                            rx.icon("navigation", color="black"),
                            rx.text("Dirección", color="rgba(0, 0, 0, 0.6)"),
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
                                ),
                                name="recipient_street",
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
                                ),
                                name="recipient_neighborhood",
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
                                        name="recipient_city",
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
                                ),
                                name="recipient_state",
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
                                                Countrystate.filter_countries(v),
                                                ShipmentGuideStateV2.update_recipient_country(
                                                    v
                                                ),
                                            ],
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
                                        name="recipient_country",
                                    ),
                                    position="relative",
                                    width="100%",
                                ),
                                rx.cond(
                                    Countrystate.show_suggestions,
                                    rx.box(
                                        rx.vstack(
                                            rx.foreach(
                                                Countrystate.filtered_country,
                                                lambda country: rx.text(
                                                    country,
                                                    on_click=lambda: Countrystate.set_country_input(
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
                            spacing="1",
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
                        ),
                        name="recipient_phone",
                    ),
                ),
                columns="2",
                spacing="4",
            ),
        ),
        on_submit=ShipmentGuideStateV2.handle_recipient_submit,
    )


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
                        ),
                        name="service_type",
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
                        ),
                        name="weight",
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
                        ),
                        name="quantity",
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
                        ),
                        name="declared_value",
                    ),
                ),
                rx.hstack(
                    rx.form.field(
                        rx.checkbox(
                            color_scheme="orange",
                            variant="surface",
                            value=str(ShipmentGuideStateV2.is_international).lower(),
                            on_change=ShipmentGuideStateV2.update_is_international,
                        ),
                        name="is_international",
                    ),
                    rx.text("¿Es un envío internacional?", color="black"),
                ),
                columns="2",
                spacing="4",
            ),
        ),
        on_submit=ShipmentGuideStateV2.handle_package_submit,
    )
