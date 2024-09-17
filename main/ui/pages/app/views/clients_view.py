import reflex as rx


@rx.page(route="/app/client", title="App | Dashboard")
def clients_view() -> rx.Component:
    return rx.box()
