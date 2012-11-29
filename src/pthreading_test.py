#!/usr/bin/env python

import urllib.request
import time
import threading


baseurl = 'http://127.0.0.1/v/'
fp = open('url.txt','wb')

def find_url(url):
    try:
        urllib.request.Request(url)
        res = urllib.request.urlopen(url)
        res.read()
        fp.write(url+'\r')
        return url
    except:
        pass

def main():
    time1 = time.ctime()
    urls = []
    threads = []
    for i in range(0,50):
        url = baseurl + str(i).zfill(5) + '/'
        urls.append(url)

    for i in urls:
        t = threading.Thread(target=find_url,arg=(i,))
        threads.append(t)
    for i in threads:
        i.start()
    for i in range(len(threads)):
        threads[i].join()
    print(time1)

if __name__ == '__main__':
    main()
    print(time.ctime())
