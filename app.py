from shiny import App, Inputs, Outputs, Session, reactive, ui
from pages.modules import bubble_sort_ui, selection_sort_ui, cocktail_sort_ui, gnome_sort_ui, quick_sort_ui, insertion_sort_ui, odd_sort_ui, bubble_server, selection_server, insertion_server, quick_server, odd_server, gnome_server, cocktail_server


js_code = '''
function showCode(language, sortType) {
    var code = '';
    switch (language) {
        case 'python':
            if (sortType === 'bubble') {
                code = `def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr`;
            } else if (sortType === 'selection') {
                code = `def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr`;
            } else if (sortType === 'insertion') {
                code = `def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr`;
            }
            break;
        case 'java':
            if (sortType === 'bubble') {
                code = `public class BubbleSort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
}`;
            } else if (sortType === 'selection') {
                code = `public class SelectionSort {
    public static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;
        }
    }
}`;
            } else if (sortType === 'insertion') {
                code = `public class InsertionSort {
    public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }
}`;
            }
            break;
        case 'cpp':
            if (sortType === 'bubble') {
                code = `void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}`;
            } else if (sortType === 'selection') {
                code = `void selectionSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        int temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
    }
}`;
            } else if (sortType === 'insertion') {
                code = `void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}`;
            }
            break;
        case 'javascript':
            if (sortType === 'bubble') {
                code = `function bubbleSort(arr) {
    var n = arr.length;
    for (var i = 0; i < n-1; i++) {
        for (var j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                var temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    return arr;
}`;
            } else if (sortType === 'selection') {
                code = `function selectionSort(arr) {
    for (var i = 0; i < arr.length; i++) {
        var minIdx = i;
        for (var j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        var temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
    }
    return arr;
}`;
            } else if (sortType === 'insertion') {
                code = `function insertionSort(arr) {
    for (var i = 1; i < arr.length; i++) {
        var key = arr[i];
        var j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
    return arr;
}`;
            }
            break;
    }
    document.getElementById(`code-${sortType}`).value = code;
}

'''
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
        ui.include_css("assets/style.css"),
        ui.tags.script(js_code)
    ),
    title=ui.tags.a(
        ui.tags.img(
            src="https://i.ibb.co/tBPLYFn/logo-cropped.png",
            width="150",
            height="70"
        ),
        href="hpass"
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    bubble_server(id="tab1")
    selection_server(id="tab2")
    cocktail_server(id="tab3")
    gnome_server(id="tab4")
    quick_server(id="tab5")
    insertion_server(id="tab6")
    odd_server(id="tab7")
    

app = App(app_ui, server)
