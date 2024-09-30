from breezypythongui import EasyFrame

class PizzeriaHomePage(EasyFrame):
    def __init__(self):
        # Set the window title and size (16:9 ratio)
        EasyFrame.__init__(self, title="Pizzeria Customizer", width=1280, height=720)
        
        # Create the "Order Now" button in the center of the window
        self.addButton(text="Order Now", row=1, column=0, columnspan=2, command=self.orderNow)
        
        # Adjust grid layout to center the button (both horizontally and vertically)
        self.setPadding(100, 100)

    # Define what happens when "Order Now" is clicked
    def orderNow(self):
        # Action can be customized (e.g., navigating to the customization page)
        self.messageBox(title="Action", message="Proceeding to order customization...")

# Run the application
if __name__ == "__main__":
    PizzeriaHomePage().mainloop()
