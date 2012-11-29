'''
Created on 2011-2-11

@author: hooxin
'''

import httplib2


httplib2.debuglevel=1

h=httplib2.Http('.cache')
response,content=h.request('http://diveintopython3.org/examples/feed.xml',headers={'cache-control':'no-cache'});
print(len(content))
print(response.status)
print(response.fromcache)
print(response.items())