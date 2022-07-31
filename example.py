import mid2exo


# EXOインスタンスを作成
exo = mid2exo.EXO()

# midファイルからオブジェクトを作成
exo.from_mid("example.mid")

# example.exo としてオブジェクトファイルをダンプ
exo.dump("example.exo")
