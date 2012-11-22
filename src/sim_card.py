#!/usr/bin/env python


import random
import time

'''
模拟洗牌
'''

def flushcards(cards,count,pushstatic):
    '''
    cards:牌
    count:洗牌次数
    '''
    print('洗牌次数:'+str(count))
    clen = len(cards)

    while count > 0:
        #随即切牌
        p2 = cards[:clen//2+random.randint(-1,1)]
        p2_len = len(p2)
        p4 = cards[p2_len:]
        p4_pos = 0
        p4_len = len(p4)
        for i in p2:
            pos = random.randint(p4_pos,p4_len)
            p4.insert(pos,i)
            p4_pos = pos
            p4_len = len(p4)
        for i in p4:
            i_index = cards.index(i)
            pushstatic[i][i_index] += 1
        count -= 1
        #有必要自己手动删除变量引用吗?
        del p2
        del cards
        #?
        cards = p4

def main():
    ls = [str(i) for i in range(2,11)] + list('JQKA')
    static = {i:[0 for j in ls] for i in ls}
    print("准备洗牌")
    t2 = time.clock()
    flushcards(ls,100000,static)
    t4 = time.clock()

    print("{0:>5}{1}".format("Pos->",
        "".join(['{0:^7}'.format(x) for x in range(1,len(ls)+1)])))
    for rs in sorted(static.keys()):
        print("{0:>5}{1}".format(str(rs)+"->","".join(["{0:^7}".format(x) for x in static[rs]])))
    print("结束,耗时{0}秒!".format(t4-t2))

if __name__ == '__main__':
    main()

