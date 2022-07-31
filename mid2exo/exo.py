import mido
from .object import *
from .filter import *


class EXO:
    def __init__(self):
        self.objects = []
    
    def from_mid(self, fp):
        # midファイルの読み込み
        mid = mido.MidiFile(fp)
        
        # noteの範囲
        note_time = []
        
        current_frame = 1
        
        # note取得 -> 範囲をリストに追加していく
        for msg in mid.tracks[1]:
            if msg.type not in ["note_on", "note_off"]:
                continue

            # AviUtlのFPSに合わせる（？）
            note_time.append(msg.time // 4)
            
            if msg.type == "note_off":
                self.objects.append(
                    Object(
                        [FilterType.Position()],
                        start=current_frame + note_time[0],
                        end=current_frame + sum(note_time) -1
                    )
                )
                current_frame += sum(note_time)
                
                # 初期化
                note_time = []
    
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
