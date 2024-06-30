import plotly.graph_objects as go
import numpy as np

def update_graph(fig, arr, current_index=None, min_index=None, final=False):
    if not final:
        colors = ['rgb(33, 58, 72)'] * len(arr)
        if current_index is not None:
            colors[current_index] = 'red'
        if min_index is not None:
            colors[min_index] = 'rgb(23, 100, 77)'
        fig.data[0].y = arr
        fig.data[0].marker.color = colors
    else:
        for i in range(len(arr)):
            colors = ['rgb(33, 58, 72)'] * len(arr)
            colors[i] = 'rgb(23, 100, 77)'
            fig.data[0].marker.color = colors
        fig.data[0].marker.color = ['rgb(23, 100, 77)'] * len(arr)

def generate_random_array(size):
    arr = np.arange(1, size + 1)
    np.random.shuffle(arr)
    return arr 

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

def selection_vis(arr, fig):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        update_graph(fig, arr, current_index=i, min_index=min_index)
        for k in range(i+1, n):
            if arr[k] < arr[min_index]:
                min_index = k
            update_graph(fig, arr, current_index=k, min_index=min_index)
        arr[i], arr[min_index] = arr[min_index], arr[i]
        update_graph(fig, arr)
    update_graph(fig, arr, final=True)

def insertion_vis(arr, fig):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            update_graph(fig, arr, current_index=j, min_index=i)
        arr[j+1] = key
    update_graph(fig, arr, final=True)


# def partition(fig, array, start, end):
#     pivot = array[start]
#     low = start + 1
#     high = end

#     while True:
#         while low <= high and array[high] >= pivot:
#             high = high - 1
#             if high < len(array):
#                 update_graph(fig, array, low)
#             else:
#                 update_graph(fig, array, low)

#         while low <= high and array[low] <= pivot:
#             low = low + 1
#             if high < len(array):
#                 update_graph(fig, array, low)
#             else:
#                 update_graph(fig, array, low)

#         if low <= high:
#             array[low], array[high] = array[high], array[low]
#             if high < len(array):
#                 update_graph(fig, array, low)
#             else:
#                 update_graph(fig, array, low)
#         else:
#             break

#     array[start], array[high] = array[high], array[start]

#     return high

# def quick_vis(array, fig, start, end):
#     if start >= end:
#         # update_graph(fig, array, final=True)
#         return

#     p = partition(fig, array, start, end)
#     quick_vis(array, fig, start, p-1)
#     quick_vis(array, fig, p+1, end)




