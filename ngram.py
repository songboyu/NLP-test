# -*- coding:utf-8 -*-
import os

from common import u

class NGram(object):
    '''n元词频统计'''
    def __init__(self):
        self.unigram = {}
        self.bigram = {}
        self.wordDict = []
        dict = open('PinYin.txt')
        for line in dict:
            if len(line.strip()) > 0:
                self.wordDict.append(line.strip().split()[0])

    def scan(self, lines):
        '''
        逐行扫描，记录并更新ngram
        @param    sentence    list{str}
        @return   none
        '''
        words = []
        for line in lines:
            # 统计n元字频，若统计词频将 list(lines) 替换为 line.split('/')
            words.extend([w for w in list(lines) if len(w.strip())>0 and w in self.wordDict])
        print '[ Make words list finish ]'

        self.ngram(words)
        print '[ Hash finish ]'

        #unigram
        file = open("freq/1.txt","w")
        for i in self.unigram:
            file.write("%s\t%d\n" % (i,self.unigram[i]))
        file.close()
        print '[ Unigram file finish ]'

        #bigram
        file = open("freq/2.txt","w")
        for i in self.bigram:
            file.write("%s\t%d\n" % (i,self.bigram[i]))
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
            key = words[i]
            if key not in self.unigram:
                self.unigram[key] = 0
            self.unigram[key] += 1

        # bigram
        for i in range(1,len(words)):
            key = words[i] + '|' + words[i-1]
            if key not in self.bigram:
                self.bigram[key] = 0
            self.bigram[key] += 1

if __name__== '__main__':
    lines = []
    for parent,_,filenames in os.walk('corpus'):
        for filename in filenames:
            print filename
            path = os.path.join(parent,filename)
            file = open(path)

            for line in file:
                if len(line.strip()) > 0:
                    lines.append(line.strip())

    n = NGram()
    n.scan(lines)
