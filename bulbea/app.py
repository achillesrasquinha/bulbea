from __future__ import absolute_import

from collections import defaultdict
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from bulbea import AppConfig

class App(object):
    class Frame(tk.Frame):
        def __init__(self, master = None):
            self.master = master

            tk.Frame.__init__(self, master)

            self.createUI()

        def createUI(self):
            pass

    def __init__(self,
                 windowSize = (AppConfig.WINDOW_WIDTH, AppConfig.WINDOW_HEIGHT)):
        self.root       = tk.Tk()
        self.windowSize = windowSize

        self.root.title('{name} v{version}'.format(
            name    = AppConfig.NAME,
            version = '.'.join(map(str, AppConfig.VERSION))
        ))

        width, height   = self.windowSize
        self.root.geometry('{width}x{height}'.format(
            width  = width,
            height = height
        ))
        self.root.resizable(width  = False,
                            height = False)

        self.frame      = App.Frame(self.root)

    def run(self):
        self.root.mainloop()
