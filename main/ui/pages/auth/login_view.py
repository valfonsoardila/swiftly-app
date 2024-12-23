import reflex as rx
from reflex_simpleicons import simpleicons
from main.ui.states.userState import UserState


@rx.page(route="/login", title="Login")
def login_view() -> rx.Component:
    return rx.hstack(
        rx.box(
            style={
                "position": "absolute",
                "top": "0",
                "left": "0",
                "right": "0",
                "bottom": "0",
                "background": "url('/design/diseño-b.png')",
                "backgroundSize": "15% auto",
                "backgroundPosition": "center",
                "backgroundRepeat": "repeat",
                "backgroundAttachment": "fixed",
                "opacity": "0.3",
                "zIndex": "0",
            },
        ),
        rx.flex(
            rx.hstack(
                rx.flex(
                    rx.card(
                        rx.vstack(
                            rx.flex(
                                rx.center(
                                    rx.image(
                                        src="/ico/logo.png",
                                        width="40%",
                                        border_radius="25%",
                                    ),
                                    rx.heading(
                                        "Sign in to your account",
                                        size="6",
                                        as_="h2",
                                        width="100%",
                                        align="center",
                                        style={
                                            "color": "black",
                                            "fontWeight": "bold",
                                        },
                                    ),
                                    rx.hstack(
                                        rx.text(
                                            "New here?",
                                            size="3",
                                            text_align="center",
                                            style={
                                                "color": "black",
                                            },
                                        ),
                                        rx.link(
                                            "Sign up",
                                            size="3",
                                            text_align="center",
                                            color="black",
                                            underline="always",
                                            style={
                                                "color": "black",
                                                "fontWeight": "bold",
                                            },
                                            href="/signup",
                                        ),
                                        spacing="2",
                                        opacity="0.8",
                                        width="100%",
                                        justify="center",
                                        align="center",
                                    ),
                                    justify="center",
                                    align="center",
                                    direction="column",
                                ),
                                justify="start",
                                direction="column",
                                spacing="4",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text(
                                    "Email address",
                                    size="3",
                                    weight="medium",
                                    text_align="left",
                                    width="100%",
                                    style={
                                        "color": "black",
                                        "fontWeight": "bold",
                                    },
                                ),
                                rx.input(
                                    rx.input.slot(rx.icon("user")),
                                    placeholder="user@gmail.com",
                                    type="email",
                                    size="3",
                                    width="100%",
                                    on_change=UserState.set_email,
                                    color_scheme="orange",
                                    variant="surface",
                                    radius="full",
                                    required=True,
                                ),
                                spacing="2",
                                justify="start",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.hstack(
                                    rx.text(
                                        "Password",
                                        size="3",
                                        weight="medium",
                                        style={
                                            "color": "black",
                                            "fontWeight": "bold",
                                        },
                                    ),
                                    rx.link(
                                        "Forgot password?",
                                        size="3",
                                        color="black",
                                        color_scheme="orange",
                                        underline="always",
                                        style={
                                            "color": "black",
                                            "fontWeight": "bold",
                                        },
                                        href="/forgot-password",
                                    ),
                                    justify="between",
                                    width="100%",
                                ),
                                rx.input(
                                    rx.input.slot(rx.icon("lock")),
                                    placeholder="Enter your password",
                                    type="password",
                                    size="3",
                                    width="100%",
                                    on_change=UserState.set_password,
                                    color_scheme="orange",
                                    variant="surface",
                                    radius="full",
                                    required=True,
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    "Sign in",
                                    size="large",
                                    width="100%",
                                    style={
                                        "color": "white",
                                        "backgroundColor": "black",
                                        "border": "none",
                                        "padding": "1em 2em",
                                        "borderRadius": "1em",
                                        "cursor": "pointer",
                                        "fontSize": "20px",
                                    },
                                    _hover={
                                        "backgroundColor": "#333333",
                                        "transform": "scale(1.05)",
                                        "transition": "transform 0.2s ease",
                                    },
                                    on_click=UserState.on_login_button_click,
                                ),
                                width="100%",
                            ),
                            rx.hstack(
                                rx.divider(
                                    margin="0",
                                    style={
                                        "backgroundColor": "rgba(0,0,0,0.5)",
                                    },
                                ),
                                rx.text(
                                    "Or continue with",
                                    white_space="nowrap",
                                    weight="medium",
                                    style={
                                        "color": "black",
                                        "fontWeight": "bold",
                                    },
                                ),
                                rx.divider(
                                    margin="0",
                                    style={
                                        "backgroundColor": "rgba(0,0,0,0.5)",
                                    },
                                ),
                                align="center",
                                width="100%",
                            ),
                            rx.center(
                                rx.icon_button(
                                    rx.image(
                                        src="/svg/google_icon.svg",
                                        width="24px",
                                        height="24px",
                                    ),
                                    variant="soft",
                                    size="3",
                                    style={
                                        "backgroundColor": "rgba(255,255,255,0.8)",
                                        "border": "none",
                                        "borderRadius": "30%",
                                        "cursor": "pointer",
                                    },
                                ),
                                rx.icon_button(
                                    rx.icon(tag="github"),
                                    variant="soft",
                                    size="3",
                                    style={
                                        "color": "white",
                                        "backgroundColor": "rgba(0,0,0,0.8)",
                                        "border": "none",
                                        "borderRadius": "30%",
                                        "cursor": "pointer",
                                    },
                                ),
                                rx.icon_button(
                                    rx.icon(tag="facebook"),
                                    variant="soft",
                                    size="3",
                                    style={
                                        "color": "white",
                                        "backgroundColor": "rgba(59,89,152,0.8)",
                                        "border": "none",
                                        "borderRadius": "30%",
                                        "cursor": "pointer",
                                    },
                                ),
                                spacing="4",
                                direction="row",
                                width="100%",
                            ),
                            spacing="6",
                            width="100%",
                        ),
                        size="4",
                        max_width="28em",
                        width="100%",
                        style={
                            "background": "linear-gradient(135deg, rgba(255,255,255, 0.42) 0%, rgba(224,224,224, 0.24) 100%)",
                        },
                    ),
                    filter="drop-shadow(0px 0px 10px rgba(0,0,0,0.1))",
                    justify="center",
                    align="center",
                    style={
                        "position": "relative",
                        "height": "100%",
                        "width": "100%",
                    },
                ),
                justify="center",
                align="center",
                height="100%",
                width="90%",
            ),
            align="center",
            justify="center",
            height="100%",
            width="100%",
        ),
        background="linear-gradient(45deg, rgba(255,193,7) 0%, rgba(255,152,0) 25%, rgba(255,113,34) 50%, rgba(242, 116,5) 100%)",
        width="-webkit-fill-available",
        height="100vh",
        style={
            "position": "relative",
            "height": "100%",
            "width": "100%",
        },
    )
