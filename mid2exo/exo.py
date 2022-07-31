from re import X
import mido
from .object import *
from .filter import *
from .error import *


class EXO:
    def __init__(self):
        self.objects = []
    
    def from_mid(self, fp):
        # midファイルの読み込み
        mid = mido.MidiFile(fp)
        
        max_layer = 0
        layers = {str(x+1): [] for x in range(99)}
        
        messages = mido.MidiTrack()
        for track in mid.tracks:
            for msg in track:
                if msg.type in ["note_on", "note_off"]:
                    messages.append(msg)
        messages.sort(key=lambda x:x.channel)
        
        current_channel = -999
        
        # note取得
        for msg in messages:
            if not current_channel == msg.channel:
                current_frame = 1
                if max_layer:
                    for x in range(int(list(layers.keys())[0]), max_layer+1):
                        del layers[str(x)]
                current_channel = msg.channel
            
            # note情報でなければ引き返す
            if msg.type not in ["note_on", "note_off"]:
                continue
            
            # AviUtl用の長さにする（？）
            time = msg.time // 4
            current_frame += time

            if msg.type == "note_on":
                # 空いてるレイヤーにnoteを入れる
                _layer = "0"
                for x in layers.keys():
                    if layers[x] == []:
                        if _layer == "0":
                            _layer = x
                    elif layers[x][0] == msg.note:
                        raise NotesOverlapError("同チャンネルのノーツが重なっています！")
                
                layers[_layer] = [msg.note, current_frame]
                max_layer = max(0, int(_layer))
            
            if msg.type == "note_off":
                note = []
                layer = "0"
                
                for x in layers.keys():
                    if not layers[x] == []:
                        if layers[x][0] == msg.note:
                            note = layers[x]
                            layer = x
                            break
                
                self.objects.append(
                    Object(
                        [FilterType.Position()],
                        start=note[1],
                        end=current_frame - 1,
                        layer=int(layer)
                    )
                )
                
                layers[layer] = []
    
    def dump(self, fp):
        open(fp, "w", encoding="cp932").close()
    
        with open(fp, "a", encoding="cp932") as f:
            for i, obj in enumerate(self.objects):
                # オブジェクト自体
                print(f"[{i}]", file=f)
                
                print(f"start={obj.start}", file=f)
                print(f"end={obj.end}", file=f)
                print(f"layer={obj.layer}", file=f)
                print(f"overlay={obj.overlay}", file=f)
                
                # フィルタ効果
                print(f"[{i}.0]", file=f)
                
                for j, flt in enumerate(obj.filters):
                    print(f"_name={flt.name}", file=f)
                    # フィルタのパラメータ
                    for n,v in flt.params.items():
                        print(f"{n}={v}", file=f)
