import numpy as np
import plotly.graph_objects as go
from shiny import Inputs, Outputs, Session, module, render, ui, reactive
from shinywidgets import output_widget, render_widget
from pages.server import bubble_vis, generate_random_array
import asyncio

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
                        max=100,
                        value=10  # Установите начальное значение по умолчанию
                    ),
                    style="display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; margin-right: 20px"
            ),
            ui.div(
                output_widget("bubble")
            )
        )
    )

@module.server
def bubble_server(input: Inputs, output: Outputs, session: Session):
    fig = go.FigureWidget(data=[go.Bar(x=[], y=[])])
    
    @render_widget
    def bubble():
        return fig

    @reactive.Effect
    @reactive.event(input.start)
    async def run_bubble_sort():
        num_beans = input.sliderBubble()  # Получаем значение слайдера в реактивном контексте
        await bubble_vis(num_beans, fig)
    
    @reactive.Effect
    @reactive.event(input.shuffle)
    def shuffle_array():
        num_beans = input.sliderBubble()
        arr = generate_random_array(num_beans)
        fig.data[0].x = list(range(len(arr)))
        fig.data[0].y = arr

    # Инициализация графика при загрузке страницы
    @reactive.Effect
    def initialize_graph():
        num_beans = input.sliderBubble()
        arr = generate_random_array(num_beans)
        fig.data[0].x = list(range(len(arr)))
        fig.data[0].y = arr



    
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