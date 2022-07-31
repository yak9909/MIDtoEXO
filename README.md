# MIDtoEXO
 まいまいさんの[RPPtoEXO](https://github.com/maimai22015/RPPtoEXO)のMID版がほしいと思い立って制作を始めたプロジェクトです<br>
 `.mid` ファイルからAviUtlのオブジェクトファイル (`.exo`) を作成できますが<br>
 上手く使えば普通にAviUtlのオブジェクトライブラリとして使えるかもしれない<br>
 ( なお既にある模様 -> [exolib](https://github.com/tikubonn/exolib) )

# Usage
 [example.py](example.py)
 ```py
 import mid2exo


 # EXOインスタンスを作成
 exo = mid2exo.EXO()
 
 # midファイルからオブジェクトを作成
 exo.from_mid("example.mid")

 # example.exo としてオブジェクトファイルをダンプ
 exo.dump("example.exo")
 ```

# License
 このプロジェクトは[MITライセンス](LICENSE)です
