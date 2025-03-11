from nicegui import ui

ui.colors(
    primary='#1976d2',
    secondary='#26A69A',
    accent='#9C27B0',
    positive='#21BA45',
    negative='#C10015',
    info='#31CCEC',
    warning='#F2C037'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: this sets the color of the text to the positive color from UI.colors
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4 animate-pulse")
        # ADDED animate-pulse: looks cool and makes the error msg more clear to the user.
        # text-negative: this sets the color of the text to the negative color from UI.colors

def convert2():
    try: 
        temp = float(tempClass.num)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label2.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label2.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label2.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: this sets the color of the text to the positive color from UI.colors
    except ValueError:
        result_label2.set_text("Please enter a valid number.")
        result_label2.classes("text-lg font-semibold text-negative mt-4 animate-pulse")
        # ADDED animate-pulse: looks cool and makes the error msg more clear to the user.
        # text-negative: this sets the color of the text to the negative color from UI.colors
# ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4 uppercase")
ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mx-auto uppercase")
# ADDED uppercase: makes text uppercase
# text-2xl: makes the text size large
# font-bold: uses bold type face
# text-accent: uses the accent color for the color
# mb-4: sets the bottom margin to setting 4

class TempClass:
    def __init__(self):
        self.num = 50

tempClass = TempClass()


with ui.row().classes("mx-auto"):

    with ui.card().classes("w-100 p-6 shadow-xl mx-auto rounded-xl  bg-gray-100 hover:bg-blue-50"):
        # ADDED bg-blue-50: adds light blue background
        # w-100: Set element width to be fixed at 100
        # p-6: set the padding to setting 6
        # shadow-xl: adds an xl shadow to the element
        # mx-auto: sets all margins to auto
        # mt-10: sets the margin top to setting 10 (this overwrites the margin auto)
        # rounded-xl: applies a rounding radius to the box for curved corners
    
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded hover:bg-blue-100")
        # ADDED hover:bg-blue-100: changes background on hover
        # w-full: full width of container
        # border: just adds a 1px border to the element
        # rounded: rounds the border
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4 ")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded")
        # text-white: sets the text color to white
        # py-2: sets the padding top and bottom to setting 2
        # px-4: sets the padding left and right to setting 4
        result_label = ui.label("").classes("text-lg mt-4 ")
    
    
    with ui.card().classes("p-6 shadow-xl mx-auto rounded-xl bg-gray-100 hover:bg-red-50"):
        # input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded hover:bg-red-100")
         
        with ui.row().classes("w-full flex gap-4 mx-auto"):
            ui.slider(min=0, max=100, step=1, value=50).bind_value(tempClass, 'num').classes("w-40 mb-4  p-4 text-lg border rounded hover:bg-red-100")

            ui.number("Temperature").bind_value(tempClass, 'num').classes("w-20")
            

        # label = ui.label(f"Slider Value: {slider.value}")
        
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4 ")
        convert_button = ui.button("Convert", on_click=convert2).classes("text-white font-bold py-2 px-4 rounded")
        # text-white: sets the text color to white
        # py-2: sets the padding top and bottom to setting 2
        # px-4: sets the padding left and right to setting 4
        result_label2 = ui.label("").classes("text-lg mt-4 ")

ui.run()