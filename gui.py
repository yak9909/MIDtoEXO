import tkinter as tk
from tkinter import ttk
from ttkthemes import *
import gui
import json
import os


class Main(ThemedTk):
    def __init__(self, theme, *args, **kwargs):
        super().__init__()
        self.title('MID to EXO')
        self.minsize(width=370, height=300)
        
        # スタイルの設定
        self.theme = ttk.Style()
        self.theme.theme_use(theme[0])
        # widgets.PlaceholderEntry の placeholder の色
        self.theme.configure("Placeholder.TEntry", foreground=theme[1])
        
        # メインフレーム
        self.main_frame = ttk.Frame(self)
        # ファイル参照フレーム
        self.browse_frame = gui.BrowseFrame(self.main_frame)
        # オプションフレーム
        self.option_frame = gui.OptionFrame(self.main_frame, text="オプション", relief="groove", padding=[0,0,0,50])
        # EXO生成ボタン
        self.generate_exo = ttk.Button(self.main_frame, text="EXO生成!!")
        
        self.main_frame.pack(expand=True, fill=tk.BOTH)
        self.browse_frame.pack(side=tk.TOP)
        self.option_frame.pack(side=tk.TOP, anchor=tk.W, fill=tk.X, padx=8, pady=10)
        self.generate_exo.pack(side=tk.TOP, anchor=tk.E, padx=8)


if __name__ == "__main__":
    themes = {
        "light": ["arc", "#d3d3d3"],
        "dark": ["equilux", "#656565"]
    }
    
    theme = themes["light"]
    
    if os.path.exists("./config.json"):
        config = json.load( open("./config.json", mode="r", encoding="utf-8") )
        if config.get("dark_mode"):
            theme = themes["dark"]
    
    main = Main(theme=theme)
    main.mainloop()
