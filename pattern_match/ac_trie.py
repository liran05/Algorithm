#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import pdb

reload(sys)
sys.setdefaultencoding('utf-8')


class ACTrieNode(object):
    """ACTrie节点

    Attributes:
        val: 本节点的值（非None即作为结束判断条件）
        children: 孩子节点
        fail: 失配跳转指针
    """
    def __init__(self, value=None):
        self.val = value
        self.children = {}
        self.fail = None

    def get_next(self, key):
        """从本节点开始，找到children中包含key的节点，如果找不到就返回根节点
        """
        if key in self.children.keys():
            return self.children[key]
        if self.fail is None:
            # fail为None就是根节点
            return self
        return self.fail.get_next(key)


class ACTrie(object):
    """ACTrie树

    Attribures:
        _root: 根节点
    """
    def __init__(self):
        self._root = ACTrieNode() # 生成root节点

    def insert(self, word):
        """将一个单词插入trie树
        """
        curr = self._root
        for char in word:
            if char not in curr.children:
                curr.children[char] = ACTrieNode()
            curr = curr.children[char]
        curr.val = word

    def update_failure(self):
        """更新failure跳转
        """
        bfs_queue = [self._root] # 利用list作为bfs缓存队列

        while len(bfs_queue) > 0:
            father = bfs_queue.pop(0) # 取出队列头部元素

            # BFS遍历父节点的所有子节点，为他们设置failure
            for key, child in father.children.items():
                bfs_queue.append(child) # 将当前元素放入队列尾部

                if father == self._root:
                    # 当前父节点是root时，其子节点的failure也指向root
                    child.fail = self._root
                else:
                    # 当前父节点不是root时，其子节点的failure尝试指向"(迭代)父节点的failure的同名子节点"
                    child.fail = father.fail.get_next(key)

    def search(self, text):
        """从源字符串中寻找目标字符串
        """
        match_set = set()
        curr = self._root

        for char in text:
            curr = curr.get_next(char)
            # 搜集匹配上的单词
            tmp_node = curr
            while tmp_node:
                if tmp_node.val:
                    match_set.add(tmp_node.val)
                tmp_node = tmp_node.fail
        return match_set


def main():
    trie = ACTrie()
    trie.insert("abcd")
    trie.insert("ab")
    trie.insert("bc")
    trie.insert("cf")
    trie.insert("cde")

    trie.update_failure()

    text = 'abcdefg'
    ret = trie.search(text)
    print ret

if __name__ == '__main__':
    main()
