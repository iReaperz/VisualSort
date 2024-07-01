import numpy as np
import plotly.graph_objects as go
from shiny import Inputs, Outputs, Session, module, render, ui, reactive
from shinywidgets import output_widget, render_widget
from pages.server import bubble_vis, selection_vis, insertion_vis, quick_vis, odd_even_vis, gnome_vis, cocktail_vis, generate_random_array

def sorting_panel_ui(sort_type, default_code):
    return ui.nav_panel(
        sort_type + " Sort",
        ui.card(
            ui.div(
                ui.span(f"{sort_type} Sort", class_="sort-text"),
                ui.div(
                    ui.div(
                        ui.input_action_button(
                            "start",
                            ui.tags.i(class_="fas fa-play fa-1x"),
                            style="margin-left: 30px; margin-bottom:5px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        ),
                        ui.input_action_button(
                            "shuffle",
                            ui.tags.i(class_="fas fa-random fa-1x"),
                            style="margin-left: 30px; width: 30px; height: 40px; display: flex; align-items: center; justify-content: center;"
                        )
                    ),
                    ui.input_slider(
                        id=f'slider{sort_type}',
                        label='Number of Beans',
                        min=3,
                        max=50,
                        value=30
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px;"
            ),
            ui.card(output_widget(f"{sort_type.lower()}")),
            ui.div(
                ui.div(
                    ui.HTML(
                        f'<div class="card_bot {sort_type.lower()}">'
                        f'<div class="header">'
                        f'<div class="top">'
                        f'<div class="title">'
                        f'</div>'
                        f'</div>'
                        f'</div>'
                        f'<div class="code-container">'
                        f'<div class="button-container">'
                        f'<button class = "animated-button" onclick="showCode(\'python\', \'{sort_type.lower()}\')"><i class="fab fa-python"></i> Python</button>'
                        f'<button class = "animated-button" onclick="showCode(\'java\', \'{sort_type.lower()}\')"><i class="fab fa-java"></i> Java</button>'
                        f'<button class = "animated-button" onclick="showCode(\'cpp\', \'{sort_type.lower()}\')"><i class="fab fa-cuttlefish"></i> C++</button>'
                        f'<button class = "animated-button" onclick="showCode(\'javascript\', \'{sort_type.lower()}\')"><i class="fab fa-js"></i> JavaScript</button>'
                        f'</div>'
                        f'<div class="textarea-container">'
                        f'<textarea class="code {sort_type.lower()}-code area shiny-bound-input" id="code-{sort_type.lower()}" name="code" readonly="">{default_code}</textarea>'
                        f'</div>'
                        f'</div>'
                        f'</div>'
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
    )

@module.ui
def bubble_sort_ui():
    default_code = """def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    """
    return sorting_panel_ui("Bubble", default_code)

@module.server
def bubble_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[], marker_color='rgb(33, 58, 72)', marker_line_width=0)])
    fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)', height=500)
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
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
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
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

@module.ui
def selection_sort_ui():
    default_code = """def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
    """
    return sorting_panel_ui("Selection", default_code)

@module.server
def selection_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[], marker_color='rgb(33, 58, 72)', marker_line_width=0)])
    fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)', height=500)
    fig.update_xaxes(fixedrange=True, visible=False)
    fig.update_yaxes(fixedrange=True, visible=False)
    arr = reactive.Value([])  # Reactive variable to store the array

    @render_widget
    def selection():
        return fig

    @reactive.Effect
    @reactive.event(input.start)
    async def run_selection_sort():
        selection_vis(arr(), fig)  # Use the reactive array in selection_vis

    @reactive.Effect
    @reactive.event(input.shuffle)
    def shuffle_array():
        num_beans = input.sliderSelection()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

    # Initialize the graph when the page loads
    @reactive.Effect
    def initialize_graph():
        num_beans = input.sliderSelection()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

@module.ui
def insertion_sort_ui():
    default_code = """def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
    """
    return sorting_panel_ui("Insertion", default_code)

@module.server
def insertion_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[], marker_color='rgb(33, 58, 72)', marker_line_width=0)])
    fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)', height=500)
    fig.update_xaxes(fixedrange=True, visible=False)
    fig.update_yaxes(fixedrange=True, visible=False)
    arr = reactive.Value([])  # Reactive variable to store the array

    @render_widget
    def insertion():
        return fig

    @reactive.Effect
    @reactive.event(input.start)
    async def run_insertion_sort():
        insertion_vis(arr(), fig)  # Use the reactive array in insertion_vis

    @reactive.Effect
    @reactive.event(input.shuffle)
    def shuffle_array():
        num_beans = input.sliderInsertion()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

    # Initialize the graph when the page loads
    @reactive.Effect
    def initialize_graph():
        num_beans = input.sliderInsertion()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

