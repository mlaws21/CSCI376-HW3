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
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: this sets the color of the text to the negative color from UI.colors

with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl bg-blue-50"):
    # w-100: Set element width to be fixed at 100
    # p-6: set the padding to setting 6
    # shadow-xl: adds an xl shadow to the element
    # mx-auto: sets all margins to auto
    # mt-10: sets the margin top to setting 10 (this overwrites the margin auto)
    # rounded-xl: applies a rounding radius to the box for curved corners
    ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
    # text-2xl: makes the text size large
    # font-bold: uses bold type face
    # text-accent: uses the accent color for the color
    # mb-4: sets the bottom margin to setting 4
    input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
    # w-full: full width of container
    # border: just adds a 1px border to the element
    # rounded: rounds the border
    conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
    convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded")
    # text-white: sets the text color to white
    # py-2: sets the padding top and bottom to setting 2
    # px-4: sets the padding left and right to setting 4
    result_label = ui.label("").classes("text-lg mt-4")

ui.run()