import reflex as rx


@rx.page(route="/senders")
def senders_view() -> rx.Component:
    return rx.box()
