import reflex as rx


class TrackingState(rx.State):
    nombre_usuario: str = ""
    numero_guia: str = ""
    estado_envio: str = ""

    def consultar_envio(self):
        self.estado_envio = f"Envío en camino para {self.nombre_usuario}"

    def go_to_login(self):
        return rx.redirect("/login")


@rx.page(route="/tracking")
def tracking_view() -> rx.Component:
    return rx.vstack(
        # Encabezado
        rx.heading(
            rx.hstack(
                rx.button(
                    rx.icon(tag="arrow-left", color="black"),
                    size="sm",
                    background_color="transparent",
                    _hover={
                        "backgroundColor": rx.color_mode_cond(
                            light="#fafafa", dark="transparent"
                        ),
                        "color": rx.color_mode_cond(light="#000", dark="#000"),
                        "cursor": "pointer",
                        "boxShadow": "0 4px 6px rgba(150, 150, 150, 0.4)",
                        "transform": "translateY(-2px)",
                        "transition": "all 0.3s ease",
                    },
                    border="1px solid transparent",
                    border_radius="md",
                    transition="all 0.2s ease",
                    on_click=TrackingState.go_to_login,  # Agregamos esta línea
                ),
                rx.text(
                    "Rastreo de envio", text_align="center", flex="1", color="black"
                ),
                rx.box(width="24px"),  # Espacio para equilibrar el botón
                width="100%",
                justify="space-between",
                align="center",
            ),
            size="2xl",
            background_color="white",
            border="none",
            box_shadow="0 2px 4px rgba(0, 0, 0, 0.4)",
            border_bottom_left_radius="10px",
            border_bottom_right_radius="10px",
            width="100%",
            margin="0",
            fontWeihgt="bold",
            fontFamily="Arial",
            fontSize="2rem",
            lineHeight="1.5",
        ),
        # Contenido
        rx.flex(
            # formulario para consultar la guia
            rx.box(
                rx.container(
                    rx.vstack(
                        rx.text("Tipo de paquete", color="black"),
                        rx.select.root(
                            rx.select.trigger(
                                placeholder="Selecciona una opción",
                                color_scheme="orange",
                                color="black",
                                width="100%",
                                style={
                                    "color": "black",
                                    "backgroundColor": "rgba(255, 255, 255, 0.4)",
                                    "border": "1px solid rgba(0, 0, 0, 0.2)",
                                    "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                    "borderRadius": "20px",
                                    "span": {"color": "rgba(0, 0, 0, 0.4)"},
                                },
                            ),
                            rx.select.content(
                                rx.select.item(
                                    rx.hstack(rx.icon("box"), rx.text("Caja")),
                                    value="1",
                                ),
                                rx.select.item(
                                    rx.hstack(rx.icon("package"), rx.text("Paquete")),
                                    value="2",
                                ),
                                rx.select.item(
                                    rx.hstack(rx.icon("mail"), rx.text("Sobre")),
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
                        rx.text("Numero de la guia", color="black"),
                        rx.input(
                            rx.input.slot(rx.icon("book-user", color="black")),
                            placeholder="# de guia",
                            type="text",
                            size="3",
                            width="100%",
                            color_scheme="orange",
                            variant="surface",
                            radius="full",
                            required=True,
                            style={
                                "color": "black",
                                "backgroundColor": "rgba(255, 255, 255, 0.4)",
                                "border": "1px solid rgba(0, 0, 0, 0.2)",
                                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                "& input::placeholder": {"color": "rgba(0, 0, 0, 0.4)"},
                            },
                        ),
                    ),
                    rx.button(
                        "Consultar",
                        color="white",
                        background_color="orange",
                        style={
                            "cursor": "pointer",
                            "border": "none",
                            "padding": "1em 2em",
                            "borderRadius": "1em",
                            "fontSize": "1.5em",
                            "marginTop": "1em",
                        },
                        size="md",
                        width="100%",
                        margin="1rem 0",
                        border_radius="full",
                        on_click=TrackingState.consultar_envio,  # Agregamos esta línea
                    ),
                ),
            ),
            # contenedor que mostrara los datos de la guia
            rx.flex(
                rx.box(
                    rx.vstack(
                        # seccion izquierda
                        rx.box(
                            rx.vstack(
                                rx.box(
                                    rx.vstack(
                                        rx.text(
                                            "Estado del envio",
                                            color="black",
                                            align="center",
                                            font_size="1.5rem",
                                            font_weight="bold",
                                        ),
                                        rx.box(
                                            rx.vstack(
                                                rx.box(
                                                    rx.hstack(
                                                        rx.icon(
                                                            "package",
                                                            color="orange",
                                                        ),
                                                        rx.text(
                                                            "¡Tu pedido está en preparación!",
                                                            color="black",
                                                            align="center",
                                                            font_size="1.5rem",
                                                        ),
                                                        align="center",
                                                    ),
                                                ),
                                                rx.box(
                                                    rx.vstack(
                                                        rx.text(
                                                            "Fecha de entrega estimada",
                                                            color="black",
                                                            align="center",
                                                            font_size="20px",
                                                        ),
                                                        rx.text(
                                                            "-- -- ----",
                                                            color="rgba(0, 0, 0, 0.4)",
                                                            align="center",
                                                            font_size="18px",
                                                        ),
                                                        align="center",
                                                        justify="center",
                                                    ),
                                                ),
                                                style={
                                                    "borderTop": "1px solid rgba(0, 0, 0, 0.2)",
                                                    "borderBottom": "1px solid rgba(0, 0, 0, 0.2)",
                                                },
                                                align="center",
                                                justify="center",
                                                width="100%",
                                                direction="column",
                                            ),
                                            width="100%",
                                            height="70%",
                                        ),
                                        align="center",
                                        width="100%",
                                        height="100%",
                                    ),
                                    width="100%",
                                    height="30%",
                                    padding="20px",
                                ),
                                rx.box(
                                    rx.vstack(
                                        rx.text(
                                            "Rastreo",
                                            color="black",
                                            align="center",
                                            font_size="1.5rem",
                                            font_weight="bold",
                                        ),
                                        # Componente de rastreo interactivo
                                        TrackingList(),
                                        align="center",
                                        width="100%",
                                        height="100%",
                                    ),
                                    width="100%",
                                    height="70%",
                                    padding="20px",
                                ),
                                width="100%",
                                height="100%",
                                align="center",
                                justify="center",
                                direction="column",
                            ),
                            background_color="transparent",
                            width="40%",
                            height="100%",
                        ),
                        # seccion derecha
                        rx.box(
                            rx.vstack(
                                rx.box(
                                    rx.vstack(
                                        rx.text(
                                            "Detalles del envio",
                                            color="black",
                                            align="center",
                                            font_size="1.5rem",
                                            font_weight="bold",
                                        ),
                                        rx.box(
                                            rx.vstack(
                                                rx.box(
                                                    rx.hstack(
                                                        rx.icon(
                                                            "package",
                                                            color="orange",
                                                        ),
                                                        rx.text(
                                                            "Numero de guia",
                                                            color="black",
                                                            align="center",
                                                            font_size="1.5rem",
                                                        ),
                                                        align="center",
                                                    ),
                                                ),
                                                rx.box(
                                                    rx.vstack(
                                                        rx.text(
                                                            "-- -- ----",
                                                            color="rgba(0, 0, 0, 0.4)",
                                                            align="center",
                                                            font_size="18px",
                                                        ),
                                                        align="center",
                                                        justify="center",
                                                    ),
                                                ),
                                                style={
                                                    "borderTop": "1px solid rgba(0, 0, 0, 0.2)",
                                                    "borderBottom": "1px solid rgba(0, 0, 0, 0.2)",
                                                },
                                                align="center",
                                                justify="center",
                                                width="100%",
                                                direction="column",
                                            ),
                                            width="100%",
                                            height="70%",
                                        ),
                                        rx.box(
                                            rx.vstack(
                                                rx.box(
                                                    rx.hstack(
                                                        rx.icon(
                                                            "user",
                                                            color="orange",
                                                        ),
                                                        rx.text(
                                                            "Nombre del remitente",
                                                            color="black",
                                                            align="center",
                                                            font_size="1.5rem",
                                                        ),
                                                        align="center",
                                                    ),
                                                ),
                                                rx.box(
                                                    rx.vstack(
                                                        rx.text(
                                                            "-- -- ----",
                                                            color="rgba(0, 0, 0, 0.4)",
                                                            align="center",
                                                            font_size="18px",
                                                        ),
                                                        align="center",
                                                        justify="center",
                                                    ),
                                                ),
                                                style={
                                                    "borderTop": "1px solid rgba(0, 0, 0, 0.2)",
                                                    "borderBottom": "1px solid rgba(0, 0, 0, 0.2)",
                                                },
                                                align="center",
                                                justify="center",
                                                width="100%",
                                                direction="column",
                                            ),
                                            width="100%",
                                            height="70%",
                                        ),
                                        rx.box(
                                            rx.vstack(
                                                rx.box(
                                                    rx.hstack(
                                                        rx.icon(
                                                            "package",
                                                            color="orange",
                                                        ),
                                                        rx.text(
                                                            "Direccion de entrega",
                                                            color="black",
                                                            align="center",
                                                            font_size="1.5rem",
                                                        ),
                                                        align="center",
                                                    ),
                                                ),
                                                rx.box(
                                                    rx.vstack(
                                                        rx.text(
                                                            "-- -- ----",
                                                            color="rgba(0, 0, 0, 0.4)",
                                                            align="center",
                                                            font_size="18px",
                                                        ),
                                                        align="center",
                                                        justify="center",
                                                    ),
                                                ),
                                                style={
                                                    "borderTop": "1px solid rgba(0, 0, 0, 0.2)",
                                                    "borderBottom": "1px solid rgba(0, 0, 0, 0.2)",
                                                },
                                                align="center",
                                                justify="center",
                                                width="100%",
                                                direction="column",
                                            ),
                                            width="100%",
                                            height="70%",
                                        ),
                                        align="center",
                                        width="100%",
                                        height="100%",
                                    ),
                                    width="100%",
                                    height="55%",
                                    padding="20px",
                                ),
                                rx.box(
                                    rx.vstack(
                                        rx.text(
                                            "Datos del paquete",
                                            color="black",
                                            align="center",
                                            font_size="1.5rem",
                                            font_weight="bold",
                                        ),
                                        # Componente de datos del paquete
                                        rx.box(
                                            rx.vstack(
                                                rx.box(
                                                    rx.vstack(
                                                        rx.box(
                                                            rx.vstack(
                                                                rx.box(
                                                                    rx.hstack(
                                                                        rx.text(
                                                                            "Tipo",
                                                                            color="black",
                                                                            align="center",
                                                                            font_size="1.5rem",
                                                                        ),
                                                                        rx.text(
                                                                            "----------------",
                                                                            color="rgba(0, 0, 0, 0.4)",
                                                                        ),
                                                                        align="center",
                                                                        justify="center",
                                                                    ),
                                                                ),
                                                                rx.box(
                                                                    rx.hstack(
                                                                        rx.text(
                                                                            "Cantidad",
                                                                            color="black",
                                                                            align="center",
                                                                            font_size="1.5rem",
                                                                        ),
                                                                        rx.text(
                                                                            "----------------",
                                                                            color="rgba(0, 0, 0, 0.4)",
                                                                        ),
                                                                        align="center",
                                                                        justify="center",
                                                                    ),
                                                                ),
                                                                align="center",
                                                                justify="center",
                                                            ),
                                                            width="50%",
                                                        ),
                                                        rx.box(
                                                            rx.vstack(
                                                                rx.box(
                                                                    rx.hstack(
                                                                        rx.text(
                                                                            "Peso",
                                                                            color="black",
                                                                            align="center",
                                                                            font_size="1.5rem",
                                                                        ),
                                                                        rx.text(
                                                                            "----------------",
                                                                            color="rgba(0, 0, 0, 0.4)",
                                                                        ),
                                                                        align="center",
                                                                        justify="center",
                                                                    ),
                                                                ),
                                                                rx.box(
                                                                    rx.hstack(
                                                                        rx.text(
                                                                            "Tipo de envio",
                                                                            color="black",
                                                                            align="center",
                                                                            font_size="1.5rem",
                                                                        ),
                                                                        rx.text(
                                                                            "----------------",
                                                                            color="rgba(0, 0, 0, 0.4)",
                                                                        ),
                                                                        align="center",
                                                                        justify="center",
                                                                    ),
                                                                ),
                                                                align="center",
                                                                justify="center",
                                                            ),
                                                            width="50%",
                                                        ),
                                                        width="100%",
                                                        direction="row",
                                                    ),
                                                    width="100%",
                                                ),
                                                rx.box(
                                                    rx.vstack(
                                                        rx.box(
                                                            rx.hstack(
                                                                rx.text(
                                                                    "Observaciones",
                                                                    color="black",
                                                                    align="center",
                                                                    font_size="1.5rem",
                                                                ),
                                                                rx.text(
                                                                    "----------------",
                                                                    color="rgba(0, 0, 0, 0.4)",
                                                                    align="center",
                                                                    font_size="18px",
                                                                ),
                                                                align="center",
                                                                justify="center",
                                                            ),
                                                            width="50%",
                                                        ),
                                                        rx.box(
                                                            rx.hstack(
                                                                rx.text(
                                                                    "Total $",
                                                                    color="orange",
                                                                    align="center",
                                                                    font_weight="bold",
                                                                    font_size="1.5rem",
                                                                ),
                                                                rx.text(
                                                                    "----------------",
                                                                    color="rgba(0, 0, 0, 0.4)",
                                                                    align="center",
                                                                    font_size="18px",
                                                                ),
                                                                align="center",
                                                                justify="center",
                                                            ),
                                                            width="50%",
                                                        ),
                                                        direction="row",
                                                    ),
                                                    width="100%",
                                                ),
                                                width="100%",
                                                direction="column",
                                            ),
                                            align="center",
                                            justify="center",
                                            height="-webkit-fill-available",
                                            width="100%",
                                            style={
                                                "borderTop": "1px solid rgba(0, 0, 0, 0.2)",
                                                "borderBottom": "1px solid rgba(0, 0, 0, 0.2)",
                                            },
                                        ),
                                        align="center",
                                        width="100%",
                                        height="100%",
                                    ),
                                    width="100%",
                                    height="70%",
                                ),
                                width="100%",
                                height="100%",
                                align="center",
                                justify="center",
                                direction="column",
                            ),
                            background_color="transparent",
                            width="60%",
                            height="100%",
                        ),
                        width="100%",
                        direction="row",
                    ),
                    style={
                        "display": "flex",  # Asegura que el contenedor principal use flexbox
                        "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                        "borderRadius": "10px",
                        "backgroundColor": "rgba(255, 255, 255, 0.4)",
                    },
                    flex_grow="1",
                    width="100%",
                    height="100%",
                ),
                padding="20px",
                flex_direction="column",
                flex_grow="1",
                width="100%",
            ),
            direction="column",
            flex_grow="1",
            width="100%",
        ),
        title="Tracking",
        display="flex",
        background_color="white",
        min_height="100vh",  # Ensure the container takes full viewport height
        spacing="0",
    )


def TrackingList() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.list.unordered(
                rx.list.item(
                    rx.hstack(
                        rx.icon(
                            "minus",
                            color="orange",
                            style={
                                "transform": "rotate(90deg)",
                                "display": "inline-block",
                            },
                        ),
                    ),
                ),
                rx.list.item(
                    rx.hstack(
                        rx.box(
                            rx.icon(
                                "package",
                                color="orange",
                            ),
                            style={
                                "border": "1px solid orange",
                                "borderRadius": "20px",
                                "padding": "5px",
                                "alignItems": "center",
                            },
                        ),
                        rx.text(
                            "Pedido 1: En preparación",
                            color="black",
                        ),
                        align="center",
                        justify="center",
                    )
                ),
                rx.list.item(
                    rx.hstack(
                        rx.icon(
                            "minus",
                            color="black",
                            style={
                                "transform": "rotate(90deg)",
                                "display": "inline-block",
                            },
                        ),
                    ),
                ),
                rx.list.item(
                    rx.hstack(
                        rx.icon(
                            "truck",
                            color="gray",
                        ),
                        rx.text(
                            "Pedido 2: En camino",
                            color="black",
                        ),
                    )
                ),
                rx.list.item(
                    rx.hstack(
                        rx.icon(
                            "minus",
                            color="black",
                            style={
                                "transform": "rotate(90deg)",
                                "display": "inline-block",
                            },
                        ),
                    ),
                ),
                rx.list.item(
                    rx.hstack(
                        rx.icon(
                            "circle_check_big",
                            color="gray",
                        ),
                        rx.text(
                            "Pedido 3: Entregado",
                            color="black",
                        ),
                    )
                ),
                rx.list.item(
                    rx.hstack(
                        rx.icon(
                            "minus",
                            color="black",
                            style={
                                "transform": "rotate(90deg)",
                                "display": "inline-block",
                            },
                        ),
                    ),
                ),
                list_style_type="none",
            ),
            style={
                "borderTop": "1px solid rgba(0, 0, 0, 0.2)",
                "borderBottom": "1px solid rgba(0, 0, 0, 0.2)",
            },
            align="center",
            justify="center",
            width="100%",
            direction="column",
        ),
        width="100%",
        height="70%",
        padding="20px",
    )
