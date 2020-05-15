# Pythonのunderbarの種別

1. 関数の前
'''python
def _underscore(x):
  return n
'''
他の場所からは呼ばれなくなるが、class._underscore()のようにclass内の関数としては呼べる。

2. 関数の後
'''python
def list_(x):
  return n
'''
予約語と同じ名前をつけたい時に使う。

3. 変数の前に2つ
'''python
__span
'''
name mangling(名前就職)と呼ばれる。class内の変数をユニークにする。上記の場合は_classname__spanに置き換わる。

4. 関数の前後に2つずつ
'''python
class classname
  def __init__(self, var):
'''
特殊メソッド。オブジェクトの振る舞いの変更できる。__init__等用意されている。