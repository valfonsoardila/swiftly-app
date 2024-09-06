import reflex as rx


@rx.page(route="/app/settings", title="App | Settings")
def settings_view() -> rx.Component:
    return rx.box()
