# -*- coding:utf-8 -*-
'''
  author: songboyu
  modify: 2014-12-07
  summary: 有向图
'''
class GraphNode(object):
  """有向图节点"""
  def __init__(self, word, emission):
    # 当前节点所代表的汉字（即状态）
    self.word = word
    # 当前状态发射拼音的发射概率
    self.emission = emission
    # 最优路径时，从起点到该节点的最高分
    self.max_score = 0.0
    # 最优路径时，该节点的前一个节点，用来输出路径的时候使用
    self.next_node = None

class Graph(object):
  """有向图结构"""
  def __init__(self, pinyins, im):
    """根据拼音所对应的所有词汇组合，构造有向图

        以offset行存储，结构如下：

        ta   [他 她 它 他们]
        shuo [说 硕]
        de   [的]
        que  [确 确实 确定 确认]
        shi  [实 实在]
        zai  [在 在理]
        li   [理 理想 离 离线]

    """
    self.sequence = []
    for i in range(len(pinyins)):
      pys = []
      current_position = {}
      for j in range(i,len(pinyins)+1):
        py = '|'.join(pinyins[i:j])
        if py in im.lm.emission:
          pys.append(py)

      for py in pys:
        for word,emission in im.lm.emission[py].items():
          node = GraphNode(word, emission)
          current_position[word] = node

      # print pinyins[i],
      # for word in current_position:
      #   print word,
      # print

      self.sequence.append(current_position)
