'''
Created on 2011-2-10

@author: hooxin
'''

import httplib2

h=httplib2.Http('.cache')
response,content=h.request('http://diveintopython3.org/examples/feed.xml')
print(response.status)
print(content[:52])
print(len(content))
