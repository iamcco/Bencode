#!/usr/bin/env python
# -.- coding: utf-8 -.-

import re

class BtDecode(object):
    '''
    递归实现
    '''

    def decodeV(self, data):
        if data[0] == 'd':
            return self.decodeDict(data[1:])
        elif data[0] == 'l':
            return self.decodeList(data[1:])
        elif data[0] == 'i':
            return self.decodeInt(data)
        elif re.match('[0-9]', data[0]):
            return self.decodeStr(data)
        else:
            raise ValueError, u'匹配到非法字符串'

    def decodeDict(self, data):
        dv = {}
        while data[0] != 'e':
            temp = self.decodeStr(data)
            dvKey = temp[0]
            dvVal = self.decodeV(temp[1])
            dv[dvKey] = dvVal[0]
            data = dvVal[1]
        return (dv, data[1:])

    def decodeList(self, data):
        lv = []
        while data[0] != 'e':
            temp = self.decodeV(data)
            lv.append(temp[0])
            data = temp[1]
        return (lv, data[1:])

    def decodeStr(self, data):
        mc = re.match('([0-9]+):', data)
        strkey = ''
        strLen = 0
        if mc != None:
            strLen = mc.group(1)
            count = len(strLen) + 1
            strLen = int(strLen) + count
            strkey = data[count:strLen]
        return (strkey, data[strLen:])

    def decodeInt(self, data):
        intVal = ''
        strLen = 0
        mc = re.match('i(-?[0-9]+)e', data)
        if mc != None:
            intVal = int(mc.group(1))
            strLen = len(mc.group())
        return (intVal, data[strLen:])

    def decodeItem(self, btName):
        bt = []
        with open(btName, 'rb') as btfile:
            data = btfile.read(-1)
            while len(data) > 0:
                temp = self.decodeV(data)
                bt.append(temp[0])
                data = temp[1]
        return bt

btDecode = BtDecode()

__all__ = ['btDecode']

if __name__ == '__main__':
    'test ...'
    for eachline in btDecode.decodeItem('./test.torrent'):
        print eachline
