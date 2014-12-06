#!/usr/bin/env python

import sys, pickle

class TrieNode(object):
    def __init__(self):
        self.value = None
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                child = TrieNode()
                node.children[char] = child
                node = child
            else:
                node = node.children[char]
        node.value = key

    def search(self, key):
        node = self.root
        matches = []
        matched_length = 0
        for char in key:
            if char not in node.children:
                break
            node = node.children[char]
            if node.value:
                matches.append(node.value)
        return matches

class ScanPos(object):
    def __init__(self, pos, token = None, parent = None):
        self.pos = pos
        self.token = token
        self.parent = parent

class PinyinTokenizer(object):
    def __init__(self):
        with open('../algorithm/pinyin_trie') as f:
            self.trie = pickle.load(f)

    def tokenize(self, content):
        total_length = len(content)
        tokens = []
        candidate_pos = [ScanPos(0)]
        last_pos = None
        while candidate_pos:
            p = candidate_pos.pop()
            if p.pos == total_length:
                last_pos = p
                break
            matches = self.trie.search(content[p.pos:])
            for m in  matches:
                new_pos = ScanPos(len(m) + p.pos, m, p)
                candidate_pos.append(new_pos)
        pos = last_pos
        while pos:
            if pos.parent:
                tokens.insert(0, pos.token)
            pos = pos.parent
        return tokens

if __name__ == '__main__':
    tokenizer = PinyinTokenizer()
    print tokenizer.tokenize('zhonghuarenmingongheguo')
