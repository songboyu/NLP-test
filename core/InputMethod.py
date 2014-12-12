# -*- coding:utf-8 -*-
'''
  author: songboyu
  modify: 2014-12-06
  summary: 拼音串(已切分)转汉字串
'''
from core.Model import LanguageModel
from core.Graph import Graph

class InputMethod(object):
  def __init__(self):
    # 加载语言模型
    self.lm = LanguageModel()
    # 待求解的拼音输入
    self.pinyins = []
    # 有向图
    self.graph = None
    # viterbi递归的缓存
    self.viterbi_cache = {}

  def get_key(self, *words):
    return '_'.join([ str(w) for w in words])

  def translate(self, pinyins):
    '''
    @param pinyins: 拼音列表
    @return:        汉字串
    '''
    self.graph = Graph(pinyins, self)
    self.viterbi_cache = {}
    self.pinyins = pinyins

    # 从第一个字开始使用viterbi算法求解最大路径
    words = self.graph.sequence[0].keys()
    max_node = None
    max_score = 0.0
    for k in words:
      node = self.graph.sequence[0][k]
      score = self.viterbi(0, k)
      if score > max_score:
        max_score = score
        max_node = node

    # 输出中文路径
    result = []
    while True:
      result.append(max_node.word)
      if not max_node.next_node:
        break
      max_node = max_node.next_node

    print (' '.join(pinyins))
    return (''.join(result)).decode('utf8')

  def viterbi(self, t, k):
    '''第 t 个位置出现 k 词的概率

    @param t:   pinyin数组下标
    @param k:   词
    @return:    最大分值
    '''
    if self.get_key(t,k) in self.viterbi_cache:
      return self.viterbi_cache[self.get_key(t,k)]

    node = self.graph.sequence[t][k]
    # 当前词长度
    length_self = len(k.decode('utf8'))
    # 开始时加载句首词词频作为初始概率
    if t == 0:
      init_prop = self.lm.get_init_score(k)
    else:
      init_prop = 1

    # 到达结尾
    if t == len(self.pinyins)-length_self:
      pinyin = '|'.join(self.pinyins[t:t+length_self])
      emission_prop = 1/self.lm.emission[pinyin][k]

      node.max_score = emission_prop
      self.viterbi_cache[self.get_key(t,k)] = node.max_score
      return node.max_score

    # 获得下一个状态所有可能的词
    next_words = self.graph.sequence[t+length_self].keys()
    for word in next_words:
      # 下一个词长度
      length_next = len(word.decode('utf8'))
      state_transfer = self.lm.get_trans_pro(word, k)
      pinyin = '|'.join(self.pinyins[t+length_self : t+length_self+length_next])

      emission_prop = 1/self.lm.emission[pinyin][word]
      # 递归调用，直到最后一个拼音结束
      score = self.viterbi(t+length_self, word) * state_transfer * emission_prop * init_prop

      if score > node.max_score:
        node.max_score = score
        node.next_node = self.graph.sequence[t+length_self][word]

    self.viterbi_cache[self.get_key(t,k)] = node.max_score
    return node.max_score
