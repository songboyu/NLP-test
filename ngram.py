# -*- coding:utf-8 -*-
'''
  author: songboyu
  modify: 2014-12-06
  summary: 统计unigram,bigram词频
'''
import os,re

class NGram(object):
    '''n元词频统计'''
    def __init__(self):
        self.unigram = {}
        self.bigram = {}
        self.wordDict = []
        # dict = open('dict.txt')
        # for line in dict:
        #     if len(line.strip()) > 0:
        #         self.wordDict.append(line.strip())

    def scan(self, lines):
        '''
        逐行扫描，记录并更新ngram
        @param    sentence    list{str}
        @return   none
        '''
        words = []
        num = 0
        for line in lines:
            num += 1
            print num
            # 统计n元字频，若统计词频将 list(line.decode('utf8')) 替换为 line.decode('utf8').split('/')
            words.append('<li>')
            words.extend([w.encode('utf8') for w in list(line.decode('utf8').split('/')) if len(w.strip())>0])#and w in self.wordDict])
            words.append('</li>')

        self.ngram(words)

        print '[ Hashed ]'

        #unigram
        file = open("freq/word_freq.txt","w")
        for key,value in self.unigram.items():
            file.write("%s\t%d\n" % (key, value))
        file.close()
        print '[ Unigram file finish ]'

        #bigram
        file = open("freq/bigram_freq.txt","w")
        for key,value in self.bigram.items():
            file.write("%s\t%d\n" % (key, value))
        file.close()
        print '[ Bigram file finish ]'

    def ngram(self, words):
        '''
        计算ngram
        @param    words       list{str}
        @return   none
        '''
        # unigram
        for i in range(0,len(words)):
            if not re.search(ur'([\u4e00-\u9fa5]|<li>|</li>)+', words[i].decode('utf8')):
                continue

            key = words[i]
            if key not in self.unigram:
                self.unigram[key] = 0
            self.unigram[key] += 1

        # bigram
        for i in range(1,len(words)):
            if not re.search(ur'([\u4e00-\u9fa5]|<li>|</li>)+', words[i].decode('utf8')):
                continue
            if not re.search(ur'([\u4e00-\u9fa5]|<li>|</li>)+', words[i-1].decode('utf8')):
                continue

            key = words[i] + '|' + words[i-1]
            if key not in self.bigram:
                self.bigram[key] = 0
            self.bigram[key] += 1

if __name__== '__main__':
    lines = []
    for parent,_,filenames in os.walk('corpus_seg'):
        for filename in filenames:
            print filename
            path = os.path.join(parent,filename)
            file = open(path)

            for line in file:
                if len(line.strip()) > 0:
                    lines.append(line.strip())

    n = NGram()
    n.scan(lines)
