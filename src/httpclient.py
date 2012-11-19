'''
Created on 2011-2-10

@author: hooxin
'''

from http.client import HTTPConnection

HTTPConnection.debuglevel=1

from urllib.request import urlopen

response=urlopen('http://diveintopython3.org/examples/feed.xml')
print(response)