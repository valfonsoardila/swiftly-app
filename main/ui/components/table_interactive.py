import reflex as rx
from typing import List


class DataTableState(rx.State):
    data: List[List[str]] = [
        [
            "2023-09-22",
            "TR123456",
            "Box",
            "1",
            "5.2 kg",
            "Juan Pérez",
            "María García",
            "Tech Solutions",
            "Calle Principal 123, Ciudad",
            "Express",
        ],
        [
            "2023-09-23",
            "TR789012",
            "Envelope",
            "1",
            "0.5 kg",
            "Ana Rodríguez",
            "Carlos López",
            "Marketing Inc.",
            "Avenida Central 456, Pueblo",
            "Standard",
        ],
        [
            "2023-09-24",
            "TR345678",
            "Pallet",
            "1",
            "150 kg",
            "Empresa A",
            "Empresa B",
            "Manufacturing Co.",
            "Polígono Industrial 789, Villa",
            "Freight",
        ],
    ]

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
        "Actions",
    ]

    def update_item(self, item_id: int):
        print(f"Actualizar item {item_id}")

    def delete_item(self, item_id: int):
        print(f"Eliminar item {item_id}")


class TextFieldPageState(rx.State):
    text: str = "1"


def show_item(item: List[str]):
    return rx.table.row(
        rx.foreach(
            item[:-1],
            lambda cell: rx.table.cell(
                cell,
                style={
                    "borderRight": rx.color_mode_cond(
                        light="1px solid rgba(0, 0, 0, 0.05)",
                        dark="1px solid rgba(50, 254, 165, 0.7)",
                    ),
                    "boxShadow": rx.color_mode_cond(
                        light="0 2px 4px rgba(0, 0, 0, 0.1)",
                        dark="inset 0 -1px transparent",
                    ),
                    "color": rx.color_mode_cond(
                        light="black",
                        dark="white",
                    ),
                    "text_align": "center",
                },
            ),
        ),
        rx.table.cell(
            rx.hstack(
                rx.button(
                    rx.icon("pencil", height="20px", width="20px"),
                    on_click=lambda: DataTableState.update_item(item[1]),
                    style={
                        "backgroundColor": "transparent",
                        "color": rx.color_mode_cond(
                            light="rgba(0, 0, 0, 0.4)",
                            dark="rgba(255, 255, 255, 0.4)",
                        ),
                        "border": rx.color_mode_cond(
                            light="0.5px solid rgba(0, 0, 0, 0.2)",
                            dark="0.5px solid rgba(255, 255, 255, 0.2)",
                        ),
                        "borderRadius": "50%",
                        "width": "30px",
                        "height": "30px",
                        "padding": "0",
                        "_hover": {
                            "color": "rgba(255, 160, 87)",
                            "backgroundColor": "rgba(255, 160, 87, 0.1)",
                            "border": "rgba(255, 160, 87, 0.4)",
                            "transform": "scale(1.05)",
                            "cursor": "pointer",
                        },
                    },
                ),
                rx.button(
                    rx.icon("package-x", height="20px", width="20px"),
                    on_click=lambda: DataTableState.delete_item(item[1]),
                    style={
                        "width": "30px",
                        "height": "30px",
                        "backgroundColor": "transparent",
                        "color": rx.color_mode_cond(
                            light="rgba(0, 0, 0, 0.4)",
                            dark="rgba(255, 255, 255, 0.4)",
                        ),
                        "border": rx.color_mode_cond(
                            light="0.5px solid rgba(0, 0, 0, 0.2)",
                            dark="0.5px solid rgba(255, 255, 255, 0.2)",
                        ),
                        "borderRadius": "50%",
                        "padding": "0",
                        "_hover": {
                            "color": "rgba(230, 25, 25)",
                            "backgroundColor": "rgba(230, 25, 25, 0.1)",
                            "border": "rgba(230, 25, 25, 0.4)",
                            "transform": "scale(1.05)",
                            "cursor": "pointer",
                        },
                    },
                ),
            ),
            style={
                "display": "flex",
                "justifyContent": "center",
                "gap": "10px",
                "boxShadow": rx.color_mode_cond(
                    light="0 2px 4px rgba(0, 0, 0, 0.1)",
                    dark="inset 0 -1px transparent",
                ),
            },
        ),
        style={
            "color": "black",
            "text_align": "center",
        },
    )


