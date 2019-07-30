#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class KMP(object):
    """KMP算法
    成员变量:
        s: 源字符串
        t: 目标字符串
        pmt: 部分匹配表(向右挪动了1格, 位置0赋-1)
    """
    def __init__(self, s, t):
        self.s = s
        self.t = t
        self.pmt = {}

    def _get_pmt_1(self):
        """根据目标字符串，计算前后缀的最大重复子串
        此方法简单，但dn指针可能回退到-1，且up不是每次都递增，所以while循环次数最多可能是t长度的两倍
        """
        self.pmt[0] = -1 # 位置0赋值-1，为了计算方便
        up = 0 # up表示上指针，用来向后移动从而实现错位
        dn = -1 # dn表示下指针，用来记录匹配的位置

        while up < len(self.t):
            if dn == -1 or self.t[up] == self.t[dn]:
                up += 1
                dn += 1
                self.pmt[up] = dn
            else:
                dn = self.pmt[dn]

    def _get_pmt_2(self):
        """根据目标字符串，计算前后缀的最大重复子串
        此方法略复杂，但dn指针不后退且up每次都递增1，所以while循环次数为t的长度
        """
        self.pmt[0] = -1 # 位置0赋值-1，为了计算方便
        self.pmt[1] = 0 # 位置1赋值0，表示没有匹配
        up = 1 # up表示上指针，用来向后移动从而实现错位
        dn = 0 # dn表示下指针，用来记录匹配的位置
        same_len = 0 # 表示匹配的字符串长度

        while up < len(self.t):
            if self.t[up] == self.t[dn]:
                dn += 1
                same_len += 1
            else:
                same_len = 0
            up += 1
            self.pmt[up] = same_len

    def run_1(self):
        """完全匹配则返回源字符串匹配成功的起始点的下标，否则返回-1
        此方法简单，但循环次数比run_2多一倍
        """
        ptr_s = 0
        ptr_t = 0

        # 获取pmt
        self._get_pmt_1() #也可以用self._get_pmt_2()

        while ptr_t == -1 or ptr_s < len(self.s) and ptr_t < len(self.t):
            if self.s[ptr_s] == self.t[ptr_t]:
                ptr_s += 1
                ptr_t += 1
            else:
                ptr_t = self.pmt[ptr_t]

        if ptr_t == len(self.t):
            return ptr_s - ptr_t
        return -1

    def run_2(self):
        """完全匹配则返回源字符串匹配成功的起始点的下标，否则返回-1
        此方法复杂，但循环次数比run_1少一半
        """
        base = 0
        same_len = 0
        len_s = len(str_s)
        len_t = len(str_t)

        # 获取pmt
        self._get_pmt_2() #也可以用self._get_pmt_1()

        while base + len_t <= len_s:
            step = 0
            while step + same_len < len_t:
                if self.t[step + same_len] == self.s[base + step + same_len]:
                    # 当前字符相同，则继续比较下一个字符
                    step += 1
                    continue
                # 当前字符不相同，则结束次轮比较，更新base基准位置，启动下一轮比较
                same_len = self.pmt[step]
                base += step - same_len
                break
            # 完全匹配成功，算法结论，返回匹配成功的基准点位置下标
            if step + same_len == len_t:
                return base
        # 遍历了所有情况，最终匹配失败，返回-1
        return -1


if __name__ == '__main__':
    str_s = u"非常地非常地非常地喜欢你"
    str_t = u"非常地喜欢"
    model = KMP(str_s, str_t)
    print model.run_2()
