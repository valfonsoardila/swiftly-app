import reflex as rx
from main.ui.states.deparmentState import DepartmentState
from main.ui.states.countriesState import CountriesState
from main.ui.components.progress_modal import progress_modal
from main.ui.components.table_interactive import table_interactive
from main.ui.states.shipmentGuideStateV2 import ShipmentGuideStateV2


# Vista de la página de guías
def guides_view():
    list_sections = [
        sender_section(),
        recipient_section(),
        package_section(),
    ]
    return rx.box(
        rx.flex(
            rx.vstack(
                # Encabezado
                rx.heading(
                    rx.hstack(
                        rx.icon(
                            "truck",
                            color=rx.color_mode_cond(
                                light="rgba(0, 0, 0, 0.8)",
                                dark="rgba(255, 255, 255, 0.8)",
                            ),
                            size=32,
                        ),
                        rx.text(
                            "Consulta de guias",
                            size="3xl",
                            font_weight="bold",
                            color=rx.color_mode_cond(light="black", dark="white"),
                        ),
                        align="center",
                        justify="center",
                    ),
                ),
                # Contenido
                rx.box(
                    rx.vstack(
                        rx.box(
                            progress_modal(
                                list_sections,
                            ),
                        ),
                        rx.box(
                            table_interactive(),
                            height="-webkit-fill-available",
                            width="100%",
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
                        width="-webkit-fill-available",
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
                        width="-webkit-fill-available",
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
                        width="-webkit-fill-available",
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
                        width="-webkit-fill-available",
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
                        width="-webkit-fill-available",
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
                        width="-webkit-fill-available",
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
                                width="-webkit-fill-available",
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
                                width="-webkit-fill-available",
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
                                        width="-webkit-fill-available",
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
                                        width="-webkit-fill-available",
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
                        width="-webkit-fill-available",
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
                        width="-webkit-fill-available",
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
                        width="-webkit-fill-available",
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
                        width="-webkit-fill-available",
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
                        width="-webkit-fill-available",
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
                        width="-webkit-fill-available",
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
