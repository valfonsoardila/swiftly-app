import reflex as rx
from main.ui.states.pageState import StatePage
from main.server.controllers.user_controller import read_all_users
from typing import List, Dict

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
                    "bg": "rgba(225, 225, 225, 0.6)",
                    "borderRadius": "0.5rem",
                    "color": "orange",
                    "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
                    "cursor": "pointer",
                    "transition": "all 0.3s",
                },
                "borderRadius": "0.5rem",
                "border": "1px solid #ccc",
                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.4)",
            },
        ),
        background_color="rgba(255, 255, 255, 0.5)",
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
                        bottom="14px",  # El texto se coloca en la parte inferior
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
                            "background": "rgba(0, 0, 0, 0.5)",
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
            width="20%",
            style={
                "borderRadius": "0.5rem",
                "_hover": {
                    "width": "22%",
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
