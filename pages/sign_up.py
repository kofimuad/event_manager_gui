from nicegui import ui


def show_signup():
    with ui.element("div").classes("w-screen flex h-screen m-0 p-0"):
        with ui.element("div").classes("w-[45%] h-screen bg-red"):
            ui.image("/assets/bg_ice_mount.jpg").classes("h-screen")
        
        with ui.element("div").classes("w-[55%] h-screen bg-blue"):
            with ui.card():
                ui.label("I am a card")