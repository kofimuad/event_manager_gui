from nicegui import ui, app
from pages.home import show_home_page
from pages.sign_up import show_signup


app.add_static_files("/assets", "assets")
ui.add_head_html('<link rel="stylesheet" href="/assets/reset.css"/>')

@ui.page("/")
def home_page():
    show_home_page()

@ui.page("/signup")
def sign_up():
    show_signup()







ui.run()