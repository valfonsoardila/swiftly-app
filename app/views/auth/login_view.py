import reflex as rx


def login_view() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.card(
                rx.vstack(
                    rx.flex(
                        rx.center(
                            rx.image(
                                src="/logo.png",
                                width="40%",
                                border_radius="25%",
                            ),
                            rx.heading(
                                "Sign in to your account",
                                size="6",
                                as_="h2",
                                width="100%",
                                align="center",
                            ),
                            rx.hstack(
                                rx.text(
                                    "New here?",
                                    size="3",
                                    text_align="center",
                                ),
                                rx.link(
                                    "Sign up", href="#", size="3", text_align="center"
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
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            placeholder="user@reflex.dev",
                            type="email",
                            size="3",
                            width="100%",
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
                            ),
                            rx.link(
                                "Forgot password?",
                                href="#",
                                size="3",
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
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.button("Sign in", size="3", width="100%"),
                    rx.hstack(
                        rx.divider(margin="0"),
                        rx.text(
                            "Or continue with",
                            white_space="nowrap",
                            weight="medium",
                        ),
                        rx.divider(margin="0"),
                        align="center",
                        width="100%",
                    ),
                    rx.center(
                        rx.icon_button(
                            rx.icon(tag="github"),
                            variant="soft",
                            size="3",
                        ),
                        rx.icon_button(
                            rx.icon(tag="facebook"),
                            variant="soft",
                            size="3",
                        ),
                        rx.icon_button(
                            rx.icon(tag="twitter"),
                            variant="soft",
                            size="3",
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
            ),
            justify="center",  # Centrado horizontal
            align="center",  # Centrado vertical
            height="100vh",  # Asegura que el flex ocupe toda la altura de la vista
        ),
        title="Container-login",
        background_color="gray",
        width="-webkit-fill-available",  # Ancho del contenedor acoplado con responsive design
        height="100vh",
    )
