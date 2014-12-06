# -*- coding:utf-8 -*-
'''
  author: songboyu
  modify: 2014-12-06
  summary: 字符编码转换
'''
def u(s, encoding):
    'converted other encoding to unicode encoding'
    if isinstance(s, unicode):
        return s
    else:
        return unicode(s, encoding)