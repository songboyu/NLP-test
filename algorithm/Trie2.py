#!/usr/bin/env python

import pickle

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
        '''return all partially matched strings with the input key'''
        node = self.root
        matches = []
        for char in key:
            if char not in node.children:
                break
            node = node.children[char]
            if node.value:
                matches.append(node.value)
        return matches

def gen_trie(input_file, output_file):
    trie = Trie()
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            trie.add(line)
    with open(output_file, 'wb') as f:
        pickle.dump(trie, f)

if __name__ == '__main__':
    gen_trie('pinyin_trie_list.txt', 'pinyin_trie')