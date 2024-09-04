import reflex as rx
from reflex_simpleicons import simpleicons
from app.views.viewState.userState import UserState
from app.server.models.guide import Guide
from app.server.models.sender import Sender


class StateSidebar(rx.State):
    show_sidebar: bool = False

    def toggle_sidebar(self):
        self.show_sidebar = not self.show_sidebar


@rx.page(route="/dashboard")
def dashboard_view() -> rx.Component:
    data = [
        {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
        {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
        {"name": "Page C", "uv": 2000, "pv": 9800, "amt": 2290},
        {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
        {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
        {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
        {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
    ]
    return rx.box(  # Contenedor principal adaptado a toda la pantalla
        rx.flex(  # Flexbox para centrar el contenido con dimensiones en porcentajes
            rx.vstack(
                # Header
                rx.drawer.root(
                    rx.drawer.trigger(
                        rx.hstack(
                            rx.heading(
                                rx.hstack(
                                    rx.button(
                                        rx.icon(tag="menu"),
                                        size="sm",
                                        background_color="transparent",
                                        on_click=StateSidebar.toggle_sidebar,
                                        _hover={
                                            "backgroundColor": rx.color_mode_cond(
                                                light="#fafafa", dark="transparent"
                                            ),
                                            "color": rx.color_mode_cond(
                                                light="#000", dark="#fff"
                                            ),
                                            "cursor": "pointer",
                                            "boxShadow": "0 4px 6px rgba(150, 150, 150, 0.4)",
                                            "transform": "translateY(-2px)",
                                            "transition": "all 0.3s ease",
                                        },
                                        border="1px solid transparent",
                                        border_radius="md",
                                        transition="all 0.2s ease",
                                    ),
                                    rx.text(
                                        "Dashboard",
                                        text_align="center",
                                        flex="1",
                                        background_color="rgba(0, 0, 0, 0.8)",
                                        background_clip="text",
                                        webkit_background_clip="text",  # Soporte para navegadores basados en WebKit
                                        text_fill_color="transparent",  # Hacer el texto transparente para mostrar el gradiente
                                        font_size="2xl",  # Opcional: ajustar el tamaño de la fuente
                                    ),
                                    rx.box(
                                        width="24px"
                                    ),  # Espacio para equilibrar el botón
                                    width="100%",
                                    justify="space-between",
                                    align="center",
                                ),
                                size="2xl",
                                background_color="rgba(255, 255, 255, 0.9)",
                                border="none",
                                box_shadow="0 2px 4px rgba(0, 0, 0, 0.4)",
                                border_radius="20px",
                                width="100%",
                                margin="0",
                                fontWeihgt="bold",
                                fontFamily="Arial",
                                fontSize="2rem",
                                lineHeight="1.5",
                            ),
                            width="100%",
                            justify="space-between",
                            align="center",
                        )
                    ),
                    rx.drawer.overlay(z_index="5"),
                    rx.drawer.portal(
                        rx.drawer.content(
                            rx.dialog.title(""),  # Título del diálogo (necesario)
                            rx.flex(
                                rx.drawer.close(
                                    rx.box(
                                        rx.button(
                                            # icono flecha izquierda
                                            rx.icon(tag="arrow-left", color="black"),
                                            size="sm",
                                            background_color="transparent",
                                            on_click=StateSidebar.toggle_sidebar,
                                            style={
                                                "_hover": {
                                                    "background_color": rx.color_mode_cond(
                                                        light="transparent",
                                                        dark="transparent",
                                                    ),
                                                    "color": rx.color_mode_cond(
                                                        light="#000", dark="#fff"
                                                    ),
                                                    "cursor": "pointer",
                                                    "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.4)",
                                                    "transform": "translateY(-2px)",
                                                    "transition": "all 0.3s ease",
                                                },
                                                "border": "1px solid transparent",
                                                "border_radius": "md",
                                                "transition": "all 0.2s ease",
                                            },
                                        )
                                    )
                                ),
                                sidebar_bottom_profile(),
                                align_items="start",
                                direction="column",
                            ),
                            top="auto",
                            right="auto",
                            height="100%",
                            width="20em",
                            padding="2em",
                            background_color="rgba(255, 255, 255, 0.4)",
                        )
                    ),
                    direction="left",
                ),
                # Main Content with two vertical sections side by side
                rx.hstack(
                    rx.hstack(
                        rx.vstack(
                            rx.card(
                                rx.vstack(
                                    # Titulo
                                    rx.box(
                                        rx.heading(
                                            "Cantidad de Guias por mes",
                                            size="2xl",
                                            color="rgba(0, 0, 0, 0.8)",
                                            align="center",
                                        ),
                                        width="100%",
                                    ),
                                    # Contenido
                                    rx.box(
                                        rx.vstack(
                                            rx.recharts.bar_chart(
                                                rx.recharts.graphing_tooltip(),
                                                rx.recharts.bar(
                                                    data_key="uv",
                                                    stroke="#8884d8",
                                                    fill="#8884d8",
                                                ),
                                                rx.recharts.bar(
                                                    data_key="pv",
                                                    stroke="#82ca9d",
                                                    fill="#82ca9d",
                                                ),
                                                rx.recharts.x_axis(data_key="name"),
                                                rx.recharts.y_axis(),
                                                data=data,
                                                sync_id="1",
                                                width="100%",
                                                height=200,
                                            ),
                                            rx.recharts.composed_chart(
                                                rx.recharts.area(
                                                    data_key="uv",
                                                    stroke="#8884d8",
                                                    fill="#8884d8",
                                                ),
                                                rx.recharts.line(
                                                    data_key="pv",
                                                    type_="monotone",
                                                    stroke="#ff7300",
                                                ),
                                                rx.recharts.x_axis(data_key="name"),
                                                rx.recharts.y_axis(),
                                                rx.recharts.graphing_tooltip(),
                                                rx.recharts.brush(
                                                    data_key="name",
                                                    height=30,
                                                    stroke="#8884d8",
                                                ),
                                                data=data,
                                                sync_id="1",
                                                width="100%",
                                                height=250,
                                            ),
                                            width="100%",
                                            height="100%",
                                            align="center",
                                            justify="center",
                                        ),
                                        width="100%",
                                        height="100%",
                                    ),
                                    direction="column",
                                    height="100%",
                                ),
                                height="70%",
                                width="100%",
                                style={
                                    "border": "none !important",
                                    "borderRadius": "none",
                                    "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                },
                                background_color="rgba(255, 255, 255, 0.5)",
                            ),
                            rx.card(
                                rx.vstack(
                                    # Titulo
                                    rx.box(
                                        rx.heading(
                                            "Clientes",
                                            size="2xl",
                                            color="rgba(0, 0, 0, 0.8)",
                                            align="center",
                                        ),
                                        width="100%",
                                    ),
                                    # Contenido
                                    rx.box(
                                        rx.vstack(
                                            rx.hstack(
                                                item_list_client(
                                                    "/logo.png", "Cliente 1", "/#"
                                                ),
                                                height="100%",
                                                width="100%",
                                                align="center",
                                                justify="center",
                                            ),
                                            height="100%",
                                            width="100%",
                                        ),
                                        height="100%",
                                        width="100%",
                                        display="flex",
                                    ),
                                    direction="column",
                                    height="100%",
                                ),
                                height="30%",
                                width="100%",
                                style={
                                    "border": "none !important",
                                    "--card-border-width": "0",
                                },
                            ),
                            width="70%",
                            height="100%",
                            spacing="2",
                        ),
                        rx.card(
                            rx.vstack(
                                rx.box(
                                    rx.vstack(
                                        # Titulo
                                        rx.box(
                                            rx.heading(
                                                "Guias Pendientes",
                                                size="2xl",
                                                color="rgba(0, 0, 0, 0.8)",
                                                align="center",
                                            ),
                                            width="100%",
                                        ),
                                        # Contenido
                                        rx.box(
                                            rx.vstack(
                                                item_list_guide(
                                                    "route", "Guia 1", "/#"
                                                ),
                                            ),
                                            width="100%",
                                            height="100%",
                                        ),
                                        direction="column",
                                    ),
                                    width="100%",
                                ),
                                rx.box(),
                                width="100%",
                                direction="column",
                            ),
                            width="30%",
                            height="100%",
                            style={
                                "borderRight": "1px solid #ccc",
                                "borderLeft": "1px solid #ccc",
                                "--card-border-width": "0",
                            },
                        ),
                        width="100%",
                        height="-webkit-fill-available",
                        padding="16px",  # Ajusta este valor según necesites
                        box_sizing="border-box",
                    ),
                    width="100%",
                    height="96vh",
                    spacing="2",
                ),
                title="Dashboard",
                width="100%",
                spacing="0",
            ),
            width="98%",
            height="98%",
            style={
                "background": "rgba(255, 255, 255, 0.82)",
                "border": "1px solid #ccc",
                "borderRadius": "20px",
                "boxShadow": "0 0.5px 2px rgba(0, 0, 0, 0.4)",
            },
        ),
        width="100%",
        height="100vh",  # Esto hará que el box ocupe toda la altura de la pantalla
        # imagen de fondo
        background_image="url('/bg.gif')",
        style={
            "backgroundSize": "cover",
            "backgroundPosition": "center",
            "backgroundRepeat": "no-repeat",
            "alignItems": "center",
            "justifyContent": "center",
            "display": "flex",
        },
    )


def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            color="black",
            align="center",
            style={
                "_hover": {
                    "bg": "rgba(220, 220, 220, 0.8)",
                    "color": "rgba(242, 116, 5, 0.9)",
                },
                "borderRadius": "0.5rem",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Dashboard", "layout-dashboard", "/#"),
        sidebar_item("Guias", "book", "/#"),
        sidebar_item("Envios", "route", "/#"),
        sidebar_item("Clientes", "user", "/#"),
        spacing="1",
        width="100%",
    )


def sidebar_bottom_profile() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/logo.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Menu", size="7", weight="bold", color="black"),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                rx.spacer(),
                rx.vstack(
                    rx.vstack(
                        sidebar_item("Settings", "settings", "/#"),
                        sidebar_item("Log out", "log-out", "/login"),
                        spacing="1",
                        width="100%",
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.icon_button(
                            rx.icon("user"),
                            size="3",
                            radius="full",
                        ),
                        rx.vstack(
                            rx.box(
                                rx.text(
                                    UserState.load_user,
                                    size="3",
                                    weight="bold",
                                ),
                                rx.text(
                                    UserState.load_user,
                                    size="2",
                                    weight="medium",
                                ),
                                width="100%",
                            ),
                            spacing="0",
                            align="start",
                            justify="start",
                            width="100%",
                        ),
                        padding_x="0.5rem",
                        align="center",
                        justify="start",
                        width="100%",
                    ),
                    width="100%",
                    spacing="5",
                ),
                spacing="5",
                # position="fixed",
                # left="0px",
                # top="0px",
                # z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                bg="transparent",
                align="start",
                # height="100%",
                height="650px",
                width="16em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(rx.icon("align-justify", size=30)),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(rx.icon("x", size=30)),
                                width="100%",
                            ),
                            sidebar_items(),
                            rx.spacer(),
                            rx.vstack(
                                rx.vstack(
                                    sidebar_item(
                                        "Settings",
                                        "settings",
                                        "/#",
                                    ),
                                    sidebar_item(
                                        "Log out",
                                        "log-out",
                                        "/login",
                                    ),
                                    width="100%",
                                    spacing="1",
                                ),
                                rx.divider(margin="0"),
                                rx.hstack(
                                    rx.icon_button(
                                        rx.icon("user"),
                                        size="3",
                                        radius="full",
                                    ),
                                    rx.vstack(
                                        rx.box(
                                            rx.text(
                                                UserState.load_user,
                                                size="3",
                                                weight="bold",
                                            ),
                                            rx.text(
                                                "user@reflex.dev",
                                                size="2",
                                                weight="medium",
                                            ),
                                            width="100%",
                                        ),
                                        spacing="0",
                                        justify="start",
                                        width="100%",
                                    ),
                                    padding_x="0.5rem",
                                    align="center",
                                    justify="start",
                                    width="100%",
                                ),
                                width="100%",
                                spacing="5",
                            ),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg="transparent",
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )


# componente para la lista de guias pendientes
def item_list_guide(icon: str, text: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, color="black"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            justify="center",
            style={
                "_hover": {
                    "bg": "rgba(20, 20, 20, 0.8)",
                    "color": "orange",
                },
                "borderRadius": "0.5rem",
                "border": "1px solid #ccc",
                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
            },
        ),
        background_color="rgba(255, 255, 255, 0.5)",
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def item_list_client(img: str, text: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            # cargare la imagen desde la base de datos
            rx.image(src=img, width="2.25em", height="auto", border_radius="25%"),
            rx.text(text, color="black"),
            padding_x="0.5rem",
            padding_y="0.75rem",
            margin_x="0.5rem",
            align="center",
            justify="center",
            style={
                "_hover": {
                    "bg": "rgba(20, 20, 20, 0.8)",
                    "color": "orange",
                },
                "borderRadius": "0.5rem",
                "border": "1px solid #ccc",
                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
            },
            background_color="rgba(255, 255, 255, 0.5)",
            height="90%",
            width="30%",
            direction="column",
        ),
        align_items="center",
        href=href,
        underline="none",
        weight="medium",
        width="100%",
        height="100%",
        display="flex",
    )
