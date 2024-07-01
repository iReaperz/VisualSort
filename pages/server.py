import plotly.graph_objects as go
import numpy as np

def update_graph(fig, arr, current_index=None, min_index=None, final=False):
    if not final:
        colors = ['rgb(33, 58, 72)'] * len(arr)
        if current_index is not None and current_index < len(colors):
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

def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

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


def partition(fig, array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high -= 1
        while low <= high and array[low] <= pivot:
            low += 1
        if low <= high:
            array[low], array[high] = array[high], array[low]

        if low <= high:
            update_graph(fig, array, current_index=low, min_index=high)
        else:
            break

    array[start], array[high] = array[high], array[start]
    update_graph(fig, array, current_index=high)

    return high

def quick_vis(array, fig, start, end):
    if start >= end:
        return

    p = partition(fig, array, start, end)
    quick_vis(array, fig, start, p-1)
    quick_vis(array, fig, p+1, end)
    
    if is_sorted(array) == True:
        update_graph(fig, array, final=True)
        
def odd_even_vis(arr,fig):
    n = len(arr)
    # Initially array is unsorted
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                update_graph(fig, arr, i)
                isSorted = 0
                
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                update_graph(fig, arr, i)
                isSorted = 0
    update_graph(fig, arr, final=True)
        
def gnome_vis(arr, fig, n): 
    index = 0
    while index < n: 
        if index == 0: 
            index = index + 1
        if arr[index] >= arr[index - 1]: 
            index = index + 1
        else: 
            arr[index], arr[index-1] = arr[index-1], arr[index] 
            index = index - 1
        update_graph(fig, arr, index-1)
    update_graph(fig, arr, final=True)

def cocktail_vis(arr, fig):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):

        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False

        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                update_graph(fig, arr, i)
                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end-1

        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end-1, start-1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                update_graph(fig, arr, i)
                swapped = True

        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start + 1
    update_graph(fig, arr, final=True)

    


