from nicegui import ui


def show_home_page():
    ui.label("Welcome to Event Home")
    with ui.row():
        ui.link("Sign Up", "/signup")
        ui.link("Sign In", "/signin")