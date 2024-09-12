import reflex as rx
from main.ui.states.userState import UserState
from main.server.models.v1.Guide import Guide
from main.server.models.v1.Sender import Sender
from main.ui.views.app.modules.guides_view import guides_view
from main.ui.views.app.modules.shipping_view import shipping_view
from main.ui.views.app.modules.clients_view import clients_view
from main.ui.views.app.modules.dashboard_view import dashboard_view
from main.ui.views.app.modules.settings_view import settings_view

# import models v1
from main.server.models.v1.Guide import Guide
from main.server.models.v1.Sender import Sender
from main.server.models.v1.Recipient import Recipient

# import models v2
from main.server.models.v2.Guide import Guide

# import states
from main.ui.states.pageState import StatePage


class StateSidebar(rx.State):
    show_sidebar: bool = False

    def toggle_sidebar(self):
        self.show_sidebar = not self.show_sidebar


@rx.page(route="/app", title="Dashboard")
def app_view() -> rx.Component:
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
                                        rx.icon(tag="menu", color="black"),
                                        size="sm",
                                        background_color="transparent",
                                        on_click=StateSidebar.toggle_sidebar,
                                        _hover={
                                            "backgroundColor": rx.color_mode_cond(
                                                light="rgba(150, 150, 150, 0.4)",
                                                dark="transparent",
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
                                    rx.box(
                                        rx.hstack(
                                            rx.text(
                                                StatePage.labael_component_route,
                                                text_align="center",
                                                align="center",
                                                font_size="30px",
                                            ),
                                            style={
                                                "color": "rgba(255, 255, 255, 0.9)",
                                                "transition": "all 0.3s ease",
                                                "_hover": {
                                                    "color": "none",
                                                    "backgroundImage": "linear-gradient(145deg, #F27405 10%, #F20505 90%)",
                                                    "WebkitBackgroundClip": "text",
                                                    "WebkitTextFillColor": "transparent",
                                                    "transition": "all 0.3s ease",
                                                },
                                            },
                                            align="center",
                                            justify="center",
                                        ),
                                        height="100%",
                                        width="-webkit-fill-available",
                                    ),
                                    rx.box(
                                        width="24px"
                                    ),  # Espacio para equilibrar el botón
                                    width="100%",
                                    justify="space-between",
                                    align="center",
                                ),
                                size="2xl",
                                background_color="rgba(255, 255, 255, 0.4)",
                                _hover={
                                    "backgroundColor": "rgba(255, 255, 255, 0.82)",
                                    "cursor": "pointer",
                                },
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
                            rx.dialog.description(""),
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
                            background_color="rgba(255, 255, 255, 0.9)",
                        )
                    ),
                    direction="left",
                ),
                # Main Content with two vertical sections side by side
                rx.hstack(
                    rx.flex(
                        rx.vstack(
                            rx.match(
                                StatePage.current_route,
                                (
                                    "dashboard",
                                    rx.box(
                                        dashboard_view(), width="100%", height="100%"
                                    ),
                                ),
                                (
                                    "guides",
                                    rx.box(guides_view(), width="100%", height="100%"),
                                ),
                                (
                                    "shipping",
                                    rx.box(
                                        shipping_view(), width="100%", height="100%"
                                    ),
                                ),
                                (
                                    "clients",
                                    rx.box(clients_view(), width="100%", height="100%"),
                                ),
                                (
                                    "settings",
                                    rx.box(
                                        settings_view(), width="100%", height="100%"
                                    ),
                                ),
                                rx.box(rx.text("Página no encontrada"), width="100%"),
                            ),
                            width="100%",
                        ),
                        style={
                            "background": "rgba(255, 255, 255, 0.82)",
                            "border": "1px solid #ccc",
                            "borderRadius": "20px",
                            "boxShadow": "0 0.5px 2px rgba(0, 0, 0, 0.4)",
                        },
                        width="100%",
                        height="100%",
                    ),
                    width="100%",
                    height="96vh",
                    spacing="2",
                ),
                title="Dashboard",
                width="100%",
                spacing="2",
            ),
            width="98%",
            height="98%",
        ),
        width="100%",
        height="100vh",  # Esto hará que el box ocupe toda la altura de la pantalla
        # imagen de fondo
        background_image="url('/img/bg.jpg')",
        style={
            "backgroundSize": "cover",
            "backgroundPosition": "center",
            "backgroundRepeat": "no-repeat",
            "alignItems": "center",
            "justifyContent": "center",
            "display": "flex",
        },
    )


def sidebar_item(
    text: str, icon: str, route: str, is_logout: bool = False
) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.icon(icon),
            rx.text(text),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            color="black",
            align="center",
        ),
        on_click=StatePage.logout if is_logout else lambda: StatePage.set_route(route),
        width="100%",
        bg="transparent",
        border="none",
        _hover={
            "bg": "rgba(220, 220, 220, 0.8)",
            "color": "rgba(242, 116, 5, 0.9)",
            "cursor": "pointer",
        },
        border_radius="0.5rem",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Dashboard", "layout-dashboard", "dashboard"),
        sidebar_item("Guias", "book", "guides"),
        sidebar_item("Envios", "route", "shipping"),
        sidebar_item("Clientes", "user", "clients"),
        spacing="1",
        width="100%",
    )


def sidebar_bottom_profile() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/ico/logo.png",
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
                        sidebar_item("Settings", "settings", "settings"),
                        sidebar_item("Log out", "log-out", "login", is_logout=True),
                        spacing="1",
                        width="100%",
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.icon_button(
                            rx.avatar(
                                src=UserState.load_user_image,
                                size="4",
                                width="100%",
                                height="100%",
                                object_fit="cover",
                            ),
                            size="4",
                            radius="full",
                            padding="0",
                        ),
                        rx.vstack(
                            rx.box(
                                rx.text(
                                    UserState.load_user_username,
                                    size="3",
                                    weight="bold",
                                    color="black",
                                ),
                                rx.text(
                                    UserState.load_user_email,
                                    size="2",
                                    weight="medium",
                                    color="black",
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
                                        "settings",
                                    ),
                                    sidebar_item(
                                        "Log out", "log-out", "login", is_logout=True
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
                                                UserState.load_user_email,
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
