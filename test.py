# -*- coding:utf-8 -*-
'''
  author: songboyu
  create: 2013-10-27
  summary: 测试类
'''

import re

from common import u
from method.fwd_max_match import fwd_mm_seg
from method.bwd_max_match import bwd_mm_seg


CODEC = 'utf8'
def file_seg_process(method, filename):
    # 打开文件
    fp_dict = open('dict.txt')
    fp_input = open('_input/'+filename)
    fp_output = open('_output/'+filename, 'w')
    
    wordDict = {} 
    # 读取字典到内存中
    for eachWord in fp_dict:
        wordDict[u(eachWord.strip(), 'utf-8')] = 1

    # 对input每一行操作
    for eachLine in fp_input:
        str = u(eachLine.strip(), 'utf-8')
        line_out = ''
        strlen = len(str)
        while strlen > 0:              
            m = re.match('\w+', str)
            if m is not None:
                subStr = m.group()
                line_out += subStr.encode(CODEC)
                subLen = len(subStr)
                str = str[subLen:]
                strlen = strlen - subLen
                continue
            
            m = re.match(ur'[\u4e00-\u9fa5]+', str)
            if m is not None:
                subStr = m.group()
                if method == 0:
                    # 正向最大匹配
                    wordList = fwd_mm_seg(wordDict, 4, subStr)
                else:
                    # 逆向最大匹配
                    wordList = bwd_mm_seg(wordDict, 4, subStr)

                line_out += wordList[0].encode(CODEC)
                for eachWord in wordList[1:]:
                    line_out += eachWord.encode(CODEC)+'/'
                subLen = len(subStr)
                str = str[subLen:]
                strlen = strlen - subLen
                continue
         
            subStr = str[0]
            line_out += subStr.encode(CODEC)
            str = str[1:]
            strlen = strlen - 1

        fp_output.write(line_out + '\n')
    # close file
    fp_input.close()
    fp_dict.close()
    fp_output.close()


if __name__ == '__main__':
    file_seg_process(1, '4.txt')
