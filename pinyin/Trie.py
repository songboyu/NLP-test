# -*- coding:utf-8 -*-
'''
  author: songboyu
  modify: 2014-12-06
  summary: 建立Tire树
'''

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

    def find(self, word):
        node = self.root
        matches = []
        for c in word:
            if c not in node.children:
                break
            node = node.children[c]
            if node.word:
                matches.append(node.word)
        if len(matches) == 0:
            return False
        return True

    def find_initial_with(self, prefix_word):
        node = self.root
        for c in prefix_word:
            if c not in node.children:
                return False
            node = node.children[c]
        if not node:
            return False
        return True

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

    def get_initial_with(self, prefix_word):
        node = self.root
        for c in prefix_word:
            if c not in node.children:
                return []
            node = node.children[c]

        return self.__collect_words(node)

if __name__ == '__main__':
    tree = Trie()
    f = open('pinyin_list.txt')
    for line in f:
        tree.insert(line.split()[0])

    # list = tree.get_initial_with('li')
    # for result in list:
    #     print result
    print tree.find_initial_with('woa')