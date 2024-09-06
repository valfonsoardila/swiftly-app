import reflex as rx


@rx.page(route="/app/guides", title="App | Guides")
def guides_view() -> rx.Component:
    return rx.box()
