import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from ttkthemes import *
import gui
import mid2exo
import json
import os


class Main(ThemedTk):
    def __init__(self, theme, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        self.generate_exo = ttk.Button(self.main_frame, text="EXO生成!!", command=lambda: self.generate())
        
        # 配置
        self.main_frame.pack(expand=True, fill=tk.BOTH)
        self.browse_frame.pack(side=tk.TOP)
        self.option_frame.pack(side=tk.TOP, anchor=tk.W, fill=tk.X, padx=8, pady=10)
        self.generate_exo.pack(side=tk.TOP, anchor=tk.E, padx=8)
        
        self.exo = mid2exo.EXO()
        self.browse_frame.mid.trace("w", self.set_bpm)
    
    def generate(self):
        try:
            self.exo.from_mid(self.browse_frame.mid_path.get(), self.option_frame.option1.get())
        except FileNotFoundError:
            tk.messagebox.showerror("MID to EXO エラー", "midiファイルが存在しません!!")
            return
        except mid2exo.NotesOverlapError as e:
            res = tk.messagebox.askquestion("MID to EXO エラー", f"同チャンネルのノーツが重なっているため、\n正常に生成できない可能性があります。\n続けますか？\n\n{e}")
            if res == "yes":
                self.exo.dump(self.browse_frame.exo_path.get())
                tk.messagebox.showinfo("MID to EXO", "生成しました")
            return
        except Exception as e:
            tk.messagebox.showerror("MID to EXO エラー", f"予期せぬエラーが発生しました。開発者にお知らせください\n\n{e}")
            return
        
        self.exo.dump(self.browse_frame.exo_path.get())
        tk.messagebox.showinfo("MID to EXO", "多分正常に生成できました!")
    
    def set_bpm(self, a, b, c):
        if os.path.exists(self.browse_frame.mid.get()):
            try:
                if self.browse_frame.bpm.get():
                    return
            except tk.TclError:
                pass

            self.browse_frame.bpm.set(self.exo.get_bpm(self.browse_frame.mid_path.get()))


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
