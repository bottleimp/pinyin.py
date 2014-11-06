#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
    Modified by anakin.yan@gmail.com
"""

__all__ = ["PinYin"]

import pkgutil


class PinYin(object):
    def __init__(self):
        __package__ = 'pinyin'
        self.word_dict = {}
        self.data = pkgutil.get_data(__package__, 'data/word.data')

    def load_word(self):
        for line in self.data.split('\n'):
            self.word_dict[line[:5].strip()] = line[8:]

    def hanzi2pinyin(self, s):
        result = []
        if not isinstance(s, unicode):
            s = s.decode('utf-8')

        for char in s:
            key = '%X' % ord(char)
            result.append(self.word_dict.get(key, char).split()[0][:-1].lower())

        return result

    def hanzi2pinyin_split(self, s='', delimiter=''):
        result = self.hanzi2pinyin(s=s)
        if delimiter == '':
            return result
        else:
            return delimiter.join(result)

    def hz2py(self, s, delimiter=' '):
        return delimiter.join([p[0] for p in self.hanzi2pinyin(s)])

if __name__ == '__main__':
    test = PinYin()
    test.load_word()
    s = "钓鱼岛是中国的"
    print "in: %s" % s
    print "out: %s" % str(test.hanzi2pinyin(s))
    print "out: %s" % test.hanzi2pinyin_split(s=s, delimiter='-')
    print "out: %s" % test.hz2py(u'钓鱼岛', delimiter=' ')
