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
    # 最优路径时，该节点的下一个节点，用来输出路径的时候使用
    self.next_node = None

class Graph(object):
  """图结构"""
  def __init__(self, pinyins, im):
    """根据拼音所对应的所有词汇组合，构造图

        以offset行存储，结构如下：

        ce      [册 测 测试 侧室 侧视 ... ]
        shi     [是 时 视频 食品 ...]
        pin     [拼 品 频 拼音  ...]
        yin     [银 音 因数 引述 ...]
        shu     [输入 输入法 树 输 书 ...]
        ru      [入 如 汝 入法 如法...]
        fa      [法 发 罚 伐 ...]

    """
    self.sequence = []
    for i in range(len(pinyins)):
      pys = []
      current_position = {}
      # pys记录以i开头的所有拼音串
      for j in range(i, len(pinyins)+1):
        py = '|'.join(pinyins[i:j])
        if py in im.lm.emission:
          pys.append(py)

      # current_position记录以i开头的所有拼音串，及其对应的词
      for py in pys:
        for word,emission in im.lm.emission[py].items():
          node = GraphNode(word, emission)
          current_position[word] = node

      self.sequence.append(current_position)
