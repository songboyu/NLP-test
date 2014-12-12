# -*- coding:utf-8 -*-
'''
  author: songboyu
  modify: 2014-12-06
  summary: 正向、逆向最大匹配分词测试
'''

import os, re

from common import u,strQ2B,tsplit
from seg_method.fwd_max import fwd_mm_seg
from seg_method.bwd_max import bwd_mm_seg

CODEC = 'utf8'
def file_seg_process(filename, method):
    '''
    @param filename: 文件名
    @param method:   分词算法 { 0:正向，1:逆向 }
    '''
    # 打开文件
    fp_dict = open('dict.txt')
    fp_input = open('corpus/'+filename)
    fp_output = open('corpus_seg/'+filename, 'w')
    
    wordDict = {} 
    # 读取字典到内存中
    for eachWord in fp_dict:
        wordDict[u(eachWord.split()[0].strip(), CODEC)] = 1

    # 对input每一行操作
    str = ''
    for eachLine in fp_input:
        line_out = ''
        # 每一段作为一行输入给分词函数
        sub = strQ2B(u(eachLine.strip(), CODEC))
        if not sub.startswith('  '):
            str += sub
            continue
        strlen = len(str)
        while strlen > 0:
            # 英文字符或数字--原文输出
            m = re.match(r'\w+', str)
            if m is not None:
                subStr = m.group()
                line_out += subStr.encode(CODEC)+'/'
                subLen = len(subStr)
                str = str[subLen:]
                strlen = strlen - subLen
                continue
            # 短句结尾标志--输出换行
            if str[0:1].encode(CODEC) in [',','。','!','?',':']:
                subStr = str[0:1]
                line_out += '\n'
                subLen = len(subStr)
                str = str[subLen:]
                strlen = strlen - subLen
            # 汉字--分词处理，输出 词/词
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
            # 其他特殊字符--跳过
            str = str[1:]
            strlen = strlen - 1
        # 跳过处理后为空行的段落
        if len(line_out.strip()) == 0:
            continue
        # 写入文件
        fp_output.write(line_out + '\n')
        str = sub
    # close file
    fp_input.close()
    fp_dict.close()
    fp_output.close()

if __name__ == '__main__':
    for _,_,filenames in os.walk('corpus'):
        for filename in filenames:
            print filename
            file_seg_process(filename, 1)