import tkinter as tk
from tkinter import ttk


class OptionFrame(ttk.LabelFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.option1 = tk.BooleanVar()
        self.option1_check = ttk.Checkbutton(self, text="偶数番目は別レイヤーに配置", variable=self.option1)
        
        self.options_place()
    
    def options_place(self):
        self.option1_check.grid(column=0, row=0, padx=10, pady=8)
