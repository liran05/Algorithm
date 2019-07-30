#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import pdb

reload(sys)
sys.setdefaultencoding('utf-8')


class BruteForce(object):
    """BF算法
    成员变量:
        str_s: 源字符串
        str_t: 目标字符串
    """
    def __init__(self, str_s, str_t):
        self.str_s = str_s
        self.str_t = str_t

    def run(self):
        """完全匹配则返回源字符串匹配成功的起始点的下标，否则返回-1
        """
        base = 0 # 记录源字符串与目标字符串对齐的基准点
        len_s = len(self.str_s)
        len_t = len(self.str_t)

        while base + len_t <= len_s:
            step = 0
            while step < len_t:
                if str_t[step] == self.str_s[base + step]:
                    # 当前字符相同，则继续比较下一个字符
                    step += 1
                    continue
                # 当前字符不相同，则结束次轮比较，更新base基准位置，启动下一轮比较
                base += 1
                break
            # 完全匹配成功，算法结论，返回匹配成功的基准点位置下标
            if step == len_t:
                return base
        # 遍历了所有情况，最终匹配失败，返回-1
        return -1


if __name__ == '__main__':
    str_s = u"非常地非常地非常地喜欢你"
    str_t = u"非常地非常地喜欢"
    model = BruteForce(str_s, str_t)
    print model.run()
