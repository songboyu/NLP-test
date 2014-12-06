# -*- coding:utf-8 -*-
'''
  author: songboyu
  modify: 2014-12-06
  summary: 加载语言模型
'''
class LanguageModel(object):

  def __init__(self):
    self.unigram_count = 0.0
    self.words_count = 0.0
    # 词频字典
    self.freq = {}
    # 发射概率（拼音/词）
    self.emission = {}
    # 加载一元词频
    # print '[ Loading Unigram.. ]'
    # self.load_unigram('freq/word_freq.txt')
    # 加载二元词频
    print '[ Loading Bigram.. ]'
    self.load_bigram('freq/bigram_freq_selected.txt')
    # 加载发射概率（拼音/词）
    print '[ Loading Unigram and Pinyins.. ]'
    self.load_emission('freq/dict_selected.txt')

  def load_unigram(self, filename):
    f =  open(filename, 'r')
    for line in f:
      key,freq = line.split()
      self.freq[key] = int(freq)
      self.unigram_count += 1
      self.words_count += int(freq)
    f.close()

  def load_bigram(self, filename):
    f =  open(filename, 'r')
    for line in f:
      key,freq = line.split()
      self.freq[key] = int(freq)
    f.close()

  def load_emission(self, filename):
    """加载发射概率，针对多音字 如：

     重 [zhong，chong]
     则 [zhong][重] 的emssion 值为 2
     使用时转换为 1/2

    """
    with open(filename,'r') as f:
      for line in f:
        if len(line.strip()) > 0:
          arr = line.strip().split()
          key = arr[0]
          freq = arr[1]
          pinyin = '|'.join([py for py in arr[2:]])

          self.freq[key] = int(freq)
          self.unigram_count += 1
          self.words_count += int(freq)

          if pinyin not in self.emission:
            self.emission[pinyin] = {}
          # 存储的概率是P(拼音|汉字),为了计算方便，所以用拼音做key
          if key not in self.emission[pinyin]:
              self.emission[pinyin][key] = 0
          self.emission[pinyin][key] += 1

  def bigram(self, word, condition):
    """获得转移概率"""
    key = word + '|' + condition
    if key not in self.freq:
      self.freq[key] = 0
    if condition not in self.freq:
      self.freq[condition] = 0
    C_1 = (float)(self.freq[key] + 0.5)
    C_2 = (float)(self.freq[condition] + 0.5*self.unigram_count)
    return C_1/C_2

  def init_score(self, word):
    """获得初始概率"""
    C_1 = (float)(self.freq[word])
    return C_1