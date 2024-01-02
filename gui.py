#!/usr/bin/env python3
import tkinter as tk

large_font = ("Arial", 24, "bold")
regular_font = ("Arial", 12)


def main_window():
    # Main Tinker Window
    base_window = tk.Tk()
    base_window.title('DArs-Weather')
    base_window.geometry('800x600')
    base_window.grid()
    # window = tk.Canvas(base_window, width=10000, height=10000, bg='black', bd=10)
    header = tk.Label(base_window, anchor="n", justify='left', font=('Arial', 24),
                      text='DArs-Weather')
    description = tk.Label(base_window, anchor='n', justify='left', font='Arial',
                           text="""
DArs-Weather is a simple weather app that allows you to get weather of the city
selected. It writes the weather data from the National Weather Service (NWS)
into a database, then gets any comparable metrics from that of Elysium Planitia
on Mars.""")
    header.grid(row=0, column=0, sticky='nw', pady=2)
    description.grid(row=1, sticky='n', pady=2)

    return base_window


class MainApp(tk.Tk):
    # Run all the components of the App together
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.title("DArs-Weather")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create the frames
        self.header = Header(container, self)
        self.description = Description(container, self)
        self.locationdescr = LocationDescr(container, self)
        self.apikeydescr = APIKeyDescr(container, self)
        self.locationinput = LocationInput(container, self)
        self.apikeyinput = APIKeyInput(container, self)
        self.runbutton = RunButton(container, self)

        # Draw and position frames
        self.header.grid(row=0, column=0, sticky="n")
        self.description.grid(row=1, column=0, sticky="w", columnspan=3)
        self.locationdescr.grid(row=2, column=0, sticky="w")
        self.apikeydescr.grid(row=3, column=0, sticky="w")
        self.locationinput.grid(row=2, column=2, sticky="e")
        self.apikeyinput.grid(row=3, column=2, sticky="e")
        self.runbutton.grid(row=4, column=0, sticky="s", columnspan=3)


class Header(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Header")
        label.pack(padx=10, pady=10)


class Description(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Description")
        label.pack(padx=10, pady=10)


class LocationDescr(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter City and State:")
        label.pack(padx=10, pady=10)


class APIKeyDescr(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter API Key:")
        label.pack(padx=10, pady=10)


class LocationInput(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Location Input")
        label.pack(padx=10, pady=10)


class APIKeyInput(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="API Input")
        label.pack(padx=10, pady=10)


class RunButton(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="RUN!")
        label.pack(padx=10, pady=10)


if __name__ == '__main__':
    # Run the main part of the program. Takes no arguments
    dars_app = MainApp()
    dars_app.mainloop()
