import reflex as rx
from main.ui.states.shipmentGuideStateV2 import ShipmentGuideStateV2


class ModalPageState(rx.State):
    current_page: int = 0
    list_sections: list = []  # Add this line

    def next_page(self):
        if self.current_page < 2:
            self.current_page += 1

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1

    def set_sections(self, sections: list[rx.Component]):
        self.list_sections = sections

    @rx.var
    def total_pages(self) -> int:
        return len(self.list_sections)


def progress_modal(
    list_sections: list[rx.Component],
) -> rx.Component:
    return (
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
                            "background": rx.color_mode_cond(
                                light="linear-gradient(90deg, #000000 0%, #434343 100%)",
                                dark="linear-gradient(45deg, rgba(38, 38, 38) 0%, #1a1a1a 85%, rgba(50, 254, 165, 0.7) 100%)",
                            ),
                            "clipPath": "border-box",
                            "border": rx.color_mode_cond(
                                light="1px solid #000000",
                                dark="0.5px solid rgba(255, 255, 255, 0.2)",
                            ),
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
                container_sections(
                    list_sections,
                ),
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
                    "backgroundImage": rx.color_mode_cond(
                        light="url('/img/portapapeles.png')",
                        dark="url('/img/portapapeles_dark.png')",
                    ),
                    "backgroundSize": "cover",
                    "backgroundPosition": "0px -70px",
                    "backgroundRepeat": "no-repeat",
                    "ClipPath": "border-box",
                    "boxShadow": rx.color_mode_cond(
                        light="0px 0px 20px rgba(0, 0, 0, 0.2)",
                        dark="0px 0px 10px rgba(50, 254, 165, 0.7)",
                    ),
                },
            ),
        ),
    )


# Step-By-Step del modal de registro de guía
def container_sections(
    list_sections: list[rx.Component],
) -> rx.Component:
    ModalPageState.list_sections = list_sections
    return rx.box(
        rx.vstack(
            rx.match(
                ModalPageState.current_page,
                *[
                    (i, rx.box(section, width="100%", height="100%"))
                    for i, section in enumerate(list_sections)
                ],
                rx.box("Default content", width="100%", height="100%"),
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
                            on_click=ShipmentGuideStateV2.on_save_guide,
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
                style={
                    "alignItems": "center",
                },
            ),
            spacing="0",
        ),
        on_mount=lambda: ModalPageState.set_sections(list_sections),
    )
