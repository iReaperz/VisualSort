import numpy as np
import plotly.graph_objects as go
from shiny import Inputs, Outputs, Session, module, render, ui, reactive
from shinywidgets import output_widget, render_widget
from pages.server import bubble_vis, selection_vis, insertion_vis, quick_vis, odd_even_vis, gnome_vis, cocktail_vis, generate_random_array

def sorting_panel_ui(sort_type, default_code, desc, worst, space, best, average):
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
                ui.div(ui.HTML(desc),
                       ui.HTML(f'''
                            <div class="leftDiv">
                                <div class="table-box">
                                    <div style="font-family: 'Jura', Courier, monospace; font-size: 35px;text-align: right;">COMPLEXITY</div>
                                    <table class="sort-table aos-init aos-animate" data-aos="flip-left" style="border-collapse: collapse; width: 100%; font-family: 'Jura', Courier, monospace; font-size: 16px;">
                                        <tbody>
                                            <tr style="border-bottom: 1px solid #ccc;">
                                                <th style="padding: 10px;">Average Complexity</th>
                                                <td style="padding: 10px; text-align: right;">{average}</td>
                                            </tr>
                                            <tr style="border-bottom: 1px solid #ccc;">
                                                <th style="padding: 10px;">Best Case</th>
                                                <td style="padding: 10px; text-align: right;">{best}</td>
                                            </tr>
                                            <tr style="border-bottom: 1px solid #ccc;">
                                                <th style="padding: 10px;">Worst Case</th>
                                                <td style="padding: 10px; text-align: right;">{worst}</td>
                                            </tr>
                                            <tr style="border-bottom: 1px solid #ccc;">
                                                <th style="padding: 10px;">Space Complexity</th>
                                                <td style="padding: 10px; text-align: right;">{space}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>'''),
                       class_ ='description'),
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
    f'<button class="animated-button" onclick="showCode(\'python\', \'{sort_type.lower()}\')"><i class="fab fa-python"></i> Python</button>'
    f'<button class="animated-button" onclick="showCode(\'java\', \'{sort_type.lower()}\')"><i class="fab fa-java"></i> Java</button>'
    f'<button class="animated-button" onclick="showCode(\'cpp\', \'{sort_type.lower()}\')"><i class="fab fa-cuttlefish"></i> C++</button>'
    f'<button class="animated-button" onclick="showCode(\'javascript\', \'{sort_type.lower()}\')"><i class="fab fa-js"></i> JavaScript</button>'
    f'</div>'
    f'<div class="textarea-container" style="position: relative;">'
    f'<textarea class="code {sort_type.lower()}-code area shiny-bound-input" id="code-{sort_type.lower()}" name="code" readonly="">{default_code}</textarea>'
    f'<div class = "tooltip>'
    f'<button class = "button-80" onclick="copyFunction()"><i class="fa fa-clone" aria-hidden="true"></i></button>'
    f'<span class="tooltiptext" id="myTooltip">Copy to clipboard</span>'
    f'</div>'
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
    description_html = """
        <div class="description" style="font-family: 'Jura', Courier, monospace; font-size: 16px;">
            <div class="rightDiv">
                <div style="font-family: 'Jura', Courier, monospace; font-size: 35px;">DESCRIPTION</div>
                <p>Bubble Sort is a straightforward and inefficient sorting algorithm.</p>
                <p>It works by repeatedly stepping through the list of items to be sorted, comparing adjacent items, and swapping them if they are in the wrong order.</p>
                <p>This process is repeated until the list is sorted. Bubble Sort gets its name because smaller elements "bubble" to the top of the list with each pass.</p>
                <p>While easy to understand and implement, Bubble Sort is not suitable for large datasets due its time complexity.</p>
            </div>
        </div>
    """    
    return sorting_panel_ui("Bubble", default_code, description_html, average="O(log<sup>2</sup> n)", best = "O(log<sup>2</sup> n)", worst = "O(log<sup>2</sup> n)", space = "O(n × log<sup>2</sup> n)")

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
    description_html = """
        <div class="description" style="font-family: 'Jura', Courier, monospace; font-size: 16px;">
            <div class="rightDiv">
                <div style="font-family: 'Jura', Courier, monospace; font-size: 35px;">DESCRIPTION</div>
                    <p>Selection Sort is a simple and inefficient sorting algorithm.</p>
                    <p>It works by repeatedly stepping through the list of items to be sorted, finding the minimum element from the unsorted part, and swapping it with the first unsorted element.</p>
                    <p>This process is repeated until the entire list is sorted. Selection Sort gets its name because it repeatedly selects the smallest remaining element.</p>
                    <p>While easy to understand and implement, Selection Sort is not suitable for large datasets due to its O(n^2) time complexity, where n is the number of items being sorted.</p>
            </div>
        </div>
    """    
    return sorting_panel_ui("Selection", default_code, description_html, average="O(n<sup>2</sup>)", best = "O(n<sup>2</sup>)", worst = "O(n<sup>2</sup>)", space = "O(1)")

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
    description_html = """
        <div class="description" style="font-family: 'Jura', Courier, monospace; font-size: 16px;">
            <div class="rightDiv">
                <div style="font-family: 'Jura', Courier, monospace; font-size: 35px;">DESCRIPTION</div>
                <p>Insertion Sort is a straightforward and efficient sorting algorithm for small datasets.</p>
<p>It works by building a sorted array one element at a time, taking each new element and inserting it into its correct position among the already-sorted elements.</p>
<p>This process is repeated until the entire list is sorted. Insertion Sort gets its name from the way it inserts elements into the sorted portion of the list.</p>
<p>While efficient for small or nearly sorted datasets, Insertion Sort is not suitable for large datasets due to its O(n^2) time complexity in the average and worst cases, where n is the number of items being sorted.</p> </div>
        </div>
    """    
    return sorting_panel_ui("Insertion", default_code, description_html, average="O(n^2)", best="O(n)", worst="O(n^2)", space="O(1)")

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
    description_html = """
        <div class="description" style="font-family: 'Jura', Courier, monospace; font-size: 16px;">
            <div class="rightDiv">
                <div style="font-family: 'Jura', Courier, monospace; font-size: 35px;">DESCRIPTION</div>
    <p>Quick Sort is a highly efficient and widely used sorting algorithm.</p>
<p>It works by selecting a 'pivot' element from the list and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.</p>
<p>This process is recursively applied to the sub-arrays until the entire list is sorted. Quick Sort gets its name from the quick partitioning process.</p>
<p>While very efficient with an average and best-case time complexity of O(n log n), Quick Sort can degrade to O(n^2) in the worst case. However, this is rare if a good pivot selection strategy is used. Its space complexity is O(log n).</p>           </div>
        </div>
    """    
    return sorting_panel_ui("Quick", default_code, description_html, average="O(n log n)", best="O(n log n)", worst="O(n^2)", space="O(log n)")

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
    description_html = """
        <div class="description" style="font-family: 'Jura', Courier, monospace; font-size: 16px;">
            <div class="rightDiv">
                <div style="font-family: 'Jura', Courier, monospace; font-size: 35px;">DESCRIPTION</div>
              <p>Odd-Even Sort, also known as Brick Sort, is a variation of the Bubble Sort algorithm.</p>
<p>It works by performing pairwise comparisons of elements in two phases: first comparing elements at odd indices with their next neighbors, then comparing elements at even indices with their next neighbors.</p>
<p>This alternating process is repeated until the list is sorted. Odd-Even Sort derives its name from the alternating pattern of comparisons.</p>
<p>While conceptually simple, Odd-Even Sort has a time complexity of O(n^2) in the average and worst cases, making it inefficient for large datasets. It has a space complexity of O(1), as it sorts in place.</p>  </div>
        </div>
    """    
    return sorting_panel_ui("Odd", default_code, description_html, average="O(n^2)", best="O(n)", worst="O(n^2)", space="O(1)")

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
    description_html = """
        <div class="description" style="font-family: 'Jura', Courier, monospace; font-size: 16px;">
            <div class="rightDiv">
                <div style="font-family: 'Jura', Courier, monospace; font-size: 35px;">DESCRIPTION</div>
       <p>Gnome Sort, also known as Stupid Sort, is a simple sorting algorithm that is similar to Insertion Sort.</p>
<p>It works by repeatedly moving backward through the list, comparing adjacent elements, and swapping them if they are in the wrong order.</p>
<p>If a swap is made, it then moves one step backward; otherwise, it moves one step forward and repeats the process.</p>
<p>This process continues until the entire list is sorted. Gnome Sort gets its name from the way it moves elements around like a gnome sorting books on a shelf.</p>
<p>While easy to understand and implement, Gnome Sort has an average and worst-case time complexity of O(n^2), making it inefficient for large datasets. It has a space complexity of O(1), as it sorts in place.</p>
     </div>
        </div>
    """    
    return sorting_panel_ui("Gnome", default_code, description_html, average="O(n^2)", best="O(n)", worst="O(n^2)", space="O(1)")

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
    description_html = """
        <div class="description" style="font-family: 'Jura', Courier, monospace; font-size: 16px;">
            <div class="rightDiv">
                <div style="font-family: 'Jura', Courier, monospace; font-size: 35px;">DESCRIPTION</div>
       <p>Cocktail Sort, also known as Bidirectional Bubble Sort or Cocktail Shaker Sort, is a variation of Bubble Sort.</p>
<p>It works by moving both forward and backward through the list, repeatedly stepping through the list of items to be sorted, comparing adjacent items, and swapping them if they are in the wrong order.</p>
<p>This bidirectional process is repeated until the list is sorted. Cocktail Sort gets its name from the way elements "bubble" up and down through the list like cocktail shakers.</p>
<p>While it improves on the standard Bubble Sort by making passes in both directions, Cocktail Sort still has an average and worst-case time complexity of O(n^2), making it inefficient for large datasets. It has a space complexity of O(1), as it sorts in place.</p>
     </div>
        </div>
    """    
    return sorting_panel_ui("Cocktail", default_code, description_html, average="O(n^2)", best="O(n)", worst="O(n^2)", space="O(1)")

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


