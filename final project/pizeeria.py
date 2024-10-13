import tkinter as tk
from tkinter import ttk

# Variables to hold user selections
selected_dough = None
selected_sauce = None
entered_toppings = None
entered_name = None

# Function to replace the start page with the dough selection page
def show_dough_options():
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Choose your dough", font=("Arial", 12))
    label.pack(pady=10)

    thin_button = tk.Button(root, text="Thin", command=lambda: select_dough("Thin"))
    thick_button = tk.Button(root, text="Thick", command=lambda: select_dough("Thick"))
    gluten_free_button = tk.Button(root, text="Gluten Free", command=lambda: select_dough("Gluten Free"))

    thin_button.pack(pady=5)
    thick_button.pack(pady=5)
    gluten_free_button.pack(pady=5)

def select_dough(dough_type):
    global selected_dough
    selected_dough = dough_type
    print(f"Dough selected: {dough_type}")
    show_sauce_options()

def show_sauce_options():
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="What sauce do you want?", font=("Arial", 12))
    label.pack(pady=10)

    tomato_button = tk.Button(root, text="Tomato", command=lambda: select_sauce("Tomato"))
    ranch_button = tk.Button(root, text="Ranch", command=lambda: select_sauce("Ranch"))
    olive_oil_button = tk.Button(root, text="Olive Oil", command=lambda: select_sauce("Olive Oil"))
    bbq_button = tk.Button(root, text="BBQ", command=lambda: select_sauce("BBQ"))

    tomato_button.pack(pady=5)
    ranch_button.pack(pady=5)
    olive_oil_button.pack(pady=5)
    bbq_button.pack(pady=5)

def select_sauce(sauce_type):
    global selected_sauce
    selected_sauce = sauce_type
    print(f"Sauce selected: {sauce_type}")
    show_toppings_input()

def show_toppings_input():
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Enter your toppings", font=("Arial", 12))
    label.pack(pady=10)

    toppings_entry = tk.Entry(root, width=30)
    toppings_entry.pack(pady=5)

    submit_button = tk.Button(root, text="Submit", command=lambda: submit_toppings(toppings_entry.get()))
    submit_button.pack(pady=10)

def submit_toppings(toppings):
    global entered_toppings
    entered_toppings = toppings
    print(f"Toppings entered: {toppings}")
    show_name_input()

def show_name_input():
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Enter your name", font=("Arial", 12))
    label.pack(pady=10)

    name_entry = tk.Entry(root, width=30)
    name_entry.pack(pady=5)

    submit_button = tk.Button(root, text="Submit", command=lambda: submit_name(name_entry.get()))
    submit_button.pack(pady=10)

def submit_name(name):
    global entered_name
    entered_name = name
    print(f"User name: {name}")
    # After name is submitted, show the order summary page
    show_order_summary()

def show_order_summary():
    for widget in root.winfo_children():
        widget.destroy()

    # Display the order summary
    label = tk.Label(root, text="Order Summary", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    dough_label = tk.Label(root, text=f"Dough: {selected_dough}", font=("Arial", 12))
    dough_label.pack(pady=5)

    sauce_label = tk.Label(root, text=f"Sauce: {selected_sauce}", font=("Arial", 12))
    sauce_label.pack(pady=5)

    toppings_label = tk.Label(root, text=f"Toppings: {entered_toppings}", font=("Arial", 12))
    toppings_label.pack(pady=5)

    name_label = tk.Label(root, text=f"Name: {entered_name}", font=("Arial", 12))
    name_label.pack(pady=5)

    # Button to return to the beginning to start a new order
    restart_button = tk.Button(root, text="Start New Order", command=show_dough_options)
    restart_button.pack(pady=10)

def add_to_board(dough, sauce, toppings, name):
    # Insert a new row in the Treeview with the collected data
    summary_board.insert("", "end", values=(dough, sauce, toppings, name))
    show_dough_options()

# Create the main window
root = tk.Tk()
root.title("Pizza Customizer")
root.geometry("300x400")

# Create the Treeview for the summary board
columns = ("Dough", "Sauce", "Toppings", "Name")
summary_board = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    summary_board.heading(col, text=col)
summary_board.pack(fill=tk.BOTH, expand=True)

# Create a start button, centered in the window
start_button = tk.Button(root, text="Start", command=show_dough_options)
start_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
