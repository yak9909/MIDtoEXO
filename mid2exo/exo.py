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
        
        current_channel = 0
        max_layer = 0
        layers = {str(x+1): [] for x in range(99)}
        
        # note取得
        for track in mid.tracks:
            current_frame = 1
            if max_layer:
                for x in range(int(list(layers.keys())[0]), max_layer+1):
                    del layers[str(x)]
            
            for msg in track:
                if msg.type not in ["note_on", "note_off"]:
                    continue
                
                time = msg.time // 4
                current_frame += time
                
                print(msg)

                if msg.type == "note_on":
                    for x in layers.keys():
                        if layers[x] == []:
                            layers[x] = [msg.note, current_frame]
                            max_layer = max(0, int(x))
                            break
                        elif layers[x][0] == msg.note:
                            raise NotesOverlapError("同チャンネルのノーツが重なっています！")
                
                
                if msg.type == "note_off":
                    nt = []
                    ind = "0"
                    
                    for x in layers.keys():
                        if not layers[x] == []:
                            if layers[x][0] == msg.note:
                                nt = layers[x]
                                ind = x
                                break
                    
                    self.objects.append(
                        Object(
                            [FilterType.Position()],
                            start=nt[1],
                            end=current_frame - 1,
                            layer=int(ind)
                        )
                    )
                    
                    layers[ind] = []
    
    def dump(self, fp):
        open(fp, "w", encoding="cp932").close()
    
        with open(fp, "a", encoding="cp932") as f:
            for i, obj in enumerate(self.objects):
                # オブジェクト自体
                print(f"[{i}]\n", file=f)
                
                print(f"start={obj.start}\n", file=f)
                print(f"end={obj.end}\n", file=f)
                print(f"layer={obj.layer}\n", file=f)
                print(f"overlay={obj.overlay}\n", file=f)
                
                # フィルタ効果
                print(f"[{i}.0]\n", file=f)
                
                for j, flt in enumerate(obj.filters):
                    print(f"_name={flt.name}\n", file=f)
                    # フィルタのパラメータ
                    for n,v in flt.params.items():
                        print(f"{n}={v}", file=f)
