# -*- coding:utf-8 -*-
'''
  author: songboyu
  create: 2013-10-27
  summary: 测试类
'''

import os, re

from common import u
from seg_method.fwd_max import fwd_mm_seg
from seg_method.bwd_max import bwd_mm_seg

CODEC = 'utf8'
def file_seg_process(filename, method):
    # 打开文件
    fp_dict = open('dict.txt')
    fp_input = open('corpus/'+filename)
    fp_output = open('corpus_seg/'+filename, 'w')
    
    wordDict = {} 
    # 读取字典到内存中
    for eachWord in fp_dict:
        wordDict[u(eachWord.split('\t')[0].strip(), 'utf-8')] = 1

    # 对input每一行操作
    for eachLine in fp_input:

        str = u(eachLine.strip(), 'utf-8')
        line_out = ''
        strlen = len(str)
        while strlen > 0:
            m = re.match(ur'[\u4e00-\u9fa5]+', str)
            if m is not None:
                subStr = m.group()
                if method == 0:
                    # 正向最大匹配
                    wordList = fwd_mm_seg(wordDict, 8, subStr)
                else:
                    # 逆向最大匹配
                    wordList = bwd_mm_seg(wordDict, 8, subStr)
                line_out += wordList[0].encode(CODEC)+'/'
                for eachWord in wordList[1:]:
                    line_out += eachWord.encode(CODEC)+'/'
                subLen = len(subStr)
                str = str[subLen:]
                strlen = strlen - subLen
                continue

            # subStr = str[0]
            # line_out += subStr.encode(CODEC)
            str = str[1:]
            strlen = strlen - 1

        if line_out.strip() == '':
            continue
        fp_output.write(line_out + '\n')
    # close file
    fp_input.close()
    fp_dict.close()
    fp_output.close()

if __name__ == '__main__':
    for _,_,filenames in os.walk('corpus'):
        for filename in filenames:
            print filename
            file_seg_process(filename, 0)