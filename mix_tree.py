#!/usr/bin/python3
import argparse
from indent import Indent 

def create_mix_data(args):
    """
    配合表を構築して返す
    """
    # 配合表。これをreturnする
    mix_data = {}

    # ファイルを読み込んで配合法を作成
    with open(args.input) as f:
        for s_line in f:
            # 入力ファイルの1列目が'#'ならその行は無視
            if s_line[0] == '#': continue

            # 改行だけの行はスキップする
            if s_line == '\n': continue

            # mix_data[成果物] = [素材1, 素材2, ...]といったdictを作成
            monster_list = s_line.split()
            monster_child = monster_list[0]
            monster_parent = []
            for i in range(1, len(monster_list)):
                monster_parent.append(monster_list[i])
            mix_data[monster_child] = monster_parent

    return mix_data


def print_mix_tree_recursive(args, mix_data, target_monster, indent=Indent(), made_monster = set()):
    """
    再帰的に配合ツリーを出力
    mix_data: 
    target_monster: 
    indent_level: 
    maked_mosnter: ここに入っているモンスターの素材は出力しない
    """
    # インデントに配慮しながら(略)というモンスター名を出力
    print(str(indent) + target_monster)

    # target_monsterが配合表に無いなら再帰を打ち止め
    if(target_monster not in mix_data): return

    # --ommit_dublicatesが有効でtarget_monsterの部分木を出力したことがあるなら省略する
    if(args.ommit_duplicates and target_monster in made_monster): 
        # 素材を表示しないなら(略)という表記を省略
        if args.ommit_noparent: return

        # インデントに配慮しながら(略)という表記を出力
        indent.add_indent(True)
        print(str(indent) + "(略)")
        indent.del_indent()
        return

    # --ommit_noparentが有効で材料の数が1以下の場合、再帰を打ち止め
    # 材料の数が1というのは配合を使用せずに入手することを想定している
    if args.ommit_noparent and len(mix_data[target_monster]) <= 1: return

    # 作成したことあるモンスターとして記録しておく。--ommit_duplicates用
    made_monster.add(target_monster)


    for i, parent_monster in enumerate(mix_data[target_monster]):
        # インデントに配慮しながら、材料の材料を出力といったことを再帰的に行う
        indent.add_indent(i + 1 == len(mix_data[target_monster]))
        print_mix_tree_recursive(args, mix_data, parent_monster, indent, made_monster)
        indent.del_indent()


def main():
    # 配合表
    # mix_data['キングスライム']はキングスライムの素材を意味する
    mix_data = {}

    # コマンドライン引数
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='配合表データのパス')
    parser.add_argument('--target', '-t', type=str, help='作成したいモンスター')
    parser.add_argument('--ommit_duplicates', '-o', action='store_true', help='すでに出力した部分木を省略する')
    parser.add_argument('--ommit_noparent', '-p', action='store_true', help='材料数が1のものを省略する')
    args = parser.parse_args()

    # 配合表を用意
    mix_data = create_mix_data(args)

    # 配合ツリーを出力
    # indent = Indent(
    #         indent_base1="┣━　 ",\
    #         indent_base2="┃　 ",\
    #         indent_base3="┗━　 ",\
    #         indent_base4="　 　 ")
    indent=Indent()
    print_mix_tree_recursive(args, mix_data, args.target, indent)



if __name__ == '__main__':
    main()
