import reflex as rx


@rx.page(route="/guides", title="Guides | Swiftly")
def guides_view() -> rx.Component:
    return rx.box()
