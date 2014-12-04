# -*- coding:utf-8 -*-
import os

from common import u

class NGram(object):
    '''n元词频统计'''
    def __init__(self, n):
        self.n = n
        self.unigram = {}
        self.bigram = {}
        self.wordDict = {}
        dict = open('dict.txt')
        for eachWord in dict:
            self.wordDict[eachWord.split('\t')[0].strip()] = 1

    def scan(self, sentence):
        '''
        逐行扫描，记录并更新ngram
        @param    sentence    list{str}
        @return   none
        '''
        # file your code here
        for line in sentence:
            self.ngram(line.split('/'))
        #unigram
        if self.n == 1:
            file = open("freq/word_freq.txt","w")
            for i in self.unigram:
                file.write("%s\t%d\n" % (i,self.unigram[i]))
        if self.n == 2:
            file = open("freq/Bigram_freq.txt","w")
            for i in self.bigram:
                file.write("%s\t%d\n" % (i,self.bigram[i]))

    def ngram(self, words):
        '''
        计算ngram
        @param    words       list{str}
        @return   none
        '''
        # unigram
        if self.n == 1:
            for i in range(0,len(words)):
                key = words[i]
                if key not in self.wordDict:
                    continue
                if key not in self.unigram:
                    self.unigram[key] = 1
                else:
                    self.unigram[key] += 1

        # bigram
        if self.n == 2:
            for i in range(1,len(words)):
                if words[i] not in self.wordDict:
                    continue
                if words[i-1] not in self.wordDict:
                    continue
                key = words[i] + '|' + words[i-1]
                if key not in self.bigram:
                    self.bigram[key] = 1
                self.bigram[key] += 1

if __name__== '__main__':
    lines = []
    for parent,_,filenames in os.walk('corpus_seg'):
        for filename in filenames:
            print filename
            path = os.path.join(parent,filename)
            file = open(path)

            for line in file:
                if len(line.strip())!=0:
                    lines.append(line.strip())

    uni = NGram(1)
    bi = NGram(2)

    uni.scan(lines)
    bi.scan(lines)
