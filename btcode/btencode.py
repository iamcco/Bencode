#!/usr/bin/env python
# -.- coding: utf-8 -.-

class BtEncode(object):
    '''
    递归实现
    '''
    def encodeItem(self, item):
        if isinstance(item, dict):
            return self.encodeDict(item)
        elif isinstance(item, list):
            return self.encodeList(item)
        elif isinstance(item, str):
            return self.encodeStr(item)
        elif isinstance(item, int):
            return self.encodeInt(item)
        else:
            raise ValueError, u'非法参数'

    def encodeDict(self, item):
        encodeData = 'd'
        for key in item:
            encodeData += self.encodeStr(key)
            encodeData += self.encodeItem(item[key])
        return encodeData + 'e'

    def encodeList(self, item):
        encodeData = 'l'
        for value in item:
            encodeData += self.encodeItem(value)
        return encodeData + 'e'

    def encodeStr(self, item):
        encodeData = str(len(item)) + ':' + item
        return encodeData

    def encodeInt(self, item):
        encodeData = 'i' + str(item) + 'e'
        return encodeData

btEncode = BtEncode()

__all__ = ['btEncode']

if __name__ == '__main__':
    'test ...'
    adict = {
        'theKey': 'this is the value',
        'list': ['hello', 'world', 1, 2, {'listKey': 'list value for the key'}]
    }
    print btEncode.encodeItem(adict)
