import tkinter as tk
from tkinter import ttk


class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, style="Placeholder.TEntry", **kwargs)
        self.placeholder = placeholder
        self.focus = False

        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, e):
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            self["style"] = "TEntry"
            self.focus = True

    def insert_t(self, index, string):
        if self["style"] == "Placeholder.TEntry":
            self["style"] = "TEntry"

        self.tk.call(self._w, 'insert', index, string)

    def _add_placeholder(self, e):
        if not self.get():
            self.insert("0", self.placeholder)
            self["style"] = "Placeholder.TEntry"
            self.focus = False
    
    def check_cleared(self):
        return self.get() == self.placeholder or not self.get()
