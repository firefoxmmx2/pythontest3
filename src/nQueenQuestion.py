num=8

class Queen(object):
    def __init__(self,n):
        self.lct = n
        self.prs = -1
        self.cdt = [i for i in range(num)]

def Count(q):
    s=0
    for i in range(num):
        if q.cdt[i] > 0: s+=1
    return s

def FindIt(q):
    u = q.prs+1
    while u<num and q.cdt[u] <= 0: u += 1
    if u < num :
        q.prs = u
        return True
    return False

def Pickup(q,n):
    x = q[n].lct
    y = q[n].prs

    for i in range(n+1,num,1):
        p = q[i].cdt
        p[y] += 1
        a = q[i].lct - x
        b = y - a
        if b >= 0 and b < num: p[b] += 1
        b = y + a
        if b >= 0 and b < num: p[b] += 1

def Select(q, n):
    j, k = 0, num + 1
    for i in range(n, num):
        t = Count(q[i])
        if k > t: j, k = i, t
    if j != n: q[n], q[j] = q[j], q[n]

def ShowIt(q):
    for i in range(n, num):
        for j in range(num):
            if q[j].lct == i:
                for k in range(num):
                    if q[j].prs == k:
                        print('*',)
                    else:
                        print('-',)
                print('')
    print('')
def Locate1():
    q = [Queen(i) for i in range(num)]
    i = 0
    j = 0
    while True:
        if q[i].prs < 0:
            Select(q, i)
        else:
            Pickup(q, i)
        if FindIt(q[i]):
            if i < num - 1:
                Select(q, i)
                i += 1
            else:
                j += 1
                yield j
        else:
            q[i].prs = -1
            i -= 1
            if i < 0: break
def Locate2():
    q = [Queen(i) for i in range(num)]
    i = 0
    j = 0
    while True:
        if q[i].prs >= 0:
            Pickup(q, i)
        if FindIt(q[i]):
            if i < num-1:
                Select(q, i)
                i += 1
            else:
                j += 1
                yield j
        else:
            q[i].prs = -1
            i -= 1
            if i< 0: break

if __name__ == '__main__':
    q = [Queen(i) for i in range(num)]
    import time
    t = time.time()
    next(Locate1())
    print('once cost {0}'.format(time.time() - t))
    print('-' * 12)

    t = time.time()
    next(Locate2())
    print('once cost {0}'.format(time.time() - t))

