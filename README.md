Python エコシステム理解 から パッケージングまで を解説

# Intro 
## 講習に込めた願い
- 1. Python をモジュール化できるようになって欲しい
    - 組織の生産性を高めて行こう
- 2. Python アプリケーションのエコシステムを知って欲しい
    - 賢者は歴史から学ぶ...Pythonのエコシステムの変遷を聞いて動向を見極めて欲しい
- 3. Python にはまって世の中をハックできる人材になって欲しい
    - グルー言語としてかなり優秀
    - 特に CLI がこんなに簡単に作れるの？を味わって欲しい
- 4. 環境周りのつまづきで Python を嫌いにならないで欲しい

## 自己紹介と経歴
- なんか話す

# Python の概要
##  Python とは
- https://qiita.com/nassy20/items/01c8fd54838d26fa5278

## Python 環境の種類
- https://qiita.com/nassy20/private/01b6fc4b389c1fa26ebb

# Python をモジュール化して再利用
## モジュール と パッケージ
- https://qiita.com/nassy20/private/b3625b11b918dbbae33a

## 名前空間とは
- https://qiita.com/nassy20/private/3e5fd7a4ab976d025179

## Pythonのモジュール検索の仕組み と 仮想環境 について
- [Python モジュール・パッケージ 検索・ロードの仕組み - Qiita](https://qiita.com/nassy20/private/378928364751aa03939b)
- [Python3 の venv モジュールはどのように仮想化を実現しているのかを調べてみた - Qiita](https://qiita.com/nassy20/items/0f438f638e03fbd9e566)

# パッケージングエコシステム
難解な Python パッケージのエコシステムを解説します。

## conda・Anaconda
- https://gist.github.com/nnashiki/948c60764022ddd049d0985b0f55ccb9
- アプリ化したり運用するフェーズでは Anaconda は使いません

## pip の解説
- [pip に関して - Qiita](https://qiita.com/nassy20/private/e33cd5e27915878bd949)

## パッケージ開発の手順を見てみよう
- https://github.com/nnashiki/wordcloud-cli
- 手順
    - https://github.com/nnashiki/wordcloud-cli/blob/main/training.md
- chapter毎のソースコード
    - https://github.com/nnashiki/wordcloud-cli/tags