@module.ui
def quick_sort_ui():
    default_code = """def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

    """
    return sorting_panel_ui("Quick", default_code)

@module.server
def quick_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[], marker_color='rgb(33, 58, 72)', marker_line_width=0)])
    fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)', height=500)
    fig.update_xaxes(fixedrange=True, visible=False)
    fig.update_yaxes(fixedrange=True, visible=False)
    arr = reactive.Value([])  # Reactive variable to store the array

    @render_widget
    def quick():
        return fig

    @reactive.Effect
    @reactive.event(input.start)
    async def run_quick_sort():
        quick_vis(arr(), fig, 0, input.sliderQuick()-1)  # Use the reactive array in quick_vis

    @reactive.Effect
    @reactive.event(input.shuffle)
    def shuffle_array():
        num_beans = input.sliderQuick()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

    # Initialize the graph when the page loads
    @reactive.Effect
    def initialize_graph():
        num_beans = input.sliderQuick()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

@module.ui
def odd_sort_ui():
    default_code = """def odd_even_sort(L):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(L)-1, 2):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                sorted = False

        for i in range(0, len(L)-1, 2):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                sorted = False
    """
    return sorting_panel_ui("Odd", default_code)

@module.server
def odd_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[], marker_color='rgb(33, 58, 72)', marker_line_width=0)])
    fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)', height=500)
    fig.update_xaxes(fixedrange=True, visible=False)
    fig.update_yaxes(fixedrange=True, visible=False)
    arr = reactive.Value([])  # Reactive variable to store the array

    @render_widget
    def odd():
        return fig

    @reactive.Effect
    @reactive.event(input.start)
    async def run_odd_sort():
        odd_even_vis(arr(), fig)  # Use the reactive array in odd_vis

    @reactive.Effect
    @reactive.event(input.shuffle)
    def shuffle_array():
        num_beans = input.sliderOdd()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

    # Initialize the graph when the page loads
    @reactive.Effect
    def initialize_graph():
        num_beans = input.sliderOdd()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

@module.ui
def gnome_sort_ui():
    default_code = """def gnomeSort(arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1
    """
    return sorting_panel_ui("Gnome", default_code)

@module.server
def gnome_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[], marker_color='rgb(33, 58, 72)', marker_line_width=0)])
    fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)', height=500)
    fig.update_xaxes(fixedrange=True, visible=False)
    fig.update_yaxes(fixedrange=True, visible=False)
    arr = reactive.Value([])  # Reactive variable to store the array

    @render_widget
    def gnome():
        return fig

    @reactive.Effect
    @reactive.event(input.start)
    async def run_gnome_sort():
        gnome_vis(arr(), fig, input.sliderGnome())  # Use the reactive array in gnome_vis

    @reactive.Effect
    @reactive.event(input.shuffle)
    def shuffle_array():
        num_beans = input.sliderGnome()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

    # Initialize the graph when the page loads
    @reactive.Effect
    def initialize_graph():
        num_beans = input.sliderGnome()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

@module.ui
def cocktail_sort_ui():
    default_code = """def cocktail(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False

        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if (swapped == False):
            break

        swapped = False
        end = end-1
        
        for i in range(end-1, start-1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1
    """
    return sorting_panel_ui("Cocktail", default_code)

@module.server
def cocktail_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[], marker_color='rgb(33, 58, 72)', marker_line_width=0)])
    fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)', height=500)
    fig.update_xaxes(fixedrange=True, visible=False)
    fig.update_yaxes(fixedrange=True, visible=False)
    arr = reactive.Value([])  # Reactive variable to store the array

    @render_widget
    def cocktail():
        return fig

    @reactive.Effect
    @reactive.event(input.start)
    async def run_cocktail_sort():
        cocktail_vis(arr(), fig)  # Use the reactive array in cocktail_vis

    @reactive.Effect
    @reactive.event(input.shuffle)
    def shuffle_array():
        num_beans = input.sliderCocktail()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'

    # Initialize the graph when the page loads
    @reactive.Effect
    def initialize_graph():
        num_beans = input.sliderCocktail()
        new_arr = generate_random_array(num_beans)
        arr.set(new_arr)  # Update the reactive array
        fig.data[0].x = list(range(len(new_arr)))
        fig.data[0].y = new_arr
        fig.update_layout(plot_bgcolor='rgb(24, 37, 51)', paper_bgcolor='rgb(24, 37, 51)',height=500)
        fig.update_xaxes(fixedrange=True, visible=False)
        fig.update_yaxes(fixedrange=True, visible=False)
        fig.data[0].marker.line.width = 0
        fig.data[0].marker.color = 'rgb(33, 58, 72)'
