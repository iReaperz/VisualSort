import plotly.graph_objects as go
import numpy as np

def update_graph(fig, arr, current_index=None, min_index=None, final=False):
    if not final:
        colors = ['blue'] * len(arr)
        if current_index is not None:
            colors[current_index] = 'red'
        if min_index is not None:
            colors[min_index] = 'green'
        fig.data[0].y = arr
        fig.data[0].marker.color = colors
    else:
        for i in range(len(arr)):
            colors = ['blue'] * len(arr)
            colors[i] = 'green'
            fig.data[0].marker.color = colors
        fig.data[0].marker.color = ['green'] * len(arr) 

def bubble_vis(arr, fig):
    been_num_val = len(arr)
    for i in range(been_num_val):
        for j in range(0, been_num_val - i - 1):
            update_graph(fig, arr, j)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                update_graph(fig, arr, j + 1)
        # Mark the last sorted bar with the normal color
        update_graph(fig, arr)

    # Final update to mark the array as fully sorted
    update_graph(fig, arr, final=True)

def generate_random_array(size):
    arr = np.arange(1, size + 1)
    np.random.shuffle(arr)
    return arr