def table_interactive() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Search bar
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.hstack(
                            # ?: Contenedor del icono de busqueda
                            rx.box(
                                rx.button(
                                    rx.icon(
                                        "search",
                                        height="20px",
                                        width="20px",
                                        color=rx.color_mode_cond(
                                            light="gray",
                                            dark="rgba(255, 255, 255, 0.6)",
                                        ),
                                    ),
                                    style={
                                        "display": "flex",
                                        "justifyContent": "center",
                                        "alignItems": "center",
                                        "width": "100%",
                                        "height": "100%",
                                        "border": "none",
                                        "borderRadius": "20px 0 0 20px",
                                        "background": "transparent",
                                        "padding": "0",
                                    },
                                ),
                                style={
                                    "display": "flex",
                                    "justifyContent": "center",
                                    "alignItems": "center",
                                },
                                width="20px",
                                height="100%",
                            ),
                            # ? Input para la busqueda
                            rx.input(
                                placeholder="Search...",
                                width="-webkit-fill-available",
                                height="100%",
                                font_size="18px",
                                style={
                                    "& input::placeholder": {"color": "gray"},
                                    "color": rx.color_mode_cond(
                                        light="black",
                                        dark="white",
                                    ),
                                    "borderRadius": "20px",
                                    "backgroundColor": "transparent",
                                    "border": "none",
                                    "_hover": {
                                        "borderRadius": "0 20px 0 20px",
                                    },
                                },
                            ),
                            spacing="0",
                            style={
                                "display": "flex",
                                "justifyContent": "center",
                                "alignItems": "center",
                            },
                            height="100%",
                            width="100%",
                        ),
                        style={
                            "display": "flex",
                            "justifyContent": "start",
                            "alignItems": "center",
                            "background": rx.color_mode_cond(
                                light="linear-gradient(90deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8))",
                                dark=rx.color("gray", 4, alpha=True),
                            ),
                            "border": "none",
                            "borderRadius": "20px",
                            "color": rx.color_mode_cond(
                                light="gray",
                                dark="rgba(255, 255, 255, 0.6)",
                            ),
                            "_hover": {
                                "svg": {
                                    "color": rx.color_mode_cond(
                                        light="black", dark="white"
                                    )
                                },
                                "borderRadius": "20px 20px 0 20px",
                                "width": "40%",
                                "color": rx.color_mode_cond(
                                    light="black",
                                    dark="white",
                                ),
                                "cursor": "pointer",
                                "transform": "scale(1.05)",
                                "transition": "0.3s",
                            },
                        },
                        height="100%",
                        width="3%",
                    ),
                    style={
                        "display": "flex",
                        "justifyContent": "center",
                        "alignItems": "center",
                    },
                    height="100%",
                ),
                height="45px",
                width="100%",
            ),
            # Table
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.foreach(
                            DataTableState.columns,
                            lambda column: rx.table.column_header_cell(
                                column,
                                style={
                                    "text_align": "center",
                                },
                            ),
                        ),
                        style={
                            "color": rx.color_mode_cond(
                                light="black",
                                dark="white",
                            ),
                            "fontSize": "18px",
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.2)",
                        },
                    )
                ),
                rx.table.body(
                    rx.foreach(DataTableState.data, show_item),
                ),
                style={
                    "width": "-webkit-fill-available",
                    "border": "0.5px solid rgba(0, 0, 0, 0.2)",
                    "borderRadius": "20px",
                    "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.2)",
                    "backgroundColor": rx.color_mode_cond(
                        light="rgba(255, 255, 255, 0.8)",
                        dark=rx.color("gray", 4, alpha=True),
                    ),
                    "text_align": "center",
                },
            ),
            # Pagination
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.text(
                                    "Rows per page",
                                    color=rx.color_mode_cond(
                                        light="black", dark="white"
                                    ),
                                ),
                                rx.box(
                                    rx.icon(
                                        "chevron-left",
                                        height="20px",
                                        width="20px",
                                        style={
                                            "marginRight": "5px",
                                            "marginLeft": "5px",
                                        },
                                    ),
                                    style={
                                        "color": rx.color_mode_cond(
                                            light="gray",
                                            dark="white",
                                        ),
                                        "display": "flex",
                                        "justifyContent": "center",
                                        "alignItems": "center",
                                        "width": "30px",
                                        "height": "30px",
                                        "_hover": {
                                            "backgroundColor": rx.color_mode_cond(
                                                light="rgba(255, 255, 255, 0.5)",
                                                dark=rx.color(
                                                    "gray",
                                                    9,
                                                    alpha=True,
                                                ),
                                            ),
                                            "border": "1px solid rgba(0, 0, 0, .4)",
                                            "borderRadius": "50%",
                                            "cursor": "pointer",
                                        },
                                    },
                                ),
                                rx.el.input(
                                    default_value=TextFieldPageState.text,
                                    style={
                                        "textAlign": "center",
                                        "color": rx.color_mode_cond(
                                            light="gray",
                                            dark="white",
                                        ),
                                        "width": "50px",
                                        "height": "30px",
                                        "border": "none",
                                        "backgroundColor": "transparent",
                                        "textIndent": "0px",
                                    },
                                    _focus={
                                        "border": "0.2px solid black",
                                        "borderRadius": "10px",
                                        "outline": "none",  # Esto elimina el contorno predeterminado del navegador
                                    },
                                ),
                                rx.box(
                                    rx.icon(
                                        "chevron-right",
                                        height="20px",
                                        width="20px",
                                        style={
                                            "marginRight": "5px",
                                            "marginLeft": "5px",
                                        },
                                    ),
                                    style={
                                        "color": rx.color_mode_cond(
                                            light="gray",
                                            dark="white",
                                        ),
                                        "display": "flex",
                                        "justifyContent": "center",
                                        "alignItems": "center",
                                        "width": "30px",
                                        "height": "30px",
                                        "_hover": {
                                            "backgroundColor": rx.color_mode_cond(
                                                light="rgba(255, 255, 255, 0.5)",
                                                dark=rx.color(
                                                    "gray",
                                                    9,
                                                    alpha=True,
                                                ),
                                            ),
                                            "border": "1px solid rgba(0, 0, 0, .4)",
                                            "borderRadius": "50%",
                                            "cursor": "pointer",
                                        },
                                    },
                                ),
                                width="fit-content",
                                spacing="1",
                            ),
                            style={
                                "display": "flex",
                                "justifyContent": "center",
                                "alignItems": "end",
                            },
                            width="fit-content",
                        ),
                        style={
                            "display": "flex",
                            "justifyContent": "end",
                            "alignItems": "center",
                            "color": "black",
                            "border": "none",
                            "borderRadius": "20px",
                            "backgroundColor": rx.color_mode_cond(
                                light="rgba(255, 255, 255, 0.8)",
                                dark=rx.color("gray", 4, alpha=True),
                            ),
                            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.2)",
                            "padding": "0 10px",
                            "_hover": {
                                "width": "100%",
                                "transition": "0.3s",
                            },
                        },
                        height="100%",
                        width="fit-content",
                    ),
                    style={
                        "display": "flex",
                        "justifyContent": "end",
                        "alignItems": "center",
                    },
                    height="100%",
                ),
                width="100%",
                height="30px",
            ),
            spacing="2",
            width="100%",
        ),
        width="100%",
        height="100%",
    )
