class Indent:
    def __init__(
            self,
            indent_base1="  ┣━━ ",\
            indent_base2="  ┃   ",\
            indent_base3="  ┗━━ ",\
            indent_base4="      "):

        # INITは配合素材のラストで無いもの
        # LASTは配合素材の最後のやつ
        self.INIT=0
        self.LAST=1

        # self.INITとself.LASTからなるリスト
        # これを元にインデントを構築する
        self.indent_list = []

        self.indent_base1 = indent_base1
        self.indent_base2 = indent_base2
        self.indent_base3 = indent_base3
        self.indent_base4 = indent_base4
    
    def __str__(self):
        res = ""
        for i, elem in enumerate(self.indent_list):
            if i + 1 == len(self.indent_list) and elem == self.INIT:
                res += self.indent_base1

            if i + 1 < len(self.indent_list) and elem == self.INIT:
                res += self.indent_base2

            if i + 1 == len(self.indent_list) and elem == self.LAST:
                res += self.indent_base3
            
            if i + 1 < len(self.indent_list) and elem == self.LAST:
                res += self.indent_base4

        return res
    
    def add_indent(self, material_last=False):
        """
        インデントを増やすメソッド
        material_last: 最後の素材かどうか？
        """
        self.indent_list.append(self.LAST if material_last else self.INIT)
    
    def del_indent(self):
        """
        インデントを減らすメソッド
        """
        self.indent_list.pop()
