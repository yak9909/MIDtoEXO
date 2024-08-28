# [RPPtoEXO v2.0](https://github.com/Garech-mas/RPPtoEXO-ver2.0) でいいです




このプロジェクト非公開にしたい

# MIDtoEXO
 ![](https://img.shields.io/badge/python-3.10-blue)
 [![](https://img.shields.io/github/license/yak9909/MIDtoEXO)](LICENSE)

 まいまいさんの [RPPtoEXO](https://github.com/maimai22015/RPPtoEXO) のMID版がほしいと思い立って制作を始めたプロジェクトです<br>
 `.mid` ファイルからAviUtlのオブジェクトファイル (`.exo`) を作成できますが<br>
 上手く使えば普通にAviUtlのオブジェクトライブラリとして使えるかもしれない<br>
 ( なお既にある模様 -> [exolib](https://github.com/tikubonn/exolib) )

## ダウンロード
 [Releases](https://github.com/yak9909/MIDtoEXO/releases) から最新の MIDtoEXO をダウンロードしてzipファイルを解凍してください<br>
 ちなみに起動クッッッッッソ遅いです　なめてんの？ってくらい　ちゃんと起動するので安心してお待ち下さい<br>
 遅いのが嫌だったら [requirements.txt](requirements.txt) を `pip install -r requirements.txt` して
 [guirun.pyw](guirun.pyw) を起動するとムッチャ早く起動できます

## config.json について
 ```json
 {
     "dark_mode": false
 }
 ```
 この `false` ってところを `true` にするとダークモードになります（誰得）

## ライブラリのつかいかた
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

## License
 このプロジェクトは[MITライセンス](LICENSE)です
