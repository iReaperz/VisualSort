import plotly.graph_objects as go
from shiny import Inputs, Outputs, Session, module, render, ui, reactive
from shinywidgets import output_widget, render_widget
from pages.server import bubble_vis, selection_vis, insertion_vis,  generate_random_array
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
                        value=30
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px;"
            ),
            ui.card(output_widget("bubble")),
            ui.div(
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
                    '<div class="button-container">'
                    '<button class = "animated-button" onclick="showCode(\'python\')"><i class="fab fa-python"></i> Python</button>'
                    '<button class = "animated-button" onclick="showCode(\'java\')"><i class="fab fa-java"></i> Java</button>'
                    '<button class = "animated-button" onclick="showCode(\'cpp\')"><i class="fab fa-cuttlefish"></i> C++</button>'
                    '<button class = "animated-button" onclick="showCode(\'javascript\')"><i class="fab fa-js"></i> JavaScript</button>'
                    '</div>'
                    '<div class="textarea-container">'
                    '<textarea class="area shiny-bound-input" id="code" name="code" readonly="">'
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
                    '</div>'
                )
            )
        )
        ),
        ui.HTML(
            '<div class="container">'
            '<ul class="link-list">'
            '<li><a href="mailto:ireaperz07@gmail.com">Email</a></li>'
            '<li><a href="https://www.linkedin.com/in/noy-simonyan-888683266/">LinkedIn</a></li>'
            '<li><a href="https://github.com/iReaperz/VisualSort">Github</a></li>'
            '</ul>'
            '</div>'
        )        
)




@module.server
def bubble_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[], marker_color='rgb(33, 58, 72)', marker_line_width=0)])
    fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)', height=600)
    fig.update_xaxes(fixedrange=True, visible=False)
    fig.update_yaxes(fixedrange=True, visible=False)
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
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=600)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

    # Initialize the graph when the page loads
    @reactive.Effect
    def initialize_graph():
        num_beans = input.sliderBubble()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=600)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'


    
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
                        id='sliderBubble',
                        label='Number of Beans',
                        min=3,
                        max=50,
                        value=30
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px;"
            ),
            ui.card(output_widget("bubble")),
            ui.div(
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
                    '<div class="button-container">'
                    '<button class = "animated-button" onclick="showCode(\'python\')"><i class="fab fa-python"></i> Python</button>'
                    '<button class = "animated-button" onclick="showCode(\'java\')"><i class="fab fa-java"></i> Java</button>'
                    '<button class = "animated-button" onclick="showCode(\'cpp\')"><i class="fab fa-cuttlefish"></i> C++</button>'
                    '<button class = "animated-button" onclick="showCode(\'javascript\')"><i class="fab fa-js"></i> JavaScript</button>'
                    '</div>'
                    '<div class="textarea-container">'
                    '<textarea class="area shiny-bound-input" id="code" name="code" readonly="">'
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
                    '</div>'
                )
            )
        )
        ),
        ui.HTML(
            '<div class="container">'
            '<ul class="link-list">'
            '<li><a href="mailto:ireaperz07@gmail.com">Email</a></li>'
            '<li><a href="https://www.linkedin.com/in/noy-simonyan-888683266/">LinkedIn</a></li>'
            '<li><a href="https://github.com/iReaperz/VisualSort">Github</a></li>'
            '</ul>'
            '</div>'
        )        
)

