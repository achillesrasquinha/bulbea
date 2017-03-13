# imports - compatibility packages
from __future__ import absolute_import

# imports - standard packages
from collections import defaultdict
try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

# imports - third-party packages
import numpy as np
from PIL import Image, ImageTk

# module imports
import bulbea as bb

class App(object):
    class Frame(ttk.Frame):
        ENTRY_DATABASE = 'entry-search'
        ENTRY_SYMBOL   = 'entry-symbol'

        BUTTON_SEARCH  = 'button-search'

        CANVAS_PLOT    = 'canvas-plot'

        def __init__(self,
                     master      = None,
                     window_size = (bb.AppConfig.WINDOW_WIDTH, bb.AppConfig.WINDOW_HEIGHT)):
            self.master      = master
            self.window_size = window_size

            ttk.Frame.__init__(self, master)

            self.createUI()

        def createUI(self):
            width, height                        = self.window_size

            self.entry                           = defaultdict(tk.Entry)
            self.entry[App.Frame.ENTRY_DATABASE] = tk.Entry(self.master, width = 19)
            self.entry[App.Frame.ENTRY_DATABASE].grid(row    = 0,
                                                      column = 0,
                                                      ipady  = 3)
            self.entry[App.Frame.ENTRY_SYMBOL]   = tk.Entry(self.master, width = 19)
            self.entry[App.Frame.ENTRY_SYMBOL].grid(row    = 0,
                                                    column = 1,
                                                    ipady  = 3)

            self.button                          = defaultdict(tk.Button)
            self.button[App.Frame.BUTTON_SEARCH] = tk.Button(self.master,
                                                             text    = 'Search')
            self.button[App.Frame.BUTTON_SEARCH].grid(row        = 1,
                                                      column     = 0,
                                                      columnspan = 2,
                                                      sticky     = tk.E + tk.W)

    def __init__(self,
                 window_size = (bb.AppConfig.WINDOW_WIDTH, bb.AppConfig.WINDOW_HEIGHT)):
        self.root        = tk.Tk()
        self.window_size = window_size

        self.root.title('{name} v{version}'.format(
            name    = bb.AppConfig.NAME,
            version = '.'.join(map(str, bb.AppConfig.VERSION))
        ))

        width, height    = self.window_size
        self.root.geometry('{width}x{height}'.format(
            width  = width,
            height = height
        ))
        self.root.resizable(width  = tk.NO,
                            height = tk.NO)

        self.frame       = App.Frame(self.root, self.window_size)
        self.frame.button[App.Frame.BUTTON_SEARCH].config(command = self.on_click_search)

    def on_click_search(self):
        database = self.frame.entry[App.Frame.ENTRY_DATABASE].get()
        symbol   = self.frame.entry[App.Frame.ENTRY_SYMBOL].get()

        share    = bb.Share(database, symbol)
        axes     = share.plot(['Close'])

    def run(self):
        self.root.mainloop()
