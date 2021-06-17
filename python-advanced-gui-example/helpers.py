from tkinter import Tk


def clear_screen(screen: Tk):
    for element in screen.grid_slaves():
        element.destroy()