@module.server
def selection_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[], marker_color='rgb(33, 58, 72)', marker_line_width=0)])
    fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)', height=600)
    fig.update_xaxes(fixedrange=True, visible=False)
    fig.update_yaxes(fixedrange=True, visible=False)
    arr = reactive.Value([])  # Reactive variable to store the array

    @render_widget
    def bubble():
        return fig

    @reactive.Effect
    @reactive.event(input.start)
    async def run_bubble_sort():
        selection_vis(arr(), fig)  # Use the reactive array in bubble_vis

    @reactive.Effect
    @reactive.event(input.shuffle)
    def shuffle_array():
        num_beans = input.sliderBubble()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=600)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

    # Initialize the graph when the page loads
    @reactive.Effect
    def initialize_graph():
        num_beans = input.sliderBubble()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=600)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'


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
                        id='sliderBubble',
                        label='Number of Beans',
                        min=3,
                        max=50,
                        value=30
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px;"
            ),
            ui.card(output_widget("bubble")),
            ui.div(
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
                    '<div class="button-container">'
                    '<button class = "animated-button" onclick="showCode(\'python\')"><i class="fab fa-python"></i> Python</button>'
                    '<button class = "animated-button" onclick="showCode(\'java\')"><i class="fab fa-java"></i> Java</button>'
                    '<button class = "animated-button" onclick="showCode(\'cpp\')"><i class="fab fa-cuttlefish"></i> C++</button>'
                    '<button class = "animated-button" onclick="showCode(\'javascript\')"><i class="fab fa-js"></i> JavaScript</button>'
                    '</div>'
                    '<div class="textarea-container">'
                    '<textarea class="area shiny-bound-input" id="code" name="code" readonly="">'
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
                    '</div>'
                )
            )
        )
        ),
        ui.HTML(
            '<div class="container">'
            '<ul class="link-list">'
            '<li><a href="mailto:ireaperz07@gmail.com">Email</a></li>'
            '<li><a href="https://www.linkedin.com/in/noy-simonyan-888683266/">LinkedIn</a></li>'
            '<li><a href="https://github.com/iReaperz/VisualSort">Github</a></li>'
            '</ul>'
            '</div>'
        )        
)

@module.server
def insertion_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[], marker_color='rgb(33, 58, 72)', marker_line_width=0)])
    fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)', height=600)
    fig.update_xaxes(fixedrange=True, visible=False)
    fig.update_yaxes(fixedrange=True, visible=False)
    arr = reactive.Value([])  # Reactive variable to store the array

    @render_widget
    def bubble():
        return fig

    @reactive.Effect
    @reactive.event(input.start)
    async def run_bubble_sort():
        insertion_vis(arr(), fig)  # Use the reactive array in bubble_vis

    @reactive.Effect
    @reactive.event(input.shuffle)
    def shuffle_array():
        num_beans = input.sliderBubble()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=600)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

    # Initialize the graph when the page loads
    @reactive.Effect
    def initialize_graph():
        num_beans = input.sliderBubble()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=600)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

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
                        id='sliderBubble',
                        label='Number of Beans',
                        min=3,
                        max=50,
                        value=30
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px;"
            ),
            ui.card(output_widget("bubble")),
            ui.div(
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
                    '<div class="button-container">'
                    '<button class = "animated-button" onclick="showCode(\'python\')"><i class="fab fa-python"></i> Python</button>'
                    '<button class = "animated-button" onclick="showCode(\'java\')"><i class="fab fa-java"></i> Java</button>'
                    '<button class = "animated-button" onclick="showCode(\'cpp\')"><i class="fab fa-cuttlefish"></i> C++</button>'
                    '<button class = "animated-button" onclick="showCode(\'javascript\')"><i class="fab fa-js"></i> JavaScript</button>'
                    '</div>'
                    '<div class="textarea-container">'
                    '<textarea class="area shiny-bound-input" id="code" name="code" readonly="">'
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
                    '</div>'
                )
            )
        )
        ),
        ui.HTML(
            '<div class="container">'
            '<ul class="link-list">'
            '<li><a href="mailto:ireaperz07@gmail.com">Email</a></li>'
            '<li><a href="https://www.linkedin.com/in/noy-simonyan-888683266/">LinkedIn</a></li>'
            '<li><a href="https://github.com/iReaperz/VisualSort">Github</a></li>'
            '</ul>'
            '</div>'
        )        
)




@module.server
def quick_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[], marker_color='rgb(33, 58, 72)', marker_line_width=0)])
    fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)', height=600)
    fig.update_xaxes(fixedrange=True, visible=False)
    fig.update_yaxes(fixedrange=True, visible=False)
    arr = reactive.Value([])  # Reactive variable to store the array

    @render_widget
    def bubble():
        return fig

    @reactive.Effect
    @reactive.event(input.start)
    async def run_bubble_sort():
        pass
        # quick_vis(arr(), fig, 0, input.sliderBubble()-1)  # Use the reactive array in bubble_vis

    @reactive.Effect
    @reactive.event(input.shuffle)
    def shuffle_array():
        num_beans = input.sliderBubble()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=600)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

    # Initialize the graph when the page loads
    @reactive.Effect
    def initialize_graph():
        num_beans = input.sliderBubble()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=600)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

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

