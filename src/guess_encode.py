#!/usr/bin/env python

'''
猜测文本文件函数，支持bom-utf-8，utf-8,utf-16,gbk,gb2312,sjis

Created on 2012-12-6

'''
import codecs

support_codecs = ['utf8','utf16','gb2312','gbk','sjis']

def guess_textfile_encode(filepath):
    guess_file=open(filepath,'rb')
    bytes=guess_file.read()
    guess_file.close()
    
    #尝试编码
    def guess_encode(codecs1):
        if bytes[:3]==codecs.BOM_UTF8:
            bytes[3:].decode('utf8')
            return 'bom-utf-8'
        else:
            bytes.decode(codecs1)
        return codecs1

    #使用的编码
    use_code=None
    for code in support_codecs:
        try:
            use_code=guess_encode(code)
            break
        except:
            pass
    
    if use_code is None :
        print('not support codecs')
    else:
        print('codecs of this file is {code}'.format(code=use_code))

if __name__ == '__main__':
    guess_textfile_encode('test.txt')