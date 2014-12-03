# -*- coding:utf-8 -*-

class LanguageModel(object):

  def __init__(self, uni_file, bi_file):
    self.words = []
    self.freq = {}

    print '---Hashing Unigram..'
    f =  open(uni_file,'r')
    for line in f:
      key,freq = line.split()
      self.freq[key] = int(freq)
      for i in range(int(freq)):
        self.words.append(key)

    print '---Hashing Bigram..'
    f =  open(bi_file,'r')
    for line in f:
      key,freq = line.split()
      self.freq[key] = int(freq)

  def get_trans_prop(self, word, condition):
    """获得转移概率"""
    key = word + '|' + condition
    if key not in self.freq:
      self.freq[key] = 0
    if condition not in self.freq:
      self.freq[condition] = 0
    C_1 = (float)(self.freq[key] + 1.0)
    C_2 = (float)(self.freq[condition] + len(self.words))
    return C_1/C_2

  def get_init_prop(self, word):
    """获得初始概率"""
    return self.get_trans_prop(word,'<s>')

  def get_prop(self, *words):
    """获得指定序列的概率"""
    init = self.get_init_prop(words[0])
    product = 1.0
    for i in range(1,len(words)):
      product *= self.get_trans_prop(words[i],words[i-1])
    return init * product

def main():
    lm = LanguageModel('freq/word_freq.txt', 'freq/Bigram_freq.txt',)
    print 'total words: ', len(lm.words)
    print 'total keys: ', len(lm.freq)
    print 'P(结|团) = ', lm.get_trans_prop('结','团')
    print 'P(斗|奋) = ', lm.get_trans_prop('斗','奋')
    print 'P(法|入) = ', lm.get_trans_prop('法','入')
    print 'P(发|入) = ', lm.get_trans_prop('发','入')
    print 'P(奋斗|团结) = ', lm.get_trans_prop('奋斗','团结')

if __name__ == '__main__':
    main()