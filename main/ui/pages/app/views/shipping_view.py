import reflex as rx


@rx.page(route="/app/shipping", title="Shipping")
def shipping_view() -> rx.Component:
    return rx.box()
