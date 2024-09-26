import reflex as rx
from main.ui.states.pageState import StatePage
from main.server.controllers.user_controller import read_all_users
from typing import List, Dict
from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)

# from reflex_simpleicons import simpleicons


class DashboardState(rx.State):
    users: List[Dict[str, str]] = []

    def load_users(self):
        self.users = read_all_users()


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
    return (
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.card(
                        rx.vstack(
                            # Titulo
                            rx.box(
                                rx.heading(
                                    "Cantidad de Guias por mes",
                                    size="2xl",
                                    color=rx.color_mode_cond(
                                        light="rgba(0, 0, 0, 0.8)",
                                        dark="rgba(255, 255, 255, 0.8)",
                                    ),
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
                            "backgroundColor": rx.color_mode_cond(
                                light="rgba(255, 255, 255, 0.5)",
                                dark=rx.color("grass", 3, alpha=True),
                            ),
                            "_hover": {
                                "backgroundColor": rx.color_mode_cond(
                                    light="rgba(255, 255, 255, 0.5)",
                                    dark=rx.color("grass", 5, alpha=True),
                                ),
                                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                                "cursor": "pointer",
                            },
                        },
                    ),
                    rx.card(
                        rx.hstack(
                            rx.vstack(
                                # Titulo
                                rx.box(
                                    rx.heading(
                                        "Clientes",
                                        size="2xl",
                                        color=rx.color_mode_cond(
                                            light="rgba(0, 0, 0, 0.8)",
                                            dark="rgba(255, 255, 255, 0.8)",
                                        ),
                                        align="center",
                                    ),
                                    width="100%",
                                    height="10%",
                                ),
                                # Contenido
                                rx.box(
                                    rx.vstack(
                                        rx.hstack(
                                            rx.foreach(
                                                DashboardState.users,
                                                lambda user: item_list_client(user),
                                            ),
                                            height="100%",
                                            width="100%",
                                            align="center",
                                            justify="center",
                                        ),
                                        height="100%",
                                        width="100%",
                                    ),
                                    height="90%",
                                    width="100%",
                                    display="flex",
                                ),
                                direction="column",
                                width="60%",
                                height="100%",
                            ),
                            rx.vstack(
                                # Cards estadisticas de la aplicacion
                                rx.box(
                                    rx.heading(
                                        "Estadisticas",
                                        size="2xl",
                                        color="rgba(0, 0, 0, 0.8)",
                                        align="center",
                                    ),
                                    width="100%",
                                    height="10%",
                                ),
                                # Contenido
                                rx.box(
                                    rx.vstack(
                                        item_stat_card(
                                            "Guias",
                                            100,
                                            0,
                                            "book",
                                            "green",
                                        ),
                                        item_stat_card(
                                            "Clientes",
                                            100,
                                            0,
                                            "users",
                                            "orange",
                                        ),
                                    ),
                                    width="100%",
                                ),
                                height="100%",
                                width="40%",
                                justify="center",
                                align="center",
                            ),
                            width="100%",
                            height="100%",
                        ),
                        height="30%",
                        width="100%",
                        style={
                            "backgroundColor": rx.color_mode_cond(
                                light="rgba(255, 255, 255, 0.4)",
                                dark="rgba(0, 0, 0, 0.1)",
                            ),
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
                                        color=rx.color_mode_cond(
                                            light="rgba(0, 0, 0, 0.8)",
                                            dark="rgba(255, 255, 255, 0.8)",
                                        ),
                                        align="center",
                                    ),
                                    width="100%",
                                ),
                                # Contenido
                                rx.box(
                                    rx.vstack(
                                        item_list_guide("route", "Guia 1", "guides"),
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
            height="100%",
            on_mount=DashboardState.load_users,
        ),
    )


# componente para la lista de tarjetas de estadisticas
def item_stat_card(
    stat_name: str = "Users",
    value: int = 4200,
    prev_value: int = 3000,
    icon: str = "users",
    badge_color: LiteralAccentColor = "blue",
) -> rx.Component:
    percentage_change = (
        round(((value - prev_value) / prev_value) * 100, 2)
        if prev_value != 0
        else 0 if value == 0 else float("inf")
    )
    change = "increase" if value > prev_value else "decrease"
    arrow_icon = "trending-up" if value > prev_value else "trending-down"
    arrow_color = "grass" if value > prev_value else "tomato"
    return (
        rx.card(
            rx.vstack(
                rx.hstack(
                    rx.badge(
                        rx.icon(tag=icon, size=28),
                        color_scheme=badge_color,
                        radius="full",
                        padding="0.7rem",
                    ),
                    rx.vstack(
                        rx.heading(
                            f"{value:,}",
                            size="6",
                            weight="bold",
                            color="black",
                            font_size="20px",
                        ),
                        rx.text(
                            stat_name,
                            weight="medium",
                            color="black",
                            font_size="16px",
                        ),
                        spacing="1",
                        height="100%",
                        align_items="start",
                        width="100%",
                    ),
                    height="100%",
                    spacing="5",
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.hstack(
                        rx.icon(
                            tag=arrow_icon,
                            size=20,
                            color=rx.color(arrow_color, 9),
                        ),
                        rx.text(
                            f"{percentage_change}%",
                            size="3",
                            color="black",
                            weight="medium",
                            font_size="16px",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    rx.text(
                        f"{change} from last month",
                        size="2",
                        color="black",
                    ),
                    align="center",
                    width="100%",
                ),
                spacing="0",
            ),
            style={
                "_hover": {
                    "bg": "rgba(225, 225, 225, 0.55)",
                    "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                    "cursor": "pointer",
                },
                "backgroundColor": "rgba(255, 255, 255, 0.5)",
            },
            size="3",
            height="45%",
            width="100%",
            paddingTop="5px",
            paddingBottom="5px",
            paddingleft="20px",
            paddingRight="20px",
        ),
    )


# componente para la lista de guias pendientes
def item_list_guide(icon: str, text: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, color="black"),
            rx.text(text, color="black"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            justify="center",
            style={
                "_hover": {
                    "bg": "rgba(225, 225, 225, 0.55)",
                    "borderRadius": "0.5rem",
                    "color": "orange",
                    "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                    "cursor": "pointer",
                    "transition": "all 0.3s",
                },
                "borderRadius": "0.5rem",
                "border": "1px solid #ccc",
                "backgroundColor": "rgba(255, 255, 255, 0.5)",
            },
        ),
        on_click=StatePage.set_current_route(href),
        underline="none",
        weight="medium",
        width="100%",
    )


# componente para la lista de clientes
def item_list_client(user: dict, href="clients") -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.box(
                rx.vstack(
                    rx.image(
                        src=f"data:image/jpeg;base64,{user['image']}",
                        height="-webkit-fill-available",
                        object_fit="cover",  # Asegura que la imagen cubra el contenedor sin distorsión
                        width="-webkit-fill-available",
                    ),
                    rx.text(
                        user["username"],
                        color="white",  # Color del texto blanco para destacar sobre la imagen
                        filter="brightness(0.5)",  # Oscurece la imagen para que el texto sea legible
                        padding="0.5rem",
                        text_align="center",
                        position="absolute",  # Posiciona el texto sobre la imagen
                        bottom="20px",  # El texto se coloca en la parte inferior
                    ),
                    padding_x="0.5rem",
                    align="center",
                    justify="center",
                    width="100%",
                    height="100%",
                ),
                width="100%",
                height="100%",
                style={
                    "_hover": {
                        # verde claro
                        "bg": "rgba(225, 225, 225, 0.6)",
                        "borderRadius": "0.5rem",
                        "color": "orange",
                        "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                        "cursor": "pointer",
                        "transition": "all 0.3s",
                        "p": {
                            "background": "rgba(0, 0, 0, 0.6)",
                            "filter": "brightness(1)",
                        },
                    },
                    "borderRadius": "0.5rem",
                    "border": "1px solid #ccc",
                    "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                },
            ),
            background_color="#E8F5E9",
            height="90%",
            width="40%",
            style={
                "borderRadius": "0.5rem",
                "_hover": {
                    "width": "42%",
                    "height": "92%",
                    "transition": "all 0.3s",
                },
            },
            direction="column",
        ),
        align_items="center",
        on_click=StatePage.set_current_route(href),
        underline="none",
        weight="medium",
        width="100%",
        height="100%",
        display="flex",
    )
