Python エコシステム理解 から パッケージングまで を解説

# Intro 
## 講習に込めた願い
- 1. Python をモジュール化できるようになって欲しい
    - 組織の生産性を高めて行こう
- 2. Python アプリケーションのエコシステムを知って欲しい
    - 賢者は歴史から学ぶ...Pythonのエコシステムを聞いてプログラミングの動向を見極めて欲しい
- 3. Python にはまって世の中をハックできる人材になって欲しい
    - グルー言語としてかなり優秀
    - 特に CLI がこんなに簡単に作れるの？を味わって欲しい

## 自己紹介と経歴
- 適当に話す


---
ここからQiitaを使う

---

# Python の概要
##  Python とは
- https://qiita.com/nassy20/items/01c8fd54838d26fa5278

## Python 環境の種類
- https://qiita.com/nassy20/private/01b6fc4b389c1fa26ebb

# Python をモジュール化して再利用
## モジュールとは

## パッケージとは

## 名前空間とは

## Pythonのモジュール検索の仕組み と 仮想空間
- <モジュール検索の仕組み>
- [Python3 の venv モジュールはどのように仮想化を実現しているのかを調べてみた - Qiita](https://qiita.com/nassy20/items/0f438f638e03fbd9e566)

# パッケージングエコシステム
とても難解な Python のパッケージエコシステムを解説します。

## conda
- https://gist.github.com/nnashiki/948c60764022ddd049d0985b0f55ccb9
- アプリ化したり運用するフェーズではAnacondaは使いません

## pip の解説
- [pip に関して - Qiita](https://qiita.com/nassy20/private/e33cd5e27915878bd949)

# 名前空間に関して

- 名前空間とは
   - 名前の集合を分割することで衝突の可能性を低減しつつ参照を容易にする概念
   - https://ja.wikipedia.org/wiki/%E5%90%8D%E5%89%8D%E7%A9%BA%E9%96%93 の プログラミングセクションを参照
  
```
$ python3
Python 3.8.6rc1 (v3.8.6rc1:08bd63da6e, Sep  7 2020, 16:14:12) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
```

- オブジェクトは名前空間に存在している

ここからは https://docs.python.org/ja/3.9/tutorial/classes.html に記載があった

- 同じ関数名・class名・変数名でも、同じ名前空間内では別の名前をつければ問題なし
  - "名前空間 (namespace) とは、名前からオブジェクトへの対応付け (mapping) です。名前空間について知っておくべき重要なことは、異なった名前空間にある名前の間には全く関係がないということです。例えば、二つの別々のモジュールの両方で関数 maximize という関数を定義することができ、定義自体は混同されることはありません"
    
ex. 別の名前をつける例 (こうすれば競合しない)

```
from os import open as osopen
from gzip import open as gzipopen
```

ex.  (こうなっていまうと後勝ち)

```
from os import open
from gzip import open
```

- "組み込みの名前が入った名前空間は Python インタプリタが起動するときに作成され、決して削除されることはありません。"
    - だから組み込みとは競合するオブジェクトを定義してはいけないね
    - "組み込みの名前は実際にはモジュール内に存在します。そのモジュールは boo と呼ばれています。"
- "モジュールのグローバルな名前空間は、モジュール定義が読み込まれたときに作成されます。"
- "通常、モジュールの名前空間は、インタプリタが終了するまで残ります。"
    - モジュールに定義されたオブジェクトは残っているよね!
- "スコープ (scope) とは、ある名前空間が直接アクセスできるような、 Python プログラムのテキスト上の領域です。 "直接アクセス可能" とは、修飾なしに (訳注: spam.egg ではなく単に egg のように) 名前を参照した際に、その名前空間から名前を見つけようと試みることを意味します。"

## 名前空間の種類
- ローカル スコープ
  - "最初に探される、最も内側のスコープは、ローカルな名前を持っています。"
  - locals() で参照できる
- enclosing スコープ
  - "外側の(enclosing)関数のスコープは、近いほうから順に探され、ローカルでもグローバルでもない名前を持っています。
  - 関数がネストした時の話
- グローバル スコープ
  - "現在のモジュールのグローバルな名前を持っています。"
  - モジュール内のトップレベルに定義したら、そのモジュールの中では参照することができる
  - パッケージ や モジュール分けすれば衝突しないということ
- ビルトインスコープ
  - "一番外側の(最後に検索される)スコープはビルトイン名を持っています。"
    - 一番最後なのでビルトイン名と同じ名前を定義しないように気をつけよう
  - `dir(__builtins__)` でビルトインの中身を見ることができる
  - https://docs.python.org/ja/3/library/builtins.html#module-builtins
  - https://docs.python.org/ja/3/library/functions.html#built-in-funcs
  - https://docs.python.org/ja/3/library/constants.html#built-in-consts
- ちなみに
   - "Jupyter Notebookなどのセル（に入力する変数定義など）は「__main__」という名前のモジュールに含まれることになっている"
       - [［Python入門］関数のローカル変数とスコープ (3/3)：Python入門 - ＠IT](https://www.atmarkit.co.jp/ait/articles/1905/24/news019_3.html)
   - 対話モードと同じですね