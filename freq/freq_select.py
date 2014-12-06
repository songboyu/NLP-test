# -*- coding:utf-8 -*-
'''
  author: songboyu
  modify: 2014-12-07
  summary: 筛选出现频率较高的一元、二元key
'''
if __name__ == '__main__':
    input = open('dict.txt', 'r')
    output = open('dict_selected.txt', 'w')
    for line in input:
        list = line.split()
        key = list[0]
        freq = list[1]
        pinyin = ' '.join(list[2:])
        if int(freq)>50:
            output.write(key+'\t'+freq+'\t'+pinyin+'\n')
    input.close()
    output.close()