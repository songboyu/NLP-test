#!/usr/bin/env python
# -*- coding:utf-8 -*-
# * trie, prefix tree
# * Algorithm refered : http://blog.csdn.net/v_july_v/article/details/6897097
# * Codes Refered : http://blog.csdn.net/psrincsdn/article/details/8158182

class Node(object):
    def __init__(self):
        self.word = None
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.word = word

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False, None
            node = node.children[c]
        return True, node.word

    def delete(self, word, node=None, i=0):
        node = node if node else self.root
        c = word[i]
        if c in node.children:
            child_node = node.children[c]
            if len(word)==(i+1):
                return node.children.pop(c) if len(child_node.children)==0 else False
            elif self.delete(word, child_node, i+1):
                return node.children.pop(c) if (len(child_node.children)==0 and not child_node.word) else False
        return False

    def __collect_words(self, node):
        results = []
        if node.word:
            results.append(node.word)
        for k,v in node.children.iteritems():
            results.extend(self.__collect_words(v))
        return results

    def auto_complete(self, prefix_word):
        node = self.root
        for c in prefix_word:
            if c not in node.children:
                return []
            node = node.children[c]

        return self.__collect_words(node)

if __name__ == '__main__':
    tree = Trie()
    f = open('../freq/dict.txt')
    for line in f:
        tree.insert(line.split()[0])

    list = tree.auto_complete('我')
    for result in list:
        print result