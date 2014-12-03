# -*- coding:utf-8 -*-

from model import LanguageModel

class GraphNode(object):
  def __init__(self, word, emission):
    # 当前节点所代表的汉字（即状态）
    self.word = word
    # 当前状态发射拼音的发射概率
    self.emission = emission
    # 最优路径时，从起点到该节点的最高分
    self.max_score = 0.0
    # 最优路径时，该节点的前一个节点，用来输出路径的时候使用
    self.prev_node = None


class Graph(object):
  """有向图结构"""
  def __init__(self, pinyins, im):
    """根据拼音所对应的所有汉字组合，构造有向图"""
    self.sequence = []
    for py in pinyins:
      current_position = {}
      # 从拼音、汉字的映射表中读取汉字及汉字到拼音的发射概率
      for word,emission in im.emission[py].items():
        node = GraphNode(word, emission)
        current_position[word] = node
      self.sequence.append(current_position)


class InputMethod(object):
  def __init__(self, uni_file, bi_file, py_file):
    self.lm = self.load_lm(uni_file, bi_file)
    # {'pinyin':{汉字 : 0.5}}
    self.emission = {}
    # 待求解的拼音输入
    self.pinyins = []
    self.graph = None
    self.load_emission(py_file)

    # viterbi递归的缓存
    self.viterbi_cache = {}

  def get_key(self, *words):
    return '_'.join([ str(w) for w in words])

  def load_emission(self, py_file):
    """加载发射概率"""
    with open(py_file,'r') as f:
      for line in f:
        if len(line.strip()) > 0:
          arr = line.strip().split()
          word = arr[0]
          pinyins = [py[0:-1] for py in arr[1:]]
          prop = float(1)/len(pinyins)
          for py in pinyins:
            if py not in self.emission:
              self.emission[py] = {}
            # 存储的概率是P(拼音|汉字),为了计算方便，所以用拼音做key
            self.emission[py][word] = prop

  def load_lm(self, uni_file, bi_file):
    """加载二元语言模型"""
    return LanguageModel(uni_file, bi_file)

  def translate(self, pinyins):
    self.graph = Graph(pinyins, self)
    self.pinyins = pinyins
    # 使用viterbi算法求解最大路径
    words = self.graph.sequence[-1].keys()
    max_node = None
    max_score = 0.0
    for k in words:
      node = self.graph.sequence[len(self.pinyins)-1][k]
      score = self.viterbi(len(self.pinyins)-1, k)
      if score > max_score:
        max_score = score
        max_node = node
    # 回溯输出最大路径
    result = []
    while True:
      result.insert(0,max_node.word)
      if max_node.prev_node:
        max_node = max_node.prev_node
      else:
        break
    print ' '.join(self.pinyins)
    print ' '.join(result)

  def viterbi(self, t, k):
    """
      第t个位置出现k字符的概率，记为p_t(k)
    """
    if self.get_key(t,k) in self.viterbi_cache:
      return self.viterbi_cache[self.get_key(t,k)]
    node = self.graph.sequence[t][k]
    if t == 0:
      state_transfer = self.lm.get_init_prop(k)
      emission_prop = self.emission[self.pinyins[t]][k]
      node.max_score = 1.0 * state_transfer * emission_prop
      self.viterbi_cache[self.get_key(t,k)] = node.max_score
      return node.max_score
    # 获得前一个状态所有可能的汉字
    pre_words = self.graph.sequence[t-1].keys()
    for l in pre_words:
      state_transfer = self.lm.get_trans_prop(k, l)
      emission_prop = self.emission[self.pinyins[t-1]][l]
      score = self.viterbi(t-1, l) * state_transfer * emission_prop
      if score > node.max_score:
        node.max_score = score
        node.prev_node = self.graph.sequence[t-1][l]
    self.viterbi_cache[self.get_key(t,k)] = node.max_score
    return node.max_score

def main():
  im = InputMethod('freq/word_freq.txt', 'freq/Bigram_freq.txt', 'PinYin.txt')
  print ''
  im.translate(['zhong','wen','shu','ru','fa'])
  print ''
  im.translate(['ren','min','ri','bao','ri','ren','min'])
  print ''
  im.translate(['zhong','hua','ren','min','gong','he','guo'])
  print ''
  im.translate(['yi','zhi','mei','li','de','xiao','hua'])

if __name__ == '__main__':
  main()