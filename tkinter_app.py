#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from sys import version_info
if version_info.major == 2:
    # We are using Python 2.x
    import Tkinter as tk
elif version_info.major == 3:
    # We are using Python 3.x
    import tkinter as tk

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


class MenuFile(tk.Menu):

    def __init__(self, app, master):
        tk.Menu.__init__(self, master, tearoff=0)
        self.title = "File"
        self.add_command(label="New",
                         compound=tk.LEFT,
                         command=lambda: popupmsg("Not supported just yet!"))
        self.add_command(label="Save",
                         compound=tk.LEFT,
                         command=lambda: popupmsg("Not supported just yet!"))
        self.add_command(label="Save as",
                         compound=tk.LEFT,
                         command=lambda: popupmsg("Not supported just yet!"))
        self.add_separator()
        self.add_command(label="Exit",
                         compound=tk.LEFT,
                         command=app.destroy)

    def get_title(self):
        return self.title


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hello World", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "My app")
        self.geometry('{width:d}x{height:d}+0+0'.format(width=self.winfo_screenwidth(),
                                                        height=self.winfo_screenheight()))
        # Set main frame
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Set the menu bar
        self.menubar = tk.Menu(self)
        for M in [MenuFile]:
            Menu = M(self, self.menubar)
            self.menubar.add_cascade(label=Menu.get_title(), menu=Menu)
        tk.Tk.config(self, menu=self.menubar)

        self.frames = {}
        for F in [StartPage]:
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def main():
    app = MyApp()
    app.mainloop()


if __name__ == "__main__":
    main()
