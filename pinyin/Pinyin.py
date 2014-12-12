# -*- coding:utf-8 -*-
'''
  author: songboyu
  modify: 2014-12-07
  summary:拼音流切分
'''
from Trie import Trie

class pinyin(object):
    def __init__(self, pinyins):
        self.pinyins = pinyins
        # 读入所有有效拼音
        self.tree = Trie()
        f = open('pinyin/pinyin_list.txt')
        # f = open('pinyin_list.txt')
        for line in f:
            self.tree.insert(line.split()[0])
        f.close()

    def split(self):
        '''
        分割函数
        @param pinyin:  拼音串 str
        @return:        分割后的拼音列表 list
        '''
        # 可作为拼音开头的字母
        pinyin_initials = ['a', 'b', 'e', 'p', 'm', 'f', 'd',
                           't', 'n', 'l', 'g', 'k', 'h', 'j',
                           'q', 'x', 'r', 'z', 'c', 's', 'y', 'w']
        # pinyin_initials = self.tree.root.children
        iuv = ['i','u','v']
        grn = ['g','r','n']

        input = ''
        result = []

        for i in range(len(self.pinyins)):
            c = self.pinyins[i]
            # 读入字符 c
            input += c
            # c是 i|u|v，并且是拼音串的首字母
            if c in iuv and len(input)==1:
                return False,None
            # 当前拼音有效或者是有效拼音的一部分
            if self.tree.find_initial_with(input):
                continue
            # c是声母
            if c in pinyin_initials:
                # 前面的拼音为有效拼音
                if self.tree.find_initial_with(input[:-1]):
                    # 在c前断开
                    result.append(input[:-1])
                    input = input[-1:]
                    continue
                else:
                    return False,None
            # 倒数第二个字母为 g|r|n
            elif input[-2:-1] in grn:
                # 在 g|r|n 前断开有效
                if self.tree.find_initial_with(input[:-2]):
                    # 在 g|r|n 前断开
                    result.append(input[:-2])
                    input = input[-2:]
                    continue
                # 在 g|r|n 后断开有效
                elif self.tree.find_initial_with(input[:-1]):
                    # 在 g|r|n 后断开
                    result.append(input[:-1])
                    input = input[-1:]
                    continue
            else:
                # 单独断开
                result.append(input)
                input = ''

        result.append(input)

        return True,result

if __name__ == '__main__':
    pinyins = pinyin('woaizhonghuarenmingongheguo')
    print pinyins.split()