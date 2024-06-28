from shiny import App, Inputs, Outputs, Session, reactive, ui
from pages.modules import bubble_sort_ui, selection_sort_ui, cocktail_sort_ui, gnome_sort_ui, quick_sort_ui, insertion_sort_ui, odd_sort_ui, bubble_server

app_ui = ui.page_navbar(
    bubble_sort_ui("tab1"),
    selection_sort_ui("tab2"),
    cocktail_sort_ui("tab3"),
    gnome_sort_ui("tab4"),
    quick_sort_ui("tab5"),
    insertion_sort_ui("tab6"),
    odd_sort_ui("tab7"),
    id="tabs",
    header=ui.tags.head(
        ui.tags.link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
        ),
        ui.include_css("assets/style.css")
    ),  # Use relative path for CSS
    title=ui.tags.a(
        ui.tags.img(
            src="https://i.ibb.co/tBPLYFn/logo-cropped.png",
            width="150",  # Set the width (in pixels)
            height="70" # Use relative path for the image
        ),
        href="hpass"
    )
)

def server(input: Inputs, output: Outputs, session: Session):
    bubble_server(id="tab1")

app = App(app_ui, server)
