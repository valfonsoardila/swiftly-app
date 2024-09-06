import reflex as rx


@rx.page(route="/app/senders", title="App | Senders")
def senders_view() -> rx.Component:
    return rx.box()
