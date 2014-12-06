# -*- coding:utf-8 -*-
'''
  author: songboyu
  modify: 2014-12-07
  summary: 拼音输入法测试类
'''
from core.InputMethod import InputMethod
if __name__ == '__main__':
  im = InputMethod()
  print im.translate(['a','li','ba','ba','ji','tuan'])
  print im.translate(['ce','shi','zhong','wen','shu','ru','fa'])
  print im.translate(['zhong','hua','ren','min','gong','he','guo'])
  print im.translate(['yi','zhi','mei','li','de','xiao','hua'])
  print im.translate(['wo','ai','bei','jing','tian','an','men'])
  print

  while True:
    pinyins = raw_input("Pinyin: ")
    print im.translate(pinyins.split())