
import urllib.request

a_url='http://diveintopython3.org/examples/feed.xml'
data=urllib.request.urlopen(a_url).read()
print(type(data))
print(data)

