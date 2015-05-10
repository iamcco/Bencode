#!/bin/usr/env python
# -.- coding: utf-8 -.-

import sys
from btcode.btdecode import btDecode
from btcode.btencode import btEncode


if __name__ == '__main__':
    'test ...'

    argv = sys.argv
    btName = ''
    if len(sys.argv) >= 2:
        btName = argv[1]
    else:
        print u'缺少btname'
        sys.exit(0)

    bt = btDecode.decodeItem(btName)
    if len(bt) > 0:
        bt = bt[0]
    else:
        raise ValueError, u'非法输入'

    #修改files, 反转文件及路径名，不反转后缀名
    if 'files' in bt['info']:
        for item in bt['info']['files']:
            #修改路径名字
            if 'path' in item:
                if len(item['path']) > 1:
                    for index in range(len(item['path']) - 1):
                        item['path'][index] = item['path'][index].decode('utf-8')[::-1].encode('utf-8')
                if not item['path'][-1].startswith('_____padding_file'):
                    fname = item['path'][-1].decode('utf-8').split('.')
                    vname = '.'.join(fname[0:-1])[::-1].split('.')
                    vname.append(fname[-1])
                    item['path'][-1] = (u'.'.join(vname)).encode('utf-8')
            #修改路径名字
            if 'path.utf-8' in item:
                if len(item['path.utf-8']) > 1:
                    for index in range(len(item['path.utf-8']) - 1):
                        item['path.utf-8'][index] = item['path.utf-8'][index].decode('utf-8')[::-1].encode('utf-8')
                if not item['path.utf-8'][-1].startswith('_____padding_file'):
                    fname = item['path.utf-8'][-1].decode('utf-8').split('.')
                    vname = u'.'.join(fname[0:-1])[::-1].split('.')
                    vname.append(fname[-1])
                    item['path.utf-8'][-1] = (u'.'.join(vname)).encode('utf-8')
        #修改名字
        if 'name' in bt['info']:
            bt['info']['name'] = bt['info']['name'].decode('utf-8')[::-1].encode('utf-8')
        #修改名字
        if 'name.utf-8' in bt['info']:
            bt['info']['name.utf-8'] = bt['info']['name.utf-8'].decode('utf-8')[::-1].encode('utf-8')

        #bt编码
        obt = btEncode.encodeItem(bt)
        #bt编码输出
        with file('output.torrent', 'wb') as output:
            output.write(obt)
