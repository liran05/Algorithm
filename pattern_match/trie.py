#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import pdb

reload(sys)
sys.setdefaultencoding('utf-8')


class TrieNode(object):
    """Trie节点

    Attributes:
        _val: 本节点的值（非None即作为结束判断条件）
        _next: 后继节点
    """
    def __init__(self, value=None):
        self._val = value
        self._next = {}

    def set_value(self, value=None):
        """为当前节点设置值
        """
        self._val = value

    def get_value(self):
        """获取当前节点的值
        """
        return self._val

    def set_next(self, key, value=None):
        """为当前节点添加一个后继节点
        """
        if key not in self._next:
            self._next[key] = TrieNode(value)
        return self._next[key]

    def get_next(self, key):
        """从当前节点获取指定的后继节点
        """
        if key not in self._next:
            return None
        return self._next[key]


class Trie(object):
    """Trie树
    Attribures:
        _root: 根节点
    """
    def __init__(self):
        # 生成root节点
        self._root = TrieNode()

    def insert(self, word):
        """将一个单词插入trie树
        """
        curr = self._root

        for char in word:
            curr = curr.set_next(char)
        curr.set_value(True)

    def search(self, word):
        """检索一个单词是否trie树中存在
        """
        curr = self._root
        ret = False

        for i, c in enumerate(word):
            curr = curr.get_next(c)
            if curr is None:
                break
            if i + 1 == len(word) and curr.get_value() is True:
                ret = True
                break
        return ret

    def startsWith(self, prefix):
        """检索trie树中是否有prefix开头的单词
        """
        curr = self._root
        ret = True

        for c in prefix:
            curr = curr.get_next(c)
            if curr is None:
                ret = False
                break
        return ret


def main():
    trie = Trie()
    trie.insert("app")
    trie.insert("apple")
    print trie.search("app")


if __name__ == '__main__':
    main()
