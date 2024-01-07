#!/usr/bin/env python3
import tkinter as tk

large_font = ("Arial", 24, "bold")
regular_font = ("Arial", 12)


def retrieve_input(user_input):
    return user_input.get("1.0", 'end-1c')


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
        self.debugcheck = DebugCheck(container, self)
        self.runbutton = RunButton(container, self)

        # Draw and position frames
        self.header.grid(row=0, column=0, sticky="nw")
        self.description.grid(row=1, column=0, sticky="w", columnspan=3)
        self.locationdescr.grid(row=2, column=0, sticky="w")
        self.apikeydescr.grid(row=3, column=0, sticky="w")
        self.locationinput.grid(row=2, column=2, sticky="e")
        self.apikeyinput.grid(row=3, column=2, sticky="e")
        self.debugcheck.grid(row=4, column=0, sticky="w")
        self.runbutton.grid(row=5, column=0, sticky="s", columnspan=3)

        self.location = self.locationinput.location
        self.apikey = self.apikeyinput.apikey


class Header(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, justify='left', font=large_font, text='DArs-Weather')
        label.pack(padx=10, pady=10)


class Description(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, justify='left', font=regular_font, text="""
DArs-Weather is a simple weather app that allows you to get weather of the city
selected. It writes the weather data from the National Weather Service (NWS)
into a database, then gets any comparable metrics from that of Elysium Planitia
on Mars.""")
        label.pack(padx=10, pady=10)


class LocationDescr(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, font=regular_font, text="Enter City and State:")
        label.pack(padx=10, pady=10)


class APIKeyDescr(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, font=regular_font, text="Enter API Key:")
        label.pack(padx=10, pady=10)


class LocationInput(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        user_input = tk.Text(self, height=1, width=30)
        self.location = retrieve_input(user_input)
        user_input.pack()


class APIKeyInput(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        user_input = tk.Text(self, height=1, width=30)
        self.apikey = retrieve_input(user_input)
        user_input.pack()


class DebugCheck(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        debug_check = tk.Checkbutton(self, text="Debug", onvalue=True,
                                     offvalue=False, variable=self.debug)
        debug_check.pack()


def run():
    pass


# Button to run get user input and run main app
class RunButton(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button = tk.Button(self, text='RUN!', font=regular_font, command=run)
        button.pack()


if __name__ == '__main__':
    # Only used to import
    pass
