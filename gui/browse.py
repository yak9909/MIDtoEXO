import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from .widgets import *


class BrowseFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.mid_browse = None
        self.exo_browse = None
        
        # .mid と .exo の一括参照ボタン
        self.browse_all = ttk.Button(self, text="一括参照", command=lambda: self.fileopen())
        
        # midファイルのパス
        self.mid = tk.StringVar()
        self.mid.trace('w', self.update)
        # exo生成フォルダのパス
        self.exo = tk.StringVar()
        self.exo.trace('w', self.update)
        # BPM値
        self.bpm = tk.IntVar()
        self.bpm.set(66)
        
        self.mid_placeholder = ".midファイル"
        self.exo_placeholder = ".exo生成フォルダ"
        
        self.browse_frame = ttk.Frame(self, relief=tk.SUNKEN, padding=4, width=10)
        self.param_frame = ttk.Frame(self, relief=tk.SUNKEN, padding=4)
        
        # .mid参照
        self.mid_label = ttk.Label(self.browse_frame, text=".mid", padding=[8,0,0,0])
        self.mid_path = PlaceholderEntry(self.browse_frame, self.mid_placeholder, textvariable=self.mid)
        self.mid_browse = ttk.Button(self.browse_frame, text="参照", padding=[1, 2], command=lambda: self.mid_fileopen())
        
        # .exo生成フォルダ参照
        self.exo_label = ttk.Label(self.browse_frame, text=".exo", padding=[8,0,0,0])
        self.exo_path = PlaceholderEntry(self.browse_frame, self.exo_placeholder, textvariable=self.exo)
        self.exo_browse = ttk.Button(self.browse_frame, text="参照", padding=[1, 2], command=lambda: self.exo_fileopen())
        
        # BPMの設定
        self.bpm_label = ttk.Label(self.param_frame, text="FPS:")
        self.bpm_entry = ttk.Entry(self.param_frame, textvariable=self.bpm, width=4)
        
        self.update()
        
        self.widgets_place()
    
    # Widgetの配置
    def widgets_place(self):
        # 一括参照ボタン
        self.browse_all.grid(column=0, row=0, pady=10)
        
        # 参照フレーム
        self.browse_frame.grid(column=0, row=1, padx=8)
        
        # mid
        self.mid_label.grid(column=0, row=0, pady=10)
        self.mid_path.grid(column=1, row=0, padx=5)
        self.mid_browse.grid(column=2, row=0, padx=5)
        # exo
        self.exo_label.grid(column=0, row=1, pady=10)
        self.exo_path.grid(column=1, row=1, padx=5)
        self.exo_browse.grid(column=2, row=1, padx=5)
        
        # パラメータフレーム
        self.param_frame.grid(column=1, row=1, padx=8)
        
        # BPM
        self.bpm_label.grid(column=0, row=0)
        self.bpm_entry.grid(column=1, row=0)
    
    def mid_fileopen(self):
        filetypes = [('Midiファイル', ['*.mid', '*.midi'])] 
        file = tk.filedialog.askopenfilename(title="Midiファイルを選択してください", filetypes=filetypes)
        
        if file:
            self.mid_path.delete(0,"end")
            self.mid_path.insert_t(0, file.replace("/", "\\"))
    
    def exo_fileopen(self):
        filetypes = [('AviUtlオブジェクトファイル', '*.exo')] 
        file = tk.filedialog.asksaveasfilename(title="EXOファイルの保存先を選択してください", filetypes=filetypes, defaultextension="exo")
        
        if file:
            self.exo_path.delete(0,"end")
            self.exo_path.insert_t(0, file.replace("/", "\\"))
    
    def fileopen(self):
        self.mid_fileopen()
        self.exo_fileopen()
        self.update()
    
    def update(self, a=None, b=None, c=None):
        if self.mid_browse is None or self.exo_browse is None:
            return
        
        if self.mid_path.check_cleared() and self.exo_path.check_cleared():
            self.mid_browse.configure(state="disabled")
            self.exo_browse.configure(state="disabled")
            return

        self.mid_browse.configure(state="normal")
        self.exo_browse.configure(state="normal")