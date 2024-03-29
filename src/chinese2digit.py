#!/usr/bin/env python

'''
Created on 2013-1-3

'''

dict_ = {'零':0,'一':1,'二':2,'三':3,'四':4,'五':5,
         '六':6,'七':7,'八':8,'九':9,'十':10,'百':100,
         '千':1000,'万':10000,'亿':10000*10000}

def getResult4Digit(a):
    count = 0
    result = 0
    tmp = 0
    billion = 0
    while count < len(a):
        tmpChr = a[count]
        tmpNum = dict_.get(tmpChr)
        
        if tmpNum == dict_['亿']:
            result += tmp
            result *= tmpNum
            billion = billion * dict_['亿'] + result
            result = 0
            tmp = 0
        elif tmpNum == dict_['万']:
            result += tmp
            result *= tmpNum
            tmp = 0
        elif tmpNum >= dict_['十']:
            if tmp == 0:
                tmp = 1
            result = result + tmpNum * tmp
            tmp = 0
        elif tmpNum is not None:
            tmp = tmp * dict_['十'] + tmpNum
        count += 1
    result = result + tmp
    result = result + billion
    return result

if __name__ == '__main__':
    test_map = {
    '三千五百二十三' : 3523,
    '七十五亿八百零七万九千二百零八':7508079208,
    '四万三千五百二十一':43521,
    '三千五百二十一':3521,
    '三千五百零八':3508,
    '三五六零':3560,
    '一万零三十':10030,
    '' : 0,
    #1 digit 个
    '零' : 0,
    '一' : 1,
    '二' : 2,
    '三' : 3,
    '四' : 4,
    '五' : 5,
    '六' : 6,
    '七' : 7,
    '八' : 8,
    '九' : 9,
    #2 digits 十
    '十' : 10,
    '十一' : 11,
    '二十' : 20,
    '二十一' : 21,
    #3 digits 百
    '一百' : 100,
    '一百零一' : 101,
    '一百一十' : 110,
    '一百二十三' : 123,
    #4 digits 千
    '一千' : 1000,
    '一千零一' : 1001,
    '一千零一十' : 1010,
    '一千一百' : 1100,
    '一千零二十三' : 1023,
    '一千二百零三' : 1203,
    '一千二百三十' : 1230,
    #5 digits 万
    '一万' : 10000,
    '一万零一' : 10001,
    '一万零一十' : 10010,
    '一万零一百' : 10100,
    '一万一千' : 11000,
    '一万零一十一' : 10011,
    '一万零一百零一' : 10101,
    '一万一千零一' : 11001,
    '一万零一百一十' : 10110,
    '一万一千零一十' : 11010,
    '一万一千一百' : 11100,
    '一万一千一百一十' : 11110,
    '一万一千一百零一' : 11101,
    '一万一千零一十一' : 11011,
    '一万零一百一十一' : 10111,
    '一万一千一百一十一' : 11111,
    #6 digits 十万
    '十万零二千三百四十五' : 102345,
    '十二万三千四百五十六' : 123456,
    '十万零三百五十六' : 100356,
    '十万零三千六百零九' : 103609,
    #7 digits 百万
    '一百二十三万四千五百六十七' : 1234567,
    '一百零一万零一百零一' : 1010101,
    '一百万零一' : 1000001,
    #8 digits 千万
    '一千一百二十三万四千五百六十七' : 11234567,
    '一千零一十一万零一百零一' : 10110101,
    '一千万零一' : 10000001,
    #9 digits 亿
    '一亿一千一百二十三万四千五百六十七' : 111234567,
    '一亿零一百零一万零一百零一' : 101010101,
    '一亿零一' : 100000001,
    #10 digits 十亿
    '十一亿一千一百二十三万四千五百六十七' : 1111234567,
    #11 digits 百亿
    '一百一十一亿一千一百二十三万四千五百六十七' : 11111234567,
    #12 digits 千亿
    '一千一百一十一亿一千一百二十三万四千五百六十七' : 111111234567,
    #13 digits 万亿
    '一万一千一百一十一亿一千一百二十三万四千五百六十七' : 1111111234567,
    #14 digits 十万亿
    '十一万一千一百一十一亿一千一百二十三万四千五百六十七' : 11111111234567,
    #17 digits 亿亿
    '一亿一千一百一十一万一千一百一十一亿一千一百二十三万四千五百六十七' : 1111111111234567,
    }

    for each in test_map:
        assert(test_map[each] == getResult4Digit(each))