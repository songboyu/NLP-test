# -*- coding:utf-8 -*-
'''
  author: songboyu
  modify: 2014-12-06
  summary: 统计unigram,bigram词频
'''
import os,re

CODEC = 'utf8'
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
        逐行扫描，ngram结果记录到文件中
        @param    sentence    list{str}
        @return   none
        '''
        words = []
        for line in lines:
            # 统计n元词频
            words.append('<li>')
            wordlist = [
                w.encode(CODEC)
                for w in list(line.decode(CODEC).split('/'))
                if len(w.strip())>0
            ]
            words.extend(wordlist)
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
        统计ngram
        @param    words       list{str}
        @return   none
        '''
        partten = ur'([\u4e00-\u9fa5]|<li>|</li>)+'
        # unigram
        for i in range(0,len(words)):
            if not re.search(partten, words[i].decode(CODEC)):
                continue
            key = words[i]
            if key not in self.unigram:
                self.unigram[key] = 0
            self.unigram[key] += 1

        # bigram
        for i in range(1,len(words)):
            if not re.search(partten, words[i].decode(CODEC)):
                continue
            if not re.search(partten, words[i-1].decode(CODEC)):
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
