#!/usr/bin/env python3

import tkinter as tk


def main_window():
    # Main Tinker Window
    base_window = tk.Tk(screenName='DArs-Weather')
    base_window.title('DArs-Weather')
    base_window.geometry('700x500')
    window = tk.Canvas(base_window, width=10000, height=10000, bg='black', bd=10)
    window.pack()
    window.create_text(100, 20, anchor='n', justify='left', fill='white',
                       font='Arial 24 bold', text='DArs-Weather')
    window.create_text(290, 60, anchor='n', justify='left', fill='white',
                       font='Arial 14 bold', text="""
DArs-Weather is a simple weather app that allows you to get weather of the city
selected. It writes the weather data from the National Weather Service (NWS)
into a database, then gets any comparable metrics from that of Elysium Planitia
on Mars.""")
    return window


def main():
    # Run the main part of the program. Takes no arguments
    window = main_window()
    # Loop the window
    window.mainloop()


if __name__ == '__main__':
    # Execute main code
    main()
