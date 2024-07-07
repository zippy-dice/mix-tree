# mix-tree

## 概要
このプログラムはDQM等の配合が登場するゲームで目的のモンスターを作るために必要な材料や配合を木で表示します

## 例
1. 以下のような配合データを用意します
    ``` sample.txt
    すごいゴーレム すごいモンスター ゴーレム すごいモンスター ゴーレム
    すごいモンスター モンスター モンスター
    ゴーレム 魔法石 土人形
    土人形 粘土 人形
    粘土 そのへんで拾う
    人形 デパートで買う
    魔法石 異世界で買う
    モンスター ペットショップで買う
    ```
1. 以下のコマンドを実行します
    `./mix_tree.py --input sample.txt --target すごいゴーレム`
1. 以下のような結果が出力されます
    ``` output
    すごいゴーレム
    ┣━━ すごいモンスター
    ┃     ┣━━ モンスター
    ┃     ┃     ┗━━ ペットショップで買う
    ┃     ┗━━ モンスター
    ┃           ┗━━ ペットショップで買う
    ┣━━ ゴーレム
    ┃     ┣━━ 魔法石
    ┃     ┃     ┗━━ 異世界で買う
    ┃     ┗━━ 土人形
    ┃           ┣━━ 粘土
    ┃           ┃     ┗━━ そのへんで拾う
    ┃           ┗━━ 人形
    ┃                 ┗━━ デパートで買う
    ┣━━ すごいモンスター
    ┃     ┣━━ モンスター
    ┃     ┃     ┗━━ ペットショップで買う
    ┃     ┗━━ モンスター
    ┃           ┗━━ ペットショップで買う
    ┗━━ ゴーレム
            ┣━━ 魔法石
            ┃     ┗━━ 異世界で買う
            ┗━━ 土人形
                ┣━━ 粘土
                ┃     ┗━━ そのへんで拾う
                ┗━━ 人形
                        ┗━━ デパートで買う
    ```

## 配合データについて
- 配合データの各行は2列以上からなります
- 1列目は作られるモンスターになります
- 2列目以降は1列目のモンスターを作るのに必要な材料になります

## オプション
### --ommit_duplicates
- すでに出力した部分木を省略します
- `./mix_tree.py --input sample.txt --target すごいゴーレム --ommit_duplicates`の実行例
    ```
    すごいゴーレム
    ┣━━ すごいモンスター
    ┃     ┣━━ モンスター
    ┃     ┃     ┗━━ ペットショップで買う
    ┃     ┗━━ モンスター
    ┃           ┗━━ (略)
    ┣━━ ゴーレム
    ┃     ┣━━ 魔法石
    ┃     ┃     ┗━━ 異世界で買う
    ┃     ┗━━ 土人形
    ┃           ┣━━ 粘土
    ┃           ┃     ┗━━ そのへんで拾う
    ┃           ┗━━ 人形
    ┃                 ┗━━ デパートで買う
    ┣━━ すごいモンスター
    ┃     ┗━━ (略)
    ┗━━ ゴーレム
            ┗━━ (略)
    ```


### --ommit_noparent
- 材料が1つしか無いモンスターの出力を省略します
- `./mix_tree.py --input sample.txt --target すごいゴーレム --ommit_noparent`の実行例
    ```
    すごいゴーレム
    ┣━━ すごいモンスター
    ┃     ┣━━ モンスター
    ┃     ┗━━ モンスター
    ┣━━ ゴーレム
    ┃     ┣━━ 魔法石
    ┃     ┗━━ 土人形
    ┃           ┣━━ 粘土
    ┃           ┗━━ 人形
    ┣━━ すごいモンスター
    ┃     ┣━━ モンスター
    ┃     ┗━━ モンスター
    ┗━━ ゴーレム
            ┣━━ 魔法石
            ┗━━ 土人形
                ┣━━ 粘土
                ┗━━ 人形
    ```
