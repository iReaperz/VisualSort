from shiny import App, Inputs, Outputs, Session, reactive, ui
from pages.modules import bubble_sort_ui, selection_sort_ui, cocktail_sort_ui, gnome_sort_ui, quick_sort_ui, insertion_sort_ui, odd_sort_ui, bubble_server, selection_server, insertion_server, quick_server

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
        ui.tags.script('''
                        function showCode(language) {
                            var code = '';
                            switch(language) {
                                case 'python':
                                    code = `def bubble_sort(arr):
                    n = len(arr)
                    for i in range(n):
                        for j in range(0, n-i-1):
                            if arr[j] > arr[j+1]:
                                arr[j], arr[j+1] = arr[j+1], arr[j]
                    return arr`;
                                    break;
                                case 'java':
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
                                    break;
                                case 'cpp':
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
                                    break;
                                case 'javascript':
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
                                    break;
                            }
                            document.getElementById('code').value = code;
                        }
                        ''')
    ),
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
    selection_server(id="tab2")
    quick_server(id="tab5")
    insertion_server(id="tab6")
    

app = App(app_ui, server)
