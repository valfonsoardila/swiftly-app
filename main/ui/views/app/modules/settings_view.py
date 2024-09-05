import reflex as rx


@rx.page(route="/settings", title="Settings | Swiftly")
def settings_view() -> rx.Component:
    return rx.box()
