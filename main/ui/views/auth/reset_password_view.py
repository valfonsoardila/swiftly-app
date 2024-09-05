import reflex as rx


@rx.page(route="/reset-password", title="Reset Password")
def reset_password_view() -> rx.Component:
    return rx.box()
