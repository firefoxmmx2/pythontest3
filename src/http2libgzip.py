'''
Created on 2011-2-11

@author: hooxin
'''

import httplib2

h=httplib2.Http('.cache')
response,content=h.request('http://diveintopython3.org/')
print(dict(response.items()))