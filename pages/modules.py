import plotly.graph_objects as go
from shiny import Inputs, Outputs, Session, module, render, ui, reactive
from shinywidgets import output_widget, render_widget
from pages.server import bubble_vis, generate_random_array
from htmltools import HTML, div
@module.ui
def bubble_sort_ui():
    return ui.nav_panel(
        "Bubble Sort",
        ui.card(
            ui.div(
                ui.span("Bubble Sort", class_="sort-text"),
                ui.div(
                    ui.div(
                        ui.input_action_button(
                            "start",
                            ui.tags.i(class_="fas fa-play fa-1x"),
                            style="margin-left: 30px; margin-bottom:5px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        ),
                        ui.input_action_button(
                            "shuffle",
                            ui.tags.i(class_="fas fa-random  fa-1x"),
                            style="margin-left: 30px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        )
                    ),
                    ui.input_slider(
                        id='sliderBubble',
                        label='Number of Beans',
                        min=3,
                        max=50,
                        value=10
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px;"
            ),
            ui.card(output_widget("bubble")),
            ui.div(
                ui.HTML(
                    '<div class="card_bot">'
                    '<div class="header">'
                    '<div class="top">'
                    '<div class="title">'
                    '</div>'
                    '</div>'
                    '</div>'
                    '<div class="code-container">'
                    '<p id="title2">BubbleSort.py</p>'
                    '<textarea class="area" id="code" name="code" readonly="">'
                    'def bubble_sort(arr):\n'
                    '    n = len(arr)\n'
                    '    for i in range(n):\n'
                    '        for j in range(0, n-i-1):\n'
                    '            if arr[j] > arr[j+1]:\n'
                    '                arr[j], arr[j+1] = arr[j+1], arr[j]\n'
                    '    return arr\n'
                    '</textarea>'
                    '</div>'
                    '</div>'
                )
            )
        ),
        ui.HTML(
            '<div class="container">'
            '<ul class="link-list">'
            '<li><a href="mailto:ireaperz07@gmail.com">Email</a></li>'
            '<li><a href="https://www.linkedin.com/in/noy-simonyan-888683266/">LinkedIn</a></li>'
            '<li><a href="https://github.com/iReaperz">Github</a></li>'
            '</ul>'
            '</div>'
        )        
)




@module.server
def bubble_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[], marker_color='blue')])
    fig.update_layout(plot_bgcolor='white')
    fig.update_xaxes(fixedrange = True, visible = False)
    fig.update_yaxes(fixedrange = True, visible = False)
    arr = reactive.Value([])  # Reactive variable to store the array
    
    @render_widget
    def bubble():
        return fig

    @reactive.Effect
    @reactive.event(input.start)
    async def run_bubble_sort():
        bubble_vis(arr(), fig)  # Use the reactive array in bubble_vis
    
    @reactive.Effect
    @reactive.event(input.shuffle)
    def shuffle_array():
        num_beans = input.sliderBubble()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.data[0].marker.color = 'blue'
        fig.update_layout(plot_bgcolor='white')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True

    # Initialize the graph when the page loads
    @reactive.Effect
    def initialize_graph():
        num_beans = input.sliderBubble()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.data[0].marker.color = 'blue'
        fig.update_layout(plot_bgcolor='white')
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True


    
@module.ui
def selection_sort_ui():
    return ui.nav_panel(
        "Selection Sort",
        ui.card(
            ui.div(
                ui.span("Selection Sort", class_="sort-text"),
                ui.div(
                    ui.div(
                        ui.input_action_button(
                            "start",
                            ui.tags.i(class_="fas fa-play fa-1x"),
                            style="margin-left: 30px; margin-bottom:5px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        ),
                        ui.input_action_button(
                            "shuffle",
                            ui.tags.i(class_="fas fa-random  fa-1x"),
                            style="margin-left: 30px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        )
                    ),
                    ui.input_slider(
                        id='value_slider',
                        label='Number of Beans',
                        min=3,
                        max=100,
                        value=50  # Установите начальное значение по умолчанию
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px"
            )
        )
    )

@module.ui
def insertion_sort_ui():
    return ui.nav_panel(
        "Insertion Sort",
        ui.card(
            ui.div(
                ui.span("Insertion Sort", class_="sort-text"),
                ui.div(
                    ui.div(
                        ui.input_action_button(
                            "start",
                            ui.tags.i(class_="fas fa-play fa-1x"),
                            style="margin-left: 30px; margin-bottom:5px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        ),
                        ui.input_action_button(
                            "shuffle",
                            ui.tags.i(class_="fas fa-random  fa-1x"),
                            style="margin-left: 30px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        )
                    ),
                    ui.input_slider(
                        id='value_slider',
                        label='Number of Beans',
                        min=3,
                        max=100,
                        value=50  # Установите начальное значение по умолчанию
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px"
            )
        )
    )

@module.ui
def quick_sort_ui():
    return ui.nav_panel(
        "Quick Sort",
        ui.card(
            ui.div(
                ui.span("Quick Sort", class_="sort-text"),
                ui.div(
                    ui.div(
                        ui.input_action_button(
                            "start",
                            ui.tags.i(class_="fas fa-play fa-1x"),
                            style="margin-left: 30px; margin-bottom:5px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        ),
                        ui.input_action_button(
                            "shuffle",
                            ui.tags.i(class_="fas fa-random  fa-1x"),
                            style="margin-left: 30px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        )
                    ),
                    ui.input_slider(
                        id='value_slider',
                        label='Number of Beans',
                        min=3,
                        max=100,
                        value=50  # Установите начальное значение по умолчанию
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px"
            )
        )
    )

@module.ui
def gnome_sort_ui():
    return ui.nav_panel(
        "Gnome Sort",
        ui.card(
            ui.div(
                ui.span("Gnome Sort", class_="sort-text"),
                ui.div(
                    ui.div(
                        ui.input_action_button(
                            "start",
                            ui.tags.i(class_="fas fa-play fa-1x"),
                            style="margin-left: 30px; margin-bottom:5px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        ),
                        ui.input_action_button(
                            "shuffle",
                            ui.tags.i(class_="fas fa-random  fa-1x"),
                            style="margin-left: 30px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        )
                    ),
                    ui.input_slider(
                        id='value_slider',
                        label='Number of Beans',
                        min=3,
                        max=100,
                        value=50  # Установите начальное значение по умолчанию
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px"
            )
        )
    )

@module.ui
def cocktail_sort_ui():
    return ui.nav_panel(
        "Cocktail Sort",
        ui.card(
            ui.div(
                ui.span("Cocktail Sort", class_="sort-text"),
                ui.div(
                    ui.div(
                        ui.input_action_button(
                            "start",
                            ui.tags.i(class_="fas fa-play fa-1x"),
                            style="margin-left: 30px; margin-bottom:5px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        ),
                        ui.input_action_button(
                            "shuffle",
                            ui.tags.i(class_="fas fa-random  fa-1x"),
                            style="margin-left: 30px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        )
                    ),
                    ui.input_slider(
                        id='value_slider',
                        label='Number of Beans',
                        min=3,
                        max=100,
                        value=50  # Установите начальное значение по умолчанию
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px"
            )
        )
    )

@module.ui
def odd_sort_ui():
    return ui.nav_panel(
        "Odd Even Sort",
        ui.card(
            ui.div(
                ui.span("Odd Even Sort", class_="sort-text"),
                ui.div(
                    ui.div(
                        ui.input_action_button(
                            "start",
                            ui.tags.i(class_="fas fa-play fa-1x"),
                            style="margin-left: 30px; margin-bottom:5px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        ),
                        ui.input_action_button(
                            "shuffle",
                            ui.tags.i(class_="fas fa-random  fa-1x"),
                            style="margin-left: 30px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        )
                    ),
                    ui.input_slider(
                        id='value_slider',
                        label='Number of Beans',
                        min=3,
                        max=100,
                        value=50  # Установите начальное значение по умолчанию
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px"
            )
        )
    